#!/usr/bin/python3
"""HBNB console"""

import cmd
import models
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

    def my_errors(self, line, args_number):
        """
        Displays error messages to user
        Args:
            line(any): gets user input using command line
            num_of_args(int): number of input arguments
        Description:
            Displays output to the use based on
            the input commands.
        """
        classes = [
        "BaseModel",
        ]

        message = [
                    "** class name missing **",
                    "** class doesn't exist **",
                    "** instance id missing **",
                    "** no instance found **",
                    "** attribute name missing **",
                    "** value missing **"
        ]

        if not line:
            print(message[0])
            return 1
        args = line.split()
        if args_number >= 1 and args[0] not in classes:
            print(message[1])
            return 1
        elif args_number == 1:
            return 0
        if args_number >= 2 and len(args) < 2:
            print(message[2])
            return 1
        d = storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        if args_number >= 2 and key not in d:
            print(message[3])
            return 1
        elif args_number == 2:
            return 0
        if args_number >= 4 and len(args) < 3:
            print(message[4])
            return 1
        if args_number >= 4 and len(args) < 4:
            print(message[5])
            return 1
        return 0

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id
        Arguments:
            args: Arguments to enter with command: <class name>
            Example: 'create User'
        """

        if (self.my_errors(args, 1) == 1):
            return
        my_list = args.split(" ")

        obj = eval(my_list[0])()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance 
        based on the class name and id
        """

        if (self.my_errors(args, 2) == 1):
            return
        dicts = args.split()
        store = storage.all()
        if dicts[1][0] == '"':
            dicts[1] = dicts[1].replace('"', "")
        key = dicts[0] + '.' + args[1]
        print(store[key])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
