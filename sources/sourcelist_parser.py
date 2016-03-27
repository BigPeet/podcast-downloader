#!/usr/bin/python

import os.path
from source import Source
import logging

def parse_sources(list_file):
    sources = []
    logging.debug(list_file)
    if os.path.exists(list_file):
        with open(list_file, "r") as sources_file:
            lines = sources_file.readlines()
            for line in lines:
                logging.debug(line.strip())
                if line.startswith("#") or line.startswith("//") or line.strip() == "":
                    continue
                sources.append(parse_source(line))
    return sources


def parse_source(line):
    logging.debug(line)
    tokens = line.split()
    source_type = tokens[0]
    id = tokens[1]
    return Source(source_type, id)
