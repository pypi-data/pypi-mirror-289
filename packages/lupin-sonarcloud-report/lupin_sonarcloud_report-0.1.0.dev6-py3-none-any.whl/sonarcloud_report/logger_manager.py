import logging


def configure_logger():
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )


configure_logger()


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)
    exit(1)
