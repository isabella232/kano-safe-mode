# kano_safe_mode_config.py
#
# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO


import os

from kano_settings.system.display import set_screen_value
from kano_settings.boot_config import set_config_value, config_copy_to, \
    end_config_transaction
from kano.logging import logger

from kano_safe_mode_services.paths import CONFIG_TXT_BACKUP_PATH


def set_safe_mode_config():
    """
    Requires sudo.
    """

    set_screen_value('hdmi_force_hotplug', 1)
    set_config_value('hdmi_force_hotplug', 1)

    set_screen_value('config_hdmi_boost', 4)
    set_config_value('config_hdmi_boost', 4)

    set_screen_value('hdmi_group', None)
    set_config_value('hdmi_group', None)

    set_screen_value('hdmi_mode', None)
    set_config_value('hdmi_mode', None)

    set_screen_value('hdmi_drive', None)
    set_config_value('hdmi_drive', None)

    set_screen_value('disable_overscan', 1)
    set_config_value('disable_overscan', 1)

    set_screen_value('overscan_left', 0)
    set_config_value('overscan_left', 0)

    set_screen_value('overscan_right', 0)
    set_config_value('overscan_right', 0)

    set_screen_value('overscan_top', 0)
    set_config_value('overscan_top', 0)

    set_screen_value('overscan_bottom', 0)
    set_config_value('overscan_bottom', 0)


def main():
    """TODO"""

    if os.getuid() != 0:
        return 10

    logger.warn("Applying Safe Mode config.txt settings")

    config_copy_to(CONFIG_TXT_BACKUP_PATH)
    set_safe_mode_config()
    end_config_transaction()
