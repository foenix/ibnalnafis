#!/usr/bin/env python
# Pandoc wrapper
import subprocess

def rst2html(rst):
    proc = subprocess.Popen(['pandoc', '--from=rst', '--to=rst'],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return proc.communicate(rst)[0]
