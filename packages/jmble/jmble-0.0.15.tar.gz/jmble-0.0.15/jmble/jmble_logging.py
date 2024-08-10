""" Utilities to configure logging using the Configurator """

import logging
import logging.config
import os

from jmble.config import Configurator
from jmble.general_modules import utils
from jmble._types import AttrDict

CONFIG = Configurator()
ENV_PROPS = CONFIG.get_environment()


def configure_logging(
    app_name: str = None, default_logger_name: str = "console_logger"
) -> logging.Logger:
    """Configure logging using the Configurator.

    Args:
        app_name (str, optional): Name of the application. Defaults to None.
        default_logger_name (str, optional): Name of the default logger to return. Defaults to "console_logger".

    Returns:
        logging.Logger: Logger instance.
    """

    app_props = CONFIG.get(app_name) if app_name else AttrDict()

    log_config = CONFIG.get("base_python_log_cfg", AttrDict())

    if not isinstance(log_config, AttrDict) and isinstance(log_config, dict):
        log_config = AttrDict(log_config)

    app_handlers = app_props.handlers
    app_loggers = app_props.loggers

    if isinstance(app_handlers, dict):
        log_config.handlers.update(app_handlers)

    if isinstance(app_loggers, dict):
        log_config.loggers.update(app_loggers)

    logging.config.dictConfig(log_config)

    return logging.getLogger(default_logger_name)
