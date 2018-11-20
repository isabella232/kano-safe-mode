# check_kano_safe_mode.py
#
# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO


import os

from kano.logging import logger
from kano.utils.shell import run_cmd
from kano.utils.file_operations import touch

from kano_safe_mode.paths import SAFE_MODE_REQUESTED_FLAG_PATH, SAFE_MODE_FLAG_PATH


def set_safe_mode_requested():
    """
    Requires sudo.
    """

    touch(SAFE_MODE_REQUESTED_FLAG_PATH)
    os.system('sudo systemctl start kano-safe-mode-requested.target')


def was_safe_mode_requested():
    """TODO"""

    return os.path.exists(SAFE_MODE_REQUESTED_FLAG_PATH)


def clear_safe_mode_requested():
    """TODO"""

    os.remove(SAFE_MODE_REQUESTED_FLAG_PATH)


def set_safe_mode():
    """
    Requires sudo.
    """

    touch(SAFE_MODE_FLAG_PATH)
    os.system('sudo systemctl start kano-safe-mode.target')


def was_safe_mode():
    """TODO"""

    return os.path.exists(SAFE_MODE_FLAG_PATH)


def clear_safe_mode():
    """TODO"""

    os.remove(SAFE_MODE_FLAG_PATH)


def check_safe_mode_hotkeys(blink_leds=False):
    """Check for Safe Mode keys being pressed.

    Returns:
        bool: whether or not the Safe Mode keys were pressed
    """

    if blink_leds:
        # Start a board LED blink in the background for a few seconds
        # so the user knows it's time to press Ctrl-Alt
        _, _, _ = run_cmd("/usr/bin/kano-led &")

    _, _, rv = run_cmd("kano-keys-pressed -r 5 -d 10")
    return (rv == 10)


def main():
    """TODO"""

    if os.getuid() != 0:
        return 10

    logger.force_log_level('info')

    if was_safe_mode_requested():
        logger.warn("Safe Mode boot")
        clear_safe_mode_requested()
        set_safe_mode()
        return

    elif was_safe_mode():
        clear_safe_mode()

    if check_safe_mode_hotkeys():
        logger.warn("Safe Mode requested")
        set_safe_mode_requested()
        run_cmd('kano-checked-reboot safeboot systemctl reboot')
        return
