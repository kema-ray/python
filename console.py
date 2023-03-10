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

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id 
        Arguments:
            args: to enter with command: <class name> <id>
            Example: 'destroy BaseModel 121212'
        """

        if (self.my_errors(args, 2) == 1):
            return
        arguments = args.split()
        stores = storage.all()
        if arguments[1][0] == '"':
            arguments[1] = arguments[1].replace('"',"")
        key = arguments[0] + '.' + arguments[1]
        del stores[key]
        storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances 
        based or not on the class name
        Arguments: 
            args: enter with command (optional): <class name>
            Example: 'all MyModel'
        """

        store = storage.all()
        if not args:
            print([str(x) for x in store.values()])
            return
        arguments = args.split()
        if (self.my_errors(args, 1) == 1):
            return
        print([str(i) for i in store.values() if i.__class__.__name__ == arguments[0]])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by 
        adding or updating attribute
        Arguments:
            args: receives the commands:
            <class name> <id> <attribute name> "<attribute value>"
            Example: update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = 
            $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """

        if (self.my_errors(args, 4) == 1):
            return
        arguments = args.split()
        store = storage.all()
        for i in range(len(arguments[1:]) + 1):
            if arguments[i][0] == '"':
                arguments[i] = arguments[i].replace('"', "")
        key = arguments[0] + '.' + arguments[1]
        attr_k = arguments[2]
        attr_j = arguments[3]
        try:
            if attr_j.isdigit():
                attr_j = int(attr_j)
            elif float(attr_j):
                attr_j = float(attr_j)
        except ValueError:
            pass
        class_attr = type(store[key]).__dict__
        if attr_k in class_attr.keys():
            try:
                attr_j = type(class_attr[attr_k])(attr_j)
            except Exception:
                print("Entered wrong value type")
                return
        setattr(store[key], attr_k, attr_j)
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
