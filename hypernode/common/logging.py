from logging import DEBUG, INFO, Logger, StreamHandler


def configure_logging(debug: bool, logger: Logger) -> None:
    level = DEBUG if debug else INFO
    logger.setLevel(level)
    ch = StreamHandler()
    logger.addHandler(ch)
