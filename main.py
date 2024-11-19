# encode : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import logging.config
import os
import dotenv

from src.core.client import LuneaMoon
from src.utils.logger import setup_logging


def main():
    logger = logging.getLogger(__name__)
    setup_logging()
    dotenv.load_dotenv()
    client = LuneaMoon()
    client_token = dotenv.get_key(
        dotenv_path=dotenv.find_dotenv(), key_to_get="CLIENT_TOKEN", encoding="utf-8"
    )
    if not client_token:
        logger.error("No client token found in .env file")
        exit(1)
    if client_token:
        client.run(client_token)


if __name__ == "__main__":
    main()
