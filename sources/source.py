#!/usr/bin/python


class SourceType:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __eq__(self, other):
         return (isinstance(other, self.__class__) and self.id == other.id)

    def __ne__(self, other):
         return not self.__eq__(other)

     def __str__(self):
         return self.name

     def __hash__(self):
         return self.id.__hash__()

YOUTUBE_PLAYLIST = SourceType("YOUTUBE_PLAYLIST", 1)


TYPES = {"YOUTUBE_PLAYLIST": YOUTUBE_PLAYLIST,
         "YT_PL": YOUTUBE_PLAYLIST}

class Source:

    def __init__(self, source_type, id):
        self.type = TYPES[str(source_type)]
        self.id = id
        self.last_scanned = None
        self.loaded_episodes_list = None

    def __str__(self):
        return self.type.name + "\t" + str(self.id)

