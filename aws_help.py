"""Replaces ``aws help`` with ``aws --help``."""

import sys
from typing import Sequence

__version__ = "0.0.1"


if sys.platform == "win32":
    import subprocess

    def execvp(cmd: str, args: Sequence[str]) -> int:
        """Mocking the behavior of execvp on Windows system."""
        return subprocess.call(args)

else:
    from os import execvp


def main() -> int:
    """Entrypoint to aws_help.

    By default, AWS CLI doesn't offer the usual ``-h`` or ``--help``
    flags. This function takes care of that by replacing the parent
    python process by ``aws help``.

    :Example:

        .. code-block:: console

            $ python3 aws_help.py --help

    .. seealso::

        [1] https://blog.devgenius.io/execvp-system-call-in-python-everything-you-need-to-know-c402fe6886eb
    """
    if "-h" not in sys.argv and "--help" not in sys.argv:
        return execvp("aws", sys.argv)
    cmd = ["aws"]
    for arg in sys.argv[1:]:
        if arg.startswith("-"):
            break
        else:
            cmd.append(arg)
    cmd.append("help")
    return execvp(cmd[0], cmd)


if __name__ == "__main__":
    raise SystemExit(main())
