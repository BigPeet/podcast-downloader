# podcast-downloader

The goal of this project is to regularly scan various podcast sources, e.g. Youtube playlists or Web-Feeds (RSS),
and download the audio files of new episodes. 

podcast-downloader can either be run indefinitely checking the defined sources with a given frequency 
for new content or can be setup as a cron job.

Additionally downloaded episodes may be transfered to different devices through various methods.

## Setup

WIP

## Requirements

see requirements.txt

Initially this project will make heavy use of other python modules and APIs, but I will try to reduce outside dependencies
and limit them to their specific sources. 
There should be no need to install Youtube specific modules, if no Youtube source is scanned.



## Notes

This is just a small personal project I do for fun. I'm aware that there are several other podcast downloaders and managing tools 
that offer more utility than this.
But I plan to do this because I want to A.) learn how to build/maintain a python project and B.) have a tool 
that caters to my very own needs.

So please, do not question the meaningfulness of podcast-downloader. But you are welcome to suggest features or podcast
sources I could add.

## Roadmap

 - Implement a way to scan a Youtube playlist/channel (or single video) for new content and download the audio file.
 - Add ways to transfer the downloaded files to additional devices.
 - Make the process easier to configure
 - Support for RSS / Atom
 - Improve creation and management of sources (currently sources.list has to be edited manually).
 - ...
