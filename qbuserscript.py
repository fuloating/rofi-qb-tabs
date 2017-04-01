#!/usr/bin/python
# coding=utf-8
import os
import sys
import codecs
import yaml
import time


## Return a formatted timestamp string
def gcm_timestamp(stamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", stamp)


## Wrapper for print() that does not break when redirecting stdin/out
## because of piped output not having a defined encoding. We default
## to UTF-8 encoding in output here.
def gcm_print(smsg):
    if sys.stdout.encoding != None:
        rsmsg = smsg.encode(sys.stdout.encoding)
    else:
        rsmsg = smsg.encode("UTF-8")

    print("{0} | {1}".format(gcm_timestamp(time.localtime()), rsmsg))


## Fatal error handler
def gcm_fatal(smsg):
    gcm_print(u"ERROR: "+ smsg)
    sys.exit(1)


## YAML load helper
def yaml_loader(filepath):
    with open(filepath, "r") as fh:
        data = yaml.load(fh)
    return data


with open(os.environ['QUTE_FIFO'], "w") as f: f.write('session-save tabs\n')
with open(os.environ['QUTE_FIFO'], "w") as f: f.write('session-delete default\n')
time.sleep(0.1)
with open(os.environ['QUTE_FIFO'], "w") as f: f.write('quit\n')


inFilename = os.environ['HOME']+"/.local/share/qutebrowser/sessions/tabs.yml"
outFilename =  os.environ['HOME']+"/scripts/rofi/tabs"

data = yaml_loader(inFilename)

try:
    ofh = open(outFilename, "a")
except:
    gcm_fatal(u"Could not open output file '{0}'.".format(outFilename))

for cwindow in data.get("windows"):
    for ctab in cwindow.get("tabs"):
        for chist in ctab.get("history"):
            if chist.get("active") != None and chist.get("active") == True:
                str = chist.get("title") +"    "+ chist.get("url")
                gcm_print(str)
                ofh.write(str.encode("UTF-8") +"\n")

ofh.close()
