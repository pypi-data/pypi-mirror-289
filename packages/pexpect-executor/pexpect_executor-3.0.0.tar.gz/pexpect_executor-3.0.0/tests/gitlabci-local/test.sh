#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
pexpect-executor --down --space --enter -- gitlabci-local
pexpect-executor --press a --press a --enter -- gitlabci-local
pexpect-executor --wait 2 --enter -- gitlabci-local
pexpect-executor --ctrl c -- gitlabci-local
