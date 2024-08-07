from concurrent.futures import ProcessPoolExecutor
import logging
import os
from os import PathLike
from pathlib import Path
import shutil
import sys
import traceback

import numpy
from pyproj import CRS, Geod, Transformer
from shapely.geometry import Point


def repository_root(path: PathLike = None) -> Path:
    if path is None:
        path = __file__
    if not isinstance(path, Path):
        path = Path(path)
    if path.is_file():
        path = path.parent
    if '.git' in (child.name for child in path.iterdir()) or path == path.parent:
        return path
    else:
        return repository_root(path.parent)


def get_logger(
    name: str,
    log_filename: PathLike = None,
    file_level: int = None,
    console_level: int = None,
    log_format: str = None,
) -> logging.Logger:
    """
    instantiate logger instance

    :param name: name of logger
    :param log_filename: path to log file
    :param file_level: minimum log level to write to log file
    :param console_level: minimum log level to print to console
    :param log_format: logger message format
    :return: instance of a Logger object
    """

    if file_level is None:
        file_level = logging.DEBUG
    if console_level is None:
        console_level = logging.INFO
    logger = logging.getLogger(name)

    # check if logger is already configured
    if logger.level == logging.NOTSET and len(logger.handlers) == 0:
        # check if logger has a parent
        if '.' in name:
            if isinstance(logger.parent, logging.RootLogger):
                for existing_console_handler in [
                    handler
                    for handler in logger.parent.handlers
                    if not isinstance(handler, logging.FileHandler)
                ]:
                    logger.parent.removeHandler(existing_console_handler)
            logger.parent = get_logger(name.rsplit('.', 1)[0])
        else:
            # otherwise create a new split-console logger
            if console_level != logging.NOTSET:
                for existing_console_handler in [
                    handler
                    for handler in logger.handlers
                    if not isinstance(handler, logging.FileHandler)
                ]:
                    logger.removeHandler(existing_console_handler)

                console_output = logging.StreamHandler(sys.stdout)
                console_output.setLevel(console_level)
                logger.addHandler(console_output)

    if log_filename is not None:
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(file_level)
        for existing_file_handler in [
            handler for handler in logger.handlers if isinstance(handler, logging.FileHandler)
        ]:
            logger.removeHandler(existing_file_handler)
        logger.addHandler(file_handler)

    if log_format is None:
        log_format = '[%(asctime)s] %(name)-15s %(levelname)-8s: %(message)s'
    log_formatter = logging.Formatter(log_format)
    for handler in logger.handlers:
        handler.setFormatter(log_formatter)

    return logger


LOGGER = get_logger('cplmdldrv')


def create_symlink(
    source_filename: PathLike, symlink_filename: PathLike, relative: bool = False
):
    if not isinstance(source_filename, Path):
        source_filename = Path(source_filename)
    if not isinstance(symlink_filename, Path):
        symlink_filename = Path(symlink_filename)

    if not symlink_filename.parent.exists():
        symlink_filename.parent.mkdir(parents=True, exist_ok=True)

    if symlink_filename.is_symlink():
        LOGGER.debug(f'removing symlink "{symlink_filename}"')
        os.remove(symlink_filename)
    symlink_filename = symlink_filename.parent.absolute().resolve() / symlink_filename.name

    starting_directory = None
    if relative:
        starting_directory = Path().cwd().resolve()
        os.chdir(symlink_filename.parent)
        if os.path.isabs(source_filename):
            try:
                source_filename = Path(
                    os.path.relpath(source_filename, symlink_filename.parent)
                )
            except ValueError as error:
                LOGGER.warning(error)
                os.chdir(starting_directory)
    else:
        source_filename = source_filename.absolute()

    try:
        symlink_filename.symlink_to(source_filename)
    except Exception as error:
        LOGGER.warning(f'could not create symbolic link: {error}')
        shutil.copyfile(source_filename, symlink_filename)
    finally:
        if starting_directory is not None:
            os.chdir(starting_directory)


def ellipsoidal_distance(
    point_a: (float, float), point_b: (float, float), crs_a: CRS, crs_b: CRS = None
) -> float:
    if isinstance(point_a, Point):
        point_a = [*point_a.coords]
    if isinstance(point_b, Point):
        point_b = [*point_b.coords]
    if crs_b is not None:
        transformer = Transformer.from_crs(crs_b, crs_a)
        point_b = transformer.transform(*point_b)
    points = numpy.stack((point_a, point_b), axis=0)
    ellipsoid = crs_a.datum.to_json_dict()['ellipsoid']
    geodetic = Geod(a=ellipsoid['semi_major_axis'], rf=ellipsoid['inverse_flattening'])
    return geodetic.line_length(points[:, 0], points[:, 1])


def make_executable(path: PathLike):
    """
    https://stackoverflow.com/questions/12791997/how-do-you-do-a-simple-chmod-x-from-within-python
    """
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2  # copy R bits to X
    os.chmod(path, mode)


class ProcessPoolExecutorStackTraced(ProcessPoolExecutor):
    """
    preserves the traceback of any kind of raised exception
    """

    def submit(self, fn, *args, **kwargs):
        return super(ProcessPoolExecutorStackTraced, self).submit(
            self._function_wrapper, fn, *args, **kwargs,
        )

    @staticmethod
    def _function_wrapper(fn, *args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception:
            # Creates an exception of the same type with the traceback as message
            raise sys.exc_info()[0](traceback.format_exc())
