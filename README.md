# json_pretty

What's json_pretty?
-------------------
A pretty-printer for JSON files!

This tool was created to help keep diffs against JSON files as readable as possible. Hence, its focus is on rewriting files in place using sane indentation and sorting.


```
$ json-pretty --help
Usage: json-pretty [OPTIONS] FILE...

  Prettifies a JSON file, or files, or stdin, by indenting and sorting.

  In lieu of filenames, '-' may be used to represent stdin.

Options:
  -o, --overwrite   Whether to overwrite files, or print to stdout
  --indent INTEGER  Number of spaces to indent
  --help            Show this message and exit.
```

Installing
----------
It'll be on PyPI soon, but in the meantime you may:
```
pip install git+https://github.com/zmc/json_pretty.git@master#egg=json_pretty
```

Examples
--------
TODO

Links
-----
TODO
