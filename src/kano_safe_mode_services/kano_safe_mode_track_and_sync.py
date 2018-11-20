# kano_safe_mode_track_and_sync.py
#
# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO


import os
import json

from kano_profile.tracker import track_data
from kano_settings.system.audio import is_HDMI
from kano.utils.file_operations import read_file_contents_as_lines
from kano.utils.shell import run_cmd

from kano_safe_mode_services.paths import CONFIG_TXT_PATH, KANUX_STAMP_PATH


def _get_kano_os_version_stamp():
    """Read the version of the OS when it was built"""
    return read_file_contents_as_lines(KANUX_STAMP_PATH)[-1].strip().split()[-1]


def _get_config_txt():
    """Read the RPi config.txt file"""
    return read_file_contents_as_lines(CONFIG_TXT_PATH)


def _get_display_name():
    """TODO"""
    display_name, err, rc = run_cmd('tvservice --name')
    return display_name.strip()


def _get_display_status():
    """TODO"""
    display_status, err, rc = run_cmd('tvservice --status')
    return display_status.strip()


def _get_display_modes(mode):
    """TODO"""
    display_modes, err, rc = run_cmd('tvservice --json --modes {}'.format(mode))
    try:
        return json.loads(display_modes)
    except:
        return list()


def _get_disk_space_usage():
    """TODO"""
    disk_space_usage, err, rc = run_cmd('df --human-readable')
    return disk_space_usage.splitlines()


def main():
    track_data(
        'safe-mode-boot',
        {
            'os-version-stamp': _get_kano_os_version_stamp(),
            'config-txt': _get_config_txt(),
            'display-name': _get_display_name(),
            'display-status': _get_display_status(),
            'display-modes-cea': _get_display_modes('cea'),
            'display-modes-dmt': _get_display_modes('dmt'),
            'hdmi-audio-output': is_HDMI(),
            'disk-space-usage': _get_disk_space_usage()
        }
    )
    os.system('kano-sync --skip-kdesk --upload-tracking-data --silent')
