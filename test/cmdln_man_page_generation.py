#!/usr/bin/env python

"""
    $ python cmdln_man_page_generation.py
"""

import sys
import cmdln

class Shell(cmdln.Cmdln):
    def get_optparser(self):
        """ the parser"""

        optparser = cmdln.CmdlnOptionParser(self, version="1.2.3")
        optparser.add_option("--foobar", action="store_true",
                help="dskjdsfjkdsfkjdsfj kjdfs dsfkj kj dsfkjdfs dfkj dsfkjdf sf dskjkdjs f!")
        return optparser

    @cmdln.option("-k", "--keeekkeke", help="This ksdl fslkd dsflkdfslksd flkdsf lksdf sdlk sdflkdsf lksdis the kekeke.", action="store_true")
    def do_foo(self, argv):
        """shazam!

        ${cmd_option_list}
        """
        print("hello from foo")

    @cmdln.alias("fuuzbaba")
    def do_fuz(self, argv):
        "zizing!"
        print("hello from fuz")

    @cmdln.alias("barbababa")
    @cmdln.group("all")
    def do_bar(self, argv):
        "whopee!"
        print("hello from bar")

    @cmdln.group("all")
    def do_buz(self, argv):
        "kaboom!"
        print("hello from buz")

    def _do_baz(self, argv):
        "kazinga!"
        print("hello from baz")

    @cmdln.group("all", "foobar")
    def do_fez(self, argv):
        "pojoing!"
        print("hello from fez")

    @cmdln.group("foobar")
    def do_buz(self, argv):
        "buzzzzz!"
        print("hello from buz")

if __name__ == "__main__":
    shell = Shell()
    print(''.join(cmdln.man_sections_from_cmdln(shell, "jepajee")))
