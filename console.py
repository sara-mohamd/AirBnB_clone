#!/usr/bin/python3
"""The console"""
import cmd



class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """quit command to exit the program."""
        return True

    def emptyline(self):
        """Empty line + Enter should't execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
