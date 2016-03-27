#!/bin/python

class Episode:

    def __init__(self, source, id, title, timestamp=None):
        self.source = source
        self.id = id
        self.title = title
        self.timestamp = timestamp

    def __str__(self):
        return "[%s]: %s - (%s) [%s]" % (self.source, self.title, self.id, self.timestamp)