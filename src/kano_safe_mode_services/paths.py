# paths.py
#
# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# Paths used throughout this package.


from os.path import join, abspath, dirname


# This is the default install path for our config stuff
BASE_DIR = '/usr/share/kano-safe-mode-services'
LOCAL_DIR = abspath(join(dirname(__file__), '..', '..'))
RES_DIR = BASE_DIR
if not LOCAL_DIR.startswith('/usr'):
    BASE_DIR = LOCAL_DIR
    RES_DIR = join(BASE_DIR, 'res')

SOUNDS_DIR = join(RES_DIR, 'sounds')

TMP_DIR = '/tmp'
BOOT_DIR = '/boot'
FLAGS_DIR = '/var/tmp/kano-safe-mode-services'

CONFIG_TXT_PATH = join(BOOT_DIR, 'config.txt')
CONFIG_TXT_BACKUP_PATH = CONFIG_TXT_PATH + '.bck'

KANUX_STAMP_PATH = join(BOOT_DIR, 'kanux_stamp')

LOGS_PATH = join(BOOT_DIR, 'support_logs.tgz')
TMP_LOGS_PATH = join(TMP_DIR, 'support_logs.tgz')
TMP_LOGS_OUTPUT_PATH = join(TMP_DIR, 'support_logs_log.txt')

LOGS_FLAG_PATH = join(FLAGS_DIR, 'ksm-logs-sent')
