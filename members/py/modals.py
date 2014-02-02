#!C:\Anaconda\python.exe
# coding=utf-8

# calling: python merge_pig.py <pig_directory> <output_merged>
# in: <pig_directory> / [part-r-00000] [part-r-00001] [...]
# out: <output_merged>

import time
import sys
import os
import glob
import itertools

# PROCESS COMMAND LINE ARGUMENTS

for i, word in enumerate(sys.argv):
    if word[0:2] == './':
        sys.argv[i] = os.getcwd() + word[1:]

member_profile_directory = sys.argv[1]

member_links_f = open(sys.argv[2],'wb')
member_modals_f = open(sys.argv[3],'wb')

p = '          '
m = '        '

member_links_f.write('\n')

print "LOG FILE [{:s}]".format(os.path.basename(sys.argv[0]))
print ""
print "processing member profiles:"
print ""

# PROCESS MEMBER PROFILE FILES

a = time.time()

member_list_g = glob.iglob(os.path.join(member_profile_directory,'*.txt'))
member_list = list(member_list_g)
member_list.sort()

i = 0
for member in member_list:
    
    with open(member,'rb') as member_f:
        
        name = member_f.readline().strip() # os.path.basename(member).split('.',1)[0]
        department = member_f.readline().strip()
        profile = member_f.readline().strip()
        
        member_links_f.write('' \
        + p + '<p align="justify"><a type="button" href="#modal' + str(i) + '" data-toggle="modal">' + name + '</a> (' + department + ')</p>\n' \
        )
        
        member_modals_f.write(m + '\n' \
        + m + '<div id="modal' + str(i) + '" class="modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n' \
        + m + '  <div class="modal-dialog">\n' \
        + m + '    <div class="modal-content">\n' \
        + m + '    <image src="./pictures/' + name + '.jpg" class="left-image hidden-xs"></image>\n' \
        + m + '      <div class="modal-header">\n' \
        + m + '        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>\n' \
        + m + '        <h4 class="modal-title">' + name + '</h4>\n' \
        + m + '      </div>\n' \
        + m + '      <div class="modal-body">\n' \
        + m + '        <p class="no-margined" align="justify">' + profile + '</p>\n' \
        + m + '      </div>\n' \
        + m + '    </div>\n' \
        + m + '  </div>\n' \
        + m + '</div>\n' \
        )
        
        print '  ' + os.path.basename(member).split('.',1)[0]
        
        i = i + 1

b = time.time()

member_links_f.close()
member_modals_f.close()

# OUTPUT RUNTIME STATISTICS TO LOG FILE

print ""
print "time = {:.10f}".format(b - a)