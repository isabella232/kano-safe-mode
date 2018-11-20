# kano_safe_mode_config_clear.py
#
# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO


import os

from kano_settings.boot_config import config_copy_from, end_config_transaction
from kano.logging import logger

from kano_safe_mode_services.paths import CONFIG_TXT_BACKUP_PATH


def main():
    """TODO"""

    if os.getuid() != 0:
        return 10

    logger.info('Reverting Safe Mode config.txt configuration')

    config_copy_from(CONFIG_TXT_BACKUP_PATH)
    os.remove(CONFIG_TXT_BACKUP_PATH)
    end_config_transaction()
