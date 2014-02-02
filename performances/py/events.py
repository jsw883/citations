#!C:\Anaconda\python.exe
# coding=utf-8

# calling: python merge_pig.py <pig_directory> <output_merged>
# in: <pig_directory> / [part-r-00000] [part-r-00001] [...]
# out: <output_merged>

import time as time_mod
import sys
import os
import glob
import itertools
import urllib

from datetime import datetime
from dateutil.parser import parse

# PROCESS COMMAND LINE ARGUMENTS

for i, word in enumerate(sys.argv):
    if word[0:2] == './':
        sys.argv[i] = os.getcwd() + word[1:]

events_directory = sys.argv[1]

events_f = open(sys.argv[2],'wb')

e = '          '

events_f.write('\n')

print "LOG FILE [{:s}]".format(os.path.basename(sys.argv[0]))
print ""
print "processing events:"
print ""

# PROCESS MEMBER PROFILE FILES

a = time_mod.time()

events_list_g = glob.iglob(os.path.join(events_directory,'*.txt'))
events_list = list(events_list_g)
events_list.sort()

i = 0
for event in events_list:
    
    with open(event,'rb') as event_f:
        
        name = event_f.readline().strip() # os.path.basename(member).split('.',1)[0]
        start = event_f.readline().strip()
        end = event_f.readline().strip()
        location = event_f.readline().strip()
        text = event_f.readline().strip()
        
        t1 = parse(start)
        t2 = parse(end)
        
        iso_start_end = datetime.strftime(t1,'%Y%m%dT%H%M%S') + '/' + datetime.strftime(t2,'%Y%m%dT%H%M%S')
        
        month = datetime.strftime(t1,'%b')
        day = datetime.strftime(t1,'%d')
        if day[0] == '0': day = day[1:]
        
        time = datetime.strftime(t1,'%I:%M %p')
        if time[0] == '0': time = time[1:]
        
        events_f.write(e + '''\n''' \
        + e + '''<div class="divider"></div>\n''' \
        + e + '''\n''' \
        + e + '''<div class="event">\n''' \
        + e + '''  <a href="http://www.google.com/calendar/event?action=TEMPLATE&text=''' + urllib.quote(name.encode('utf-8')) + '''&dates=''' + iso_start_end + '''&details=''' + urllib.quote(text.encode('utf-8')) + '''&location=''' + urllib.quote(location.encode('utf-8')) + '''&trp=false&sprop=The%20Citations%20%40%20Yale%20Graduate%20School&sprop=name:www.yale.edu%2Fcitations" target="_blank">\n''' \
        + e + '''  <div class="event-pill hidden-xs">\n''' \
        + e + '''    <div class="month">''' + month + '''</div>\n''' \
        + e + '''    <div class="day">''' + day + '''</div>\n''' \
        + e + '''    <div class="divider"></div>\n''' \
        + e + '''    <div class="time">''' + time + '''</div>\n''' \
        + e + '''  </div>\n''' \
        + e + '''  <div class="event-row visible-xs">\n''' \
        + e + '''    <p class="name"><b>''' + name + '''</b></p>\n''' \
        + e + '''    <div class="inner">\n''' \
        + e + '''      <span class="month">''' + month + '''</span>\n''' \
        + e + '''      <span class="day">''' + day + '''</span>\n''' \
        + e + '''      <span class="divider"></span>\n''' \
        + e + '''      <span class="time">''' + time + '''</span>\n''' \
        + e + '''    </div>\n''' \
        + e + '''  </div>\n''' \
        + e + '''  </a>\n''' \
        + e + '''  <div class="event-body">\n''' \
        + e + '''    <p class="event-name hidden-xs" align="justify"><b>''' + name + '''</b></p>\n''' \
        + e + '''    <p class="event-text" align="justify">''' + text + '''</p>\n''' \
        + e + '''  </div>\n''' \
        + e + '''</div>\n''' \
        )
        
        print '  ' + os.path.basename(event).split('.',1)[0]
        
        i = i + 1

b = time_mod.time()

events_f.close()

# OUTPUT RUNTIME STATISTICS TO LOG FILE

print ""
print "time = {:.10f}".format(b - a)