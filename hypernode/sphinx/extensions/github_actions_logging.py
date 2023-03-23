import logging
import os
import sys
from collections import defaultdict
from typing import TYPE_CHECKING

from sphinx.util.logging import (
    NAMESPACE,
    OnceFilter,
    SafeEncodingWriter,
    SphinxLogRecord,
    WarningLogRecordTranslator,
    WarningStreamHandler,
    WarningSuppressor,
)

if TYPE_CHECKING:
    from sphinx.application import Sphinx

LOG_TYPE_MAP = defaultdict(
    lambda: "error",
    {
        logging.ERROR: "error",
        logging.WARNING: "warning",
    },
)


class GithubFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        log_type = LOG_TYPE_MAP[record.levelno]
        if isinstance(record, SphinxLogRecord):
            file, line = record.location.split(":")
            return f"::{log_type} file={file},line={line}::{record.msg}"
        else:
            return f"::{log_type}::{message}"


def setup_logging(app: "Sphinx"):
    logger = logging.getLogger(NAMESPACE)
    github_handler = WarningStreamHandler(SafeEncodingWriter(sys.stdout))
    github_handler.addFilter(WarningSuppressor(app))
    github_handler.addFilter(WarningLogRecordTranslator(app))
    github_handler.addFilter(OnceFilter())
    github_handler.setLevel(logging.WARNING)
    github_handler.setFormatter(GithubFormatter())
    logger.addHandler(github_handler)


def setup(app: "Sphinx"):
    if os.getenv("GITHUB_WORKFLOW"):
        setup_logging(app)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
