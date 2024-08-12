#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
DEBUG_UPDATES_DISABLE= pexpect-executor --version
DEBUG_UPDATES_DISABLE= pexpect-executor --update-check
FORCE_COLOR=1 DEBUG_UPDATES_DISABLE= pexpect-executor --update-check
NO_COLOR=1 DEBUG_UPDATES_DISABLE= pexpect-executor --update-check
FORCE_COLOR=1 PYTHONIOENCODING=ascii DEBUG_UPDATES_DISABLE= pexpect-executor --update-check
FORCE_COLOR=1 DEBUG_UPDATES_DISABLE= COLUMNS=40 pexpect-executor --update-check
FORCE_COLOR=1 DEBUG_UPDATES_DISABLE= DEBUG_UPDATES_OFFLINE=true pexpect-executor --update-check
FORCE_COLOR=1 DEBUG_UPDATES_DISABLE= DEBUG_UPDATES_OFFLINE=true DEBUG_VERSION_FAKE=0.0.2 DEBUG_UPDATES_FAKE=0.0.1 pexpect-executor --update-check
FORCE_COLOR=1 DEBUG_UPDATES_DISABLE= DEBUG_UPDATES_OFFLINE=true DEBUG_VERSION_FAKE=0.0.2 DEBUG_UPDATES_FAKE=0.0.2 pexpect-executor --update-check
FORCE_COLOR=1 DEBUG_UPDATES_DISABLE= DEBUG_UPDATES_OFFLINE=true DEBUG_VERSION_FAKE=0.0.2 DEBUG_UPDATES_FAKE=0.0.3 pexpect-executor --update-check
FORCE_COLOR=1 DEBUG_UPDATES_DISABLE= DEBUG_UPDATES_DAILY=true DEBUG_VERSION_FAKE=0.0.2 DEBUG_UPDATES_FAKE=0.0.3 pexpect-executor -- echo 'Test'
FORCE_COLOR=1 DEBUG_UPDATES_DISABLE= pexpect-executor -- echo 'Test'
