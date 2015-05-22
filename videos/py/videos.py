#!C:\Anaconda\python.exe

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
gallery_directory = sys.argv[1]


videos_f = open(sys.argv[2],'wb')

v = '        '
s = '    '

videos_f.write('\n')

print "LOG FILE [{:s}]".format(os.path.basename(sys.argv[0]))
print ""
print "processing galleries:"
print ""

# PROCESS MEMBER PROFILE FILES

a = time_mod.time()

gallery_list_g = glob.iglob(os.path.join(gallery_directory,'*'))
gallery_list = list(gallery_list_g)
gallery_list.sort(reverse=True)

for gallery in gallery_list:
    
    gallery_path = os.path.basename(gallery).strip()
    
    with open(gallery + '/details.txt') as details_f:
        
        gallery_name = details_f.readline().strip()
        gallery_text = details_f.readline().strip()
        
        videos_f.write(v + '''\n''' \
        + v + '''<div class="col-md-12 text-box">\n''' \
        + v + '''  <h4 class="no-top-margined">''' + gallery_name + '''</h4>\n''' \
        + v + '''  <p align="justify" class="no-bot-margined">''' + gallery_text + '''</p>\n''' \
        + v + '''</div>\n''' \
        + v + '''\n''' \
        + v + '''<div class="row">\n''' \
        + v + '''  <div class="col-md-12">\n''' \
        + v + '''    <div id="''' + gallery_name.lower().replace(" ","-") + '''" class="blueimp-gallery blueimp-gallery-controls blueimp-gallery-carousel">\n''' \
        + v + '''      <div class="slides"></div>\n''' \
        + v + '''      <h3 class="title"></h3>\n''' \
        + v + '''      <a class="prev"><span style="margin-left:-3px;"></span></a>\n''' \
        + v + '''      <a class="next"><span style="margin-left:+3px;"></span></a>\n''' \
        + v + '''      <a class="play-pause"></a>\n''' \
        + v + '''      <ol class="indicator"></ol>\n''' \
        + v + '''    </div>\n''' \
        + v + '''  </div>\n''' \
        + v + '''</div>\n''' \
        )
        
        print "  " + gallery_name

first = True

for gallery in gallery_list:
    
    gallery_path = os.path.basename(gallery).strip()
    
    with open(gallery + '/details.txt') as details_f:
        
        gallery_name = details_f.readline().strip()
    
    videos_f.write(s + '''\n''' \
    + s + '''<script>\n''' \
    + s + '''  blueimp.Gallery(\n''' \
    + s + '''    [''' \
    )
    
    with open(gallery + '/names.txt') as names_f, open(gallery + '/ids.txt') as ids_f:
        
        first = True
        
        for line in names_f:
            
            name = line.strip()
            id = ids_f.readline().strip()
            
            if first:
                first = False
            else:
                videos_f.write(''',\n''' + v)
            
            videos_f.write('''{\n''' \
            + v + '''  title: "''' + name + '''",\n''' \
            + v + '''  href: "http://www.youtube.com/watch?v=''' + id + '''",\n''' \
            + v + '''  type: "text/html",\n''' \
            + v + '''  youtubeid: "''' + id + '''",\n''' \
            + v + '''  poster: "./videos/''' + gallery_path + '''/screenshots/''' + name + '''.jpg"\n''' \
            + v + '''}''' \
            )
    
    videos_f.write('''],\n''' \
    + s + '''    {\n''' \
    + s + '''      container: "#''' + gallery_name.lower().replace(" ","-") + '''",\n''' \
    + s + '''      carousel: true,\n''' \
    + s + '''      \n''' \
    + s + '''      youTubeVideoIdProperty: "youtubeid",\n''' \
    + s + '''      youTubeClickToPlay: false\n''' \
    + s + '''    }\n''' \
    + s + '''  );\n''' \
    + s + '''</script>''' \
    )
    
b = time_mod.time()

videos_f.close()

# OUTPUT RUNTIME STATISTICS TO LOG FILE

print "time = {:.10f}".format(b - a)