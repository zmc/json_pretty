#!/usr/bin/env python
from __future__ import (absolute_import, division,
                        print_function)

import click
import sys

from .ops import dumps, loads


@click.command()
@click.argument(
    'file',
    type=click.Path(
        file_okay=True,
        dir_okay=False,
    ),
    required=True,
    nargs=-1,
)
@click.option(
    '--overwrite', '-o',
    is_flag=True,
    help="Whether to overwrite files, or print to stdout",
)
@click.option(
    '--indent',
    default=2,
    help='Number of spaces to indent',
)
def cli(file, overwrite, indent):
    """
    Prettifies a JSON file, or files, or stdin, by indenting and sorting.

    In lieu of filenames, '-' may be used to represent stdin.
    """
    if file == ('-',):
        prettify(sys.stdin, False, indent)
    else:
        for path in file:
            mode = 'r+' if overwrite else 'r'
            fobj = open(path, mode)
            prettify(fobj, overwrite, indent)


def prettify(fobj, overwrite, indent):
    in_str = fobj.read()
    jobj = loads(in_str)
    if not overwrite:
        sys.stderr.write("// {}:\n".format(fobj.name))
    new_str = dumps(jobj, indent=indent).strip() + '\n'
    if (fobj is sys.stdin) or (overwrite is False):
        sys.stdout.write(new_str)
        sys.stdout.flush()
    else:
        fobj.seek(0)
        fobj.truncate()
        fobj.write(new_str)
