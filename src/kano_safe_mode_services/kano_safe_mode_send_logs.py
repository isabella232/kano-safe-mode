# kano_safe_mode_send_logs.py
#
# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO


import os
import time

from kano.utils.shell import run_cmd
from kano.logging import logger

from kano_safe_mode_services.paths import LOGS_FLAG_PATH, LOGS_PATH, \
    TMP_LOGS_OUTPUT_PATH


def _logs_already_sent():
    """TODO"""
    return os.path.exists(LOGS_FLAG_PATH)


def main():
    # Ensure script is not run as root.
    if os.getuid() == 0:
        return 10

    if _logs_already_sent():
        return

    if not os.path.exists(LOGS_PATH):
        return

    # Service is running too early in user space. Give the system some
    # time to settle.
    time.sleep(30)

    out, err, rc = run_cmd(
        'kano-feedback-cli'
        '   --title "Kano OS: Safe Mode Boot Logs"'
        '   --description "Kano OS booted into Safe Mode. Debugging logs attached."'
        '   --send --logs {path}'
        '   --flag {flag}'
        '   >{output} 2>&1'
        .format(
            path=LOGS_PATH,
            flag=LOGS_FLAG_PATH,
            output=TMP_LOGS_OUTPUT_PATH
        )
    )
    if rc != 0:
        logger.error('Could not send logs, kano-feedback-cli rc {}'.format(rc))
        return 20
