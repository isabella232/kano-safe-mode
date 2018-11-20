#!/usr/bin/env groovy

@Library('kanolib')
import build_deb_pkg


def repo_name = 'kano-safe-mode'


stage ('Build') {
    autobuild_repo_pkg "$repo_name"
}
