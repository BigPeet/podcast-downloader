#!/bin/python


from abc import ABCMeta, abstractmethod

class Downloader(object):
    __metaclass__  = ABCMeta

    @abstractmethod
    def download(self, episode):
        pass
