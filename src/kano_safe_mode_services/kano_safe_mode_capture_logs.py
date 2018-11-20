# kano_safe_mode_capture_logs.py
#
# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO


import os
import subprocess
# from kano.utils.audio import play_sound

from kano_safe_mode_services.paths import LOGS_PATH, TMP_LOGS_PATH, \
    TMP_LOGS_OUTPUT_PATH, LOGS_FLAG_PATH

# SOUND_FILE = "res/sounds/kano_captured_logs.wav"

# Ensure we have some space left in /boot after writing logs
SPACE_MARGIN = 10000


def _clear_logs_already_sent_flag():
    """TODO"""
    if os.path.exists(LOGS_FLAG_PATH):
        os.remove(LOGS_FLAG_PATH)


def _capture_logs():
    rc = os.system(
        'USER=root LOGNAME=root HOME=/root'
        ' kano-feedback-cli --output {}'
        ' >{} 2>&1'
        .format(TMP_LOGS_PATH, TMP_LOGS_OUTPUT_PATH)
    )
    if rc != 0:
        rc = _store_logging_error()
    return rc


def _store_logging_error():
    return os.system("tar czf {} {}".format(TMP_LOGS_PATH, TMP_LOGS_OUTPUT_PATH))


def _get_boot_space():
    lines = subprocess.check_output(
        "df -k /boot/ --output=avail".split(" ")
    ).split("\n")
    return int(lines[1])


def _get_log_size():
    return os.stat(TMP_LOGS_PATH).st_size / 1024


def main():
    # Ensure script is run as root.
    if os.getuid() != 0:
        return 10

    # Generating new logs, ensure they'll be sent.
    _clear_logs_already_sent_flag()

    _capture_logs()

    if (_get_boot_space() - _get_log_size()) > SPACE_MARGIN:
        os.system("cp {} {}".format(TMP_LOGS_PATH, LOGS_PATH))

        # Only sync the boot partition to disk in case of power failure.
        os.system("syncfs <{}".format(LOGS_PATH))
        # play_sound(SOUND_FILE)
