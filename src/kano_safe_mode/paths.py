# paths.py
#
# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# Paths used throughout this package.


import os


CACHE_DIR = '/var/cache/kano-safe-mode'
SAFE_MODE_REQUESTED_FLAG_NAME = 'safe-mode-requested-flag'
SAFE_MODE_REQUESTED_FLAG_PATH = os.path.join(CACHE_DIR, SAFE_MODE_REQUESTED_FLAG_NAME)
SAFE_MODE_FLAG_NAME = 'safe-mode-flag'
SAFE_MODE_FLAG_PATH = os.path.join(CACHE_DIR, SAFE_MODE_FLAG_NAME)
