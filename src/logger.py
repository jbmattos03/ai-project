import structlog
import logging
from typing import Optional

import os
from dotenv import load_dotenv
load_dotenv()

def logger_config(process_name: Optional[str], level: str = os.getenv("LOG_LEVEL"), pretty: bool = True):
    """
    Configures the logger for the application.

    :param process_name: Name of the process for which the logger is being configured.
    :param level: Logging level (default is logging.INFO).
    :param pretty: If True, configures the logger to use pretty formatting.
    """
    if not level or level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        level = "INFO" # Default logging level if not set in environment or invalid

    logging.basicConfig(level=level)

    processors = [
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.dev.ConsoleRenderer() if pretty else structlog.processors.JSONRenderer()
    ]

    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    logger = structlog.get_logger().bind(process=process_name) if process_name else structlog.get_logger()

    return logger