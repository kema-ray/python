#!/usr/bin/python3
"""HBNB console"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Defines HBNB command interpreter
    Attributes:
        prompt(str) : command prompt
    """

    prompt = "(hbnb)"
    __classes = {
        "BaseModel",
    }

    def emptyline(self):
        """Do nothing upon receiving and empty line"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF to exit the program"""
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
