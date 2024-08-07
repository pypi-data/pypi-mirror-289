#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Guy-Yann VECTOL"
__credits__ = ["Guy-Yann VECTOL"]
__Lisence__ = "BSD"
__maintainer__ = "Guy-Yann VECTOL"
__email__ = "guyyann.vectol@gmail.com"
__status__ = "Development"
__version__ = "0.0.1"

# Default python packages
import logging
import os
import time


class TransPyJs:
    """Class that allows the developper to use Transcript with ease"""

    def __init__(self, conf_path=os.path.join(os.path.expanduser("~"),
                                              ".work_login.conf")):
        """Saves config file location"""

        self.conf_path = conf_path

    def login(self):
        """Logs user in through terminal"""

        # Configures config file if not done so already
        if not os.path.exists(self.conf_path):
            self.configure()
        # Opens a terminal
        os.system("gnome-terminal")
        time.sleep(1)
        with open(self.conf_path, "r") as f:
            for cmd in f:
                self._run_cmd(cmd)

    def configure(self):
        """Configures file that will contain commands to run"""

        logging.info("Configuring work login")
        cmds = [input("Next command, or hit enter:\n")]
        # Ugh needs 3.6 compatibility, but with 3.8 could use walrus here
        while cmds[-1] != "":
            cmds.append(input("Next command, or hit enter:\n"))
        with open(self.conf_path, "w+") as f:
            f.write("\n".join(cmds))

    def _run_cmd(self, cmd):
        """Runs a command slowly so as not to error"""

        new_cmd = cmd.replace("\n", "")
        for c in new_cmd:
            self._type_key(c)
        time.sleep(.1)

if __name__ == "__main__":
    TransPyJs().login()
    
