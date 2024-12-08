# encode : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import yaml

from typing import TypedDict
from pathlib import Path


class Config(TypedDict):
    GUILD_ID: int
    TEST_CHANNEL_ID: int
    MODE: str
    ADMINSTRATION_CHANNEL_ID: int
    ADVENT_CALENDAR_CHANNEL_ID: int


def load_config(path: Path) -> Config:
    with open(path, "r") as file:
        config = yaml.safe_load(file)
    return validate_config(config)


def validate_config(config: Config) -> Config:
    config["ADVENT_CALENDAR_CHANNEL_ID"] = (
        config["ADVENT_CALENDAR_CHANNEL_ID"]
        if config["MODE"] == "production"
        else config["TEST_CHANNEL_ID"]
    )
    for key in config.keys():
        if config[key] is None:
            raise Exception(f"{key} is not set in config")
    return config
