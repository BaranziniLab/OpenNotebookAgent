"""Command-line entry point for OpenNotebookAgent."""

import logging
import os

from opennotebookagent.server import main as server_main

logger = logging.getLogger("OpenNotebookAgent")


def main() -> None:
    log_level = os.getenv("OPEN_NOTEBOOK_LOG_LEVEL", "INFO")
    logging.basicConfig(level=getattr(logging, log_level.upper(), logging.INFO))
    logger.info("Starting OpenNotebookAgent")
    server_main(log_level=log_level)


if __name__ == "__main__":
    main()
