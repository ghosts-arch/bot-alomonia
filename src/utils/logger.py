# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import logging.config
import yaml
import pathlib
import logging


def setup_logging():
    logger_config_file = pathlib.Path("logger.yaml")
    with open(logger_config_file, "r") as f:
        config = yaml.safe_load(f)
    logging.config.dictConfig(config=config)
