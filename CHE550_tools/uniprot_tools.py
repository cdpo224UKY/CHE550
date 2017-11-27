#!/usr/bin/python3
"""
This module contains a number of functions and classes to deal with retrieving from and interacting with the UniProt
(SwissProt) knowledgebase.
"""


def entry_retrieve_from_uniprot(format, accession):
    """
    Method for retrieving data from the UniProt database.

    :param format: file format for data to be retrieved in
    :type format: str
    :param accession: UniProt accession number
    :type accession: str

    :returns:
        * *entries_str* (str) --
            string of the data retrieved from UniProt
        * *request_datetime* (str) --
            string of the date and time when UniProt was queried
    """
    from urllib import request, error
    from datetime import datetime

    # determining the time of request (used for naming purposes)
    request_datetime = str(datetime.now()).replace(' ', '_').replace('.', '_')

    # creation of query string
    query_str = "http://www.uniprot.org/uniprot/?query="
    query_str += accession
    query_str += '&format=' + format

    # request API
    try:
        with request.urlopen(query_str) as request:
            entries_str = request.read().decode('utf-8')  # the retrieved data must be formatted into utf-8

    except error.HTTPError as err:
        print(err)
        return None, None

    return entries_str, request_datetime


def batch_retrieve_from_uniprot(format, **kwargs):
    """
    Method for retrieving data from the UniProt database.

    :param format: file format for data to be retrieved in
    :type format: str
    :param **kwargs:
        See below
    :keyword Arguments:
        * *keyword* (int) --
            UniProt keyword identifier
        * *reviewed* (str) --
            limits query to SwissProt
        * *go_id* (int) --
            limits query to a specific Gene Ontology (GO) term

    :returns:
        * *entries_str* (str) --
            string of the data retrieved from UniProt
        * *request_datetime* (str) --
            string of the date and time when UniProt was queried
    """
    from urllib import request, error
    from datetime import datetime

    # determining the time of request (used for naming purposes)
    request_datetime = str(datetime.now()).replace(' ', '_').replace('.', '_')

    # creation of query string
    query_str = "http://www.uniprot.org/uniprot/?query="

    for key in kwargs:

        if len(query_str) > 38:
            query_str += '+AND+'

        if type(kwargs[key]) is list:
            for item in kwargs[key]:
                query_str += key + ':' + item

        else:
            query_str += key + ':' + kwargs[key]

    query_str += '&format=' + format

    print(query_str)

    # request API
    try:
        with request.urlopen(query_str) as request:
            entries_str = request.read().decode('utf-8')  # the retrieved data must be formatted into utf-8

    except error.HTTPError as err:
        print(err)
        return None, None

    return entries_str, request_datetime


def uniprot_fasta_parser(entries_str):

    fasta_list = list()
    start_index = 0

    while entries_str.find('>sp|', start_index) != -1:
        end_index = entries_str.find('>sp|', start_index + 1)
        fasta_list.append(entries_str[start_index: end_index])
        start_index = end_index

    return fasta_list


def uniprot_txt_parser(entries_str):
    """

    :param entries_str:
    :return:
    """
    entry_list = list()
    start_index = 0
    while entries_str.find('//\nID   ', start_index) != -1:
        end_index = entries_str.find('//\nID   ', start_index + 1)

        entry_list.append(entries_str[start_index: end_index])

        start_index = end_index

    return entry_list
