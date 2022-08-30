"""AWS Help setup.

This will install the ``aws_help`` package in python 3.6+ environment.
Before proceeding, please ensure you have a virtual environment setup &
running.

See https://github.com/xames3/aws_help/ for more help.
"""

try:
    import setuptools
except ImportError:
    raise RuntimeError(
        "Could not install package in the environment as setuptools is "
        "missing. Please create a new virtual environment before proceeding."
    )

import platform

from pkg_resources import parse_version  # type: ignore

CURRENT_PYTHON_VERSION = platform.python_version()
MIN_PYTHON_VERSION = "3.6"

if parse_version(CURRENT_PYTHON_VERSION) < parse_version(MIN_PYTHON_VERSION):
    raise SystemExit(
        "Could not install `aws_help` in the environment. It requires python "
        f"version 3.6+, you are using {CURRENT_PYTHON_VERSION}"
    )

# BUG: Cannot install into user directory with editable source
# Using this solution: https://stackoverflow.com/a/68487739/14316408
# to solve the problem with installation. As of Aug, 2022 an issue is
# open on GitHub here: https://github.com/pypa/pip/issues/7953.

import site
import sys

site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

if __name__ == "__main__":
    setuptools.setup()
