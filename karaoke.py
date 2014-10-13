Enter file contents here#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import smallsmilhandler
import os



class KaraokeLocal():

    def __init__(self, fichero):
        parser = make_parser()
        cHandler = smallsmilhandler.smallsmilHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fich))
        self.list_tags = cHandler.get_tags()

    def do_local(self):
        for Elemento in self.list_tags:
            for Atributo in Elemento:
                if Atributo != 'etiqueta':
                    if Atributo == 'scr':
                        os.system("wget -q " + Elemento[Atributo])
                        Elemento[Atributo] = Elemento[Atributo].split('/')[-1]

    
        

if __name__ == "__main__":
    try:
        fich = sys.argv[1]
        karaoke = KaraokeLocal(fich)
        
        karaoke.do_local()
    
    except IndexError:
        print "Usage: python karaoke.py src_file.smil!"
