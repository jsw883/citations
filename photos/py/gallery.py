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

gallery_directory = sys.argv[1]

gallery_f = open(sys.argv[2],'wb')

g = '        '
s = '    '

gallery_f.write('\n')

print "LOG FILE [{:s}]".format(os.path.basename(sys.argv[0]))
print ""
print "processing galleries:"
print ""

# PROCESS MEMBER PROFILE FILES

a = time_mod.time()

gallery_list_g = glob.iglob(os.path.join(gallery_directory,'*'))
gallery_list = list(gallery_list_g)
gallery_list.sort()

for gallery in gallery_list:
    
    gallery_path = os.path.basename(gallery).strip()
    
    with open(gallery + '/details.txt') as details_f:
        
        gallery_name = details_f.readline().strip()
        gallery_text = details_f.readline().strip()
        
        gallery_f.write(g + '''\n'''
        + g + '''<div class="divider"></div>\n''' \
        + g + '''\n''' \
        + g + '''<div class="col-md-12 text-box">\n''' \
        + g + '''  <h4 class="no-top-margined">''' + gallery_name + '''</h4>\n''' \
        + g + '''  <p align="justify" class="no-bot-margined">''' + gallery_text + '''</p>\n''' \
        + g + '''</div>\n''' \
        + g + '''<div class="row">\n''' \
        + g + '''  <div class="col-md-12">\n''' \
        + g + '''    <div id="''' + gallery_name.lower().replace(" ","-") + '''" class="gallery">''' \
        )
        
        print gallery_name + ":"
        print ""
    
    img_list_g = glob.iglob(os.path.join(gallery,'*.jpg*'))
    img_list = list(img_list_g)
    img_list.sort()
    
    with open(gallery + '/captions.txt','rb') as captions_f:
        
        for img in img_list:
            
            img_name = os.path.basename(img)
            caption = captions_f.readline().strip()
            
            gallery_f.write('''<a href="./galleries/''' + gallery_path + '''/''' + img_name + '''" title="''' + caption + '''"><img src="./galleries/''' + gallery_path + '''/thumbnails/''' + img_name + '''" alt="''' + caption + '''"></a>''')
            
            print "  " + os.path.basename(img)
    
    gallery_f.write('''</div>\n''' \
    + g + '''  </div>\n''' \
    + g + '''</div>\n''' \
    )
        
    print ""

gallery_f.write('\n')

for gallery in gallery_list:
    
    with open(gallery + '/details.txt') as details_f:
      
        gallery_name = details_f.readline().strip()
        
        gallery_f.write(s + '''\n''' \
        + s + '''<script>\n''' \
        + s + '''  document.getElementById("''' + gallery_name.lower().replace(" ","-") + '''").onclick = function (event) {\n''' \
        + s + '''    event = event || window.event;\n''' \
        + s + '''    var target = event.target || event.srcElement,\n''' \
        + s + '''      link = target.src ? target.parentNode : target,\n''' \
        + s + '''      options = {index: link, event: event},\n''' \
        + s + '''      links = this.getElementsByTagName('a');\n''' \
        + s + '''    blueimp.Gallery(links, options);\n''' \
        + s + '''  };\n''' \
        + s + '''</script>\n''' \
        )

b = time_mod.time()

gallery_f.close()

# OUTPUT RUNTIME STATISTICS TO LOG FILE

print "time = {:.10f}".format(b - a)