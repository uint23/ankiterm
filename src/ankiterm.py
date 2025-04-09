# ANKITERM
# (}) 2025 Abhinav Prasai
# https://uint23.xyz/
# https://github.com/uint23/
#
# MIT License
#
# Copyright (c) 2025 uint23
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Libs
import sys
import utils
import run


# Messages
VERSIONMSG = """
LICENSE: MIT
(!C) Abhinav Prasai 2025
https://github.com/uint23
https://uint23.xyz/

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
See 'ankiterm.py' for full license
"""
HELPMSG = """
USEAGE:
    [-v || --version] - Displays version and other information
    [-h || --help]    - Displays help information
"""


# Functions
def checkargs():
    if (len(sys.argv) == 1):
        return

    av = sys.argv[1];
    if (av == "--version" or av == "-v"):
        utils.die(VERSIONMSG, 0)
    if (av == "--help" or av == "-h"):
        utils.die(HELPMSG, 0)
    else:
        utils.die(HELPMSG, 0)


if __name__ == "__main__":
    checkargs()
    run.run()
