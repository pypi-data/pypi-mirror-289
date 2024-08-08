import sys
import json
from typing import Optional
import datetime
import logging
from gunicorn import glogging
from flask import request


# def get_logger():
#     return logging.getLogger(__name__)


class CustomFormatter(logging.Formatter):

    def format(self, record):
        message = super().format(record)
        try:
            test_id = request.headers.get("X-Test-Id")
            session_id = request.headers.get("X-Session-Id")
            request_id = request.headers.get("X-Request-Id")
            # TODO: if None (so nothing use the framework!)
        except RuntimeError as e:
            err_msg = e.args[0]
            outside_context_message = "Working outside of request context."
            if len(err_msg) > 35 and err_msg.startswith(outside_context_message):
                session_id = "no-session-id"
                test_id = "no-test-id"
                request_id = "no-request-id"
            else:
                raise e
        json_message = {
            "message": message,
            "time": datetime.datetime.now(datetime.timezone.utc)
            .isoformat()
            .replace("+00:00", "Z"),
            "severity": record.levelname,
            "session_id": session_id,
            "test_id": test_id,
            "request_id": request_id,
        }
        return json.dumps(json_message)


def get_stream_handler():
    formatter = CustomFormatter()
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    return stream_handler


def update_root_logger():
    stream_handler = get_stream_handler()
    # all loggers should have same formatting, so setting at root level
    root_logger = logging.getLogger()
    root_logger.addHandler(stream_handler)
    root_logger.setLevel(level=logging.DEBUG)


update_root_logger()


def info(*args, **kwargs):
    logging.getLogger(__name__).info(*args, **kwargs)


def debug(*args, **kwargs):
    logging.getLogger(__name__).debug(*args, **kwargs)


def warning(*args, **kwargs):
    logging.getLogger(__name__).warning(*args, **kwargs)


def error(*args, **kwargs):
    logging.getLogger(__name__).error(*args, **kwargs)


def critical(*args, **kwargs):
    logging.getLogger(__name__).error(*args, **kwargs)
