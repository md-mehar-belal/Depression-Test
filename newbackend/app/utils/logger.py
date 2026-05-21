import logging
import os

def setup_logger(
    name: str,
    log_file_path: str | None = None
) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(
        os.getenv("LOG_LEVEL", "INFO")
    )
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(name)s: %(message)s"
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # CONTRACT ISSUE:
    # logging_service passed a log-file path to get_logger(), but this
    # utility accepted only a logger name. That violated the utility
    # contract and prevented logging_service from importing.
    #
    # Legacy behavior remains: callers may still pass only the name.
    if log_file_path:
        os.makedirs(
            os.path.dirname(log_file_path),
            exist_ok=True
        )

        file_handler = logging.FileHandler(
            log_file_path
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def get_logger(
    name: str,
    log_file_path: str | None = None
) -> logging.Logger:
    return setup_logger(
        name,
        log_file_path
    )
