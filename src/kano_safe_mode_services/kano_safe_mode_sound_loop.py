# kano_safe_mode_sound_loop.py
#
# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO


import os

from kano.utils.audio import play_sound

from kano_safe_mode_services.paths import SOUNDS_DIR


def main():
    """TODO"""

    path = os.path.join(SOUNDS_DIR, 'kano_safe_mode.wav')

    while True:
        play_sound(path, delay=10)
