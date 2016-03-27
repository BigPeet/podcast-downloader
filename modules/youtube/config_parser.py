#!/bin/python
import logging

def parse_config(config_file_path):
    config = {}
    with open(config_file_path, "r") as config_file:
        lines = config_file.readlines()
        for line in lines:
            if line.startswith("#") or line.startswith("//"):
                continue
            tokens = line.split("=")
            assert(len(tokens) == 2)
            logging.debug("KEY=%s \t VALUE=%s" % (tokens[0].strip(), tokens[1].strip()))
            config[tokens[0].strip()] = tokens[1].strip()
    return config
