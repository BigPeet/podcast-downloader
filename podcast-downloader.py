#!/usr/bin/python

import argparse
import logging
from sources import sourcelist_parser
from modules.module import Module

class PodcastDownloader():
    def __init__(self, source_list_file):
        self.sources = sourcelist_parser.parse_sources(source_list_file)
        self.loaded_modules = {}

    def check_sources(self):
        for source in self.sources:
            logging.debug(source)
            source_module = self.load_module(source.type)
            episodes = source_module.scan(source)
            filtered_episodes = source_module.filter_episodes(episodes, source)
            source_module.download_episodes(filtered_episodes)

    def load_module(self, source_type):
        if source_type in self.loaded_modules.keys():
            return self.loaded_modules[source_type]
        else:
            module = Module.create_module(source_type)
            self.loaded_modules[source_type] = module
            return module


if __name__ == "__main__":

  parser = argparse.ArgumentParser()

  parser.add_argument("--loop", default=None, help="The frequency the sources will be checked with. \
      If no value is specified, the sources will be checked only once.")
  parser.add_argument("--sources", default="conf/sources.list", help="path to the list of podcast sources")
  parser.add_argument("--loglevel", default="DEBUG", help="the logging level")
  parser.add_argument("--logfile", default=None, help="The logfile the log output will be written into. \
   If no value is specified, the output will be written into stdout.")

  args = parser.parse_args()

  numeric_level = getattr(logging, args.loglevel.upper(), None)
  if not isinstance(numeric_level, int):
      raise ValueError("Invalid log level: %s" % loglevel)
  logging.basicConfig(level=numeric_level, filename=args.logfile, filemode="w",
      format="%(levelname)s:%(asctime)s - %(funcName)s: %(message)s")

  downloader = PodcastDownloader(args.sources)
  downloader.check_sources()


