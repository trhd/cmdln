#!/usr/bin/env python

"""
    $ python cmdln_help_groups.py foo
    hello from foo
    $ python cmdln_help_groups.py fuz
    hello from fuz
    $ python cmdln_help_groups.py bar
    hello from bar
    $ python cmdln_help_groups.py barbababa
    hello from bar
    $ python cmdln_help_groups.py buz
    hello from buz
    $ python cmdln_help_groups.py baz
    hello from baz
    $ python cmdln_help_groups.py fez
    hello from fez
    $ python cmdln_help_groups.py buz
    hello from buz

    $ python cmdln_help_groups.py help
    Usage:
        cmdln_help_groups.py COMMAND [ARGS...]
        cmdln_help_groups.py help [COMMAND]
    <BLANKLINE>
    Options:
        -h, --help  show this help message and exit
    <BLANKLINE>
    Commands:
        foo             shazam!
        fuz (fuuzbaba)  zizing!
        help (?)        give detailed help on a specific sub-command
        help-all        display alternative help message
        help-foobar     display alternative help message

    $ python cmdln_help_groups.py help-all
    Usage:
        cmdln_help_groups.py COMMAND [ARGS...]
        cmdln_help_groups.py help [COMMAND]
    <BLANKLINE>
    Options:
        -h, --help  show this help message and exit
    <BLANKLINE>
    Commands:
        bar (barbababa)  whopee!
        fez              pojoing!
        foo              shazam!
        fuz (fuuzbaba)   zizing!
        help (?)         give detailed help on a specific sub-command
        help-all         display alternative help message
        help-foobar      display alternative help message

    $ python cmdln_help_groups.py help-foobar
    Usage:
        cmdln_help_groups.py COMMAND [ARGS...]
        cmdln_help_groups.py help [COMMAND]
    <BLANKLINE>
    Options:
        -h, --help  show this help message and exit
    <BLANKLINE>
    Commands:
        buz             buzzzzz!
        fez             pojoing!
        foo             shazam!
        fuz (fuuzbaba)  zizing!
        help (?)        give detailed help on a specific sub-command
        help-all        display alternative help message
        help-foobar     display alternative help message

"""

import sys
import cmdln

class Shell(cmdln.Cmdln):
    def do_foo(self, argv):
        "shazam!"
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
    retval = shell.main(loop=cmdln.LOOP_NEVER) # don't want a command loop
    sys.exit(retval)
