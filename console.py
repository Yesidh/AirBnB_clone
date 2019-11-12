#!/usr/bin/python3
"""
======================================================
Module with the entry point of the command interpreter
======================================================
"""
import cmd
import os
import shlex
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""

    intro = 'Welcome the Airbnb console, type help for help or quit for close'
    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "Place",  # List of classes we might need
               "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """method for close and exit from the console"""

        print("Chao PapAA")
        return True

    def do_EOF(self, arg):
        """method for exit from the console"""
        print("\nya no hay mas que leer")
        exit()

    def do_create(self, arg):

        if len(arg) < 1:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()  # this saves it into the file.json
            print(new.id)

    def do_show(self, arg):

        data = arg.split()
        my_list = []
        if len(data) < 1:
            print("** class name missing **")
        elif not data[0] in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(data) < 2:
            print("** instance id missing **")
        else:
            key = data[0] + "." + data[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                my_list.append("[{}] ({}) {}".format(data[0],
                               data[1], storage.all()[key]))
                print(my_list)

    def do_destroy(self, arg):

        data = arg.split()
        if len(data) < 1:
            print("** class name missing **")
        elif not data[0] in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(data) < 2:
            print("** instance id missing **")
        else:
            key = data[0] + "." + data[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(key)  # Deletes the key of the dict
                storage.save()  # Saves the file,json

    def do_all(self, arg):

        data = shlex.split(arg)
        my_list = []
        if len(arg) < 1:  # If only typed all
            # Print all the items of storage
            for key, value in storage.all().items():
                c_name, c_id = key.split(".")
                my_list.append("{}".format(value))
            print(my_list)
        else:
            if not data[0] in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                # print all the keys with data[0]
                for key, value in storage.all().items():
                    c_name, c_id = key.split(".")
                    if c_name == data[0]:
                        my_list.append("{}".format(value))
                print(my_list)

    def do_update(self, arg):
        """Updates and instance"""

        # Splits in shell syntax (for strings as arguments)
        data = shlex.split(arg)
        if len(data) < 1:
            print("** class name missing **")
        elif not data[0] in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(data) < 2:
            print("** instance id missing **")
        else:
            key = data[0] + "." + data[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(data) < 3:
                print("** attribute name missing **")
            elif len(data) < 4:
                print("** value missing **")
            else:
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    obj = storage.all().get(key)
                    setattr(obj, data[2], data[3])
                    storage.save()
            # Do we need to check the agument type???

    def do_clear(self, arg):
        """Clearses the screen"""

        os.system('clear')

    def emptyline(self):
        """empty line"""

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()