#!/usr/bin/env python
from __future__ import (absolute_import, division,
                        print_function)

import json

from collections import OrderedDict


def loads(s):
    return json.loads(
        s,
        object_pairs_hook=OrderedDict,
    )


def dumps(o, indent=2):
    return json.dumps(
        o,
        indent=indent,
        sort_keys=True,
        separators=(',', ': '),
    )
