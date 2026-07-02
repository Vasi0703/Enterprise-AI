from config.settings import DEBUG
from utils.logger import logger


def trace(title: str):
    if not DEBUG:
        return

    logger.info("=" * 60)
    logger.info(title.upper())
    logger.info("=" * 60)