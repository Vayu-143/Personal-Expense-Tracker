import logging

from app.config import LOG_FILE


def setup_logging():

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def log_message(message):

    logging.info(message)