import logging


# logging.basicConfig(level=logging.ERROR)

# logging.debug("Debug message")
# logging.info("Info message")
# logging.warning("Warning message")
# logging.error("Error message")
# logging.critical("Critical message")

# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s | %(levelname)s | %(message)s | %(name)s",
#     datefmt="%Y-%m-%d %H:%M:%S"
# )

# logging.info("Testing")

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

logger.info("Program started")
logger.debug("Doing some extremely important goobering")
logger.warning("Goobering levels dangerously high")

try:
    number = int("goober")
except ValueError:
    logger.exception("Failed to convert value")