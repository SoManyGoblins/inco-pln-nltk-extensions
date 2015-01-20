# coding=utf-8
import json

from inco.pln.parse.maltparser import MaltParser

__author__ = 'Matias'

import inco.pln.tag.treetagger
import inco.pln.tag.freeling
import inco.pln.parse.freeling

tagger_tt = inco.pln.tag.treetagger.TreeTagger(
    "C:\\Users\\Matias\\Downloads\\tree-tagger-windows-3.2\\TreeTagger\\bin\\tag-spanish.bat")
tagger_fl = inco.pln.tag.freeling.FreeLing(
    "C:\\Users\\Matias\\Downloads\\freeling-3.1-win\\freeling-3.1-win\\bin\\analyzer.exe")

tokens = [u"En", u"el", u"tramo", u"de", u"Telefónica", u"un", u"toro", u"descolgado", u"ha", u"creado", u"peligro",
          u"tras", u"embestir", u"contra", u"un", u"grupo", u"de", u"mozos", u"."]

full = tagger_fl.tag_full(tokens)

string = json.dumps(full)

parser_mp = MaltParser("C:\\Users\\Matias\\Downloads\\maltparser-1.8\\maltparser-1.8\\maltparser-1.8.jar",
                       "C:\\Users\\Matias\\Downloads\\maltparser-1.8\\maltparser-1.8\\ModeloESP\\espmalt-1.0.mco")
parser_fl = inco.pln.parse.freeling.FreeLing(
    "C:\\Users\\Matias\\Downloads\\freeling-3.1-win\\freeling-3.1-win\\bin\\analyzer.exe")


# print "--------- PARSE MALTPARSER ----------"
# print parser_mp.parse(string)
# print "--------- PARSE FREELING ----------"
# print parser_fl.parse(string)