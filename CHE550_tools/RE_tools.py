#!/usr/bin/python3
from urllib import request, error
from datetime import datetime

standard_abbreviation = {
    'R': ['G', 'A'],
    'Y': ['C', 'T'],
    'M': ['A', 'C'],
    'K': ['G', 'T'],
    'S': ['G', 'C'],
    'W': ['A', 'T'],
    'B': ['C', 'G', 'T'],
    'D': ['A', 'G', 'T'],
    'H': ['A', 'C', 'T'],
    'V': ['A', 'C', 'G'],
    'N': ['A', 'C', 'G', 'T']
}


def retrieve_restriction_enzymes():
    """

    :return:
    """
    request_datetime = str(datetime.now()).replace(' ', '_').replace('.', '_')
    try:
        with request.urlopen("ftp://ftp.neb.com/pub/rebase/allenz.txt") as req:
            entries_str = req.read().decode('utf-8')  # the retrieved data must be formatted into utf-8

    except error.HTTPError as err:
        print(err)
        return None, None

    return entries_str, request_datetime

def parse_REBASE(REBASE_path):
    """

    :param REBASE_path:
    :return:
    """
    REZs = dict()
    enzyme = str()

    with open(REBASE_path, 'r') as f:
        for line in f:
            if '<1>' in line:
                pass
            elif '<5>' in line:
                pass
    pass
