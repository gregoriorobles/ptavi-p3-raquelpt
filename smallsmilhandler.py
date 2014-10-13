#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class smallsmilHandler(ContentHandler):

    def __init__(self):
        self.root_layout = {}
        self.region = {}
        self.img = {}
        self.audio = {}
        self.textstream = {}
        self.Lista = []

    def startElement(self, name, attrs):

        if name == 'root-layout':
            self.root_layout['width'] = str(attrs.get('width', ""))
            self.root_layout['height'] = str(attrs.get('height', ""))
            self.root_layout['background-color'] =\
                str(attrs.get('background-color', ""))
            self.Lista.append([name, self.root_layout])
        elif name == 'region':
            self.region['id'] = str(attrs.get('id', ""))
            self.region['top'] = str(attrs.get('top', ""))
            self.region['left'] = str(attrs.get('left', ""))
            self.region['right'] = str(attrs.get('right', ""))
            self.Lista.append([name, self.region])
        elif name == 'img':
            self.img['src'] = str(attrs.get('src', ""))
            self.img['region'] = str(attrs.get('region', ""))
            self.img['begin'] = str(attrs.get('begin', ""))
            self.img['dur'] = str(attrs.get('dur', ""))
            self.Lista.append([name, self.img])
        elif name == 'audio':
            self.audio['src'] = str(attrs.get('src', ""))
            self.audio['begin'] = str(attrs.get('begin', ""))
            self.audio['dur'] = str(attrs.get('dur', ""))
            self.Lista.append([name, self.audio])
        elif name == 'textstream':
            self.textstream['src'] = str(attrs.get('src', ""))
            self.textstream['region'] = str(attrs.get('region', ""))
            self.Lista.append([name, self.textstream])

    def get_tags(self):
        return self.Listae
