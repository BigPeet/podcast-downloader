#!/usr/bin/python

import os.path
from source import Source

def parse_sources(list_file):
    sources = []
    if os.path.exists(list_file):
		with open(list_file, "r") as sources_file:
			lines = sources_file.readlines()
			sources = [parse_source(line) for line in lines]
    
    return sources


def parse_source(line):
	tokens = line.split()
	source_type = tokens[0]
	id = tokens[1]
	return Source(source_type, id)