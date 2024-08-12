from __future__ import annotations

import subprocess

import pkg_resources


def runit(x):
    filename = pkg_resources.resource_filename(__name__, "testprogram")
    output = subprocess.check_output([filename, str(x)])
    return float(output)
