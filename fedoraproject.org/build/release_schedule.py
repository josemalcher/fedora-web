#!/usr/bin/python
# This script will parse the f-19-key-milestones.tjx file and retrieve three relevant
# dates: Alpha Release Public Availability, Beta Release Public Availability and Final Release Public Availability.

import urllib
from xml.etree import ElementTree
import gzip
import os

a = open('build/schedule_alpha.cache', 'w')
b = open('build/schedule_beta.cache', 'w')
f = open('build/schedule_final.cache', 'w')

urllib.urlretrieve('http://fedorapeople.org/groups/schedule/f-19/f-19-key-milestones.tjx', 'build/f-19-key-milestones.tjx')
localFile = gzip.open('build/f-19-key-milestones.tjx', 'r')

tree = ElementTree.parse(localFile)
root = tree.getroot()
for elem in tree.iterfind('taskList/task/task/task/task[@id="f19.TestingPhase.alpha.alpha_drop"]/taskScenario/start'):
	alpha_tag = elem.tag
        alpha_attr = elem.attrib

for elem in tree.iterfind('taskList/task/task/task/task[@id="f19.TestingPhase.beta.beta_drop"]/taskScenario/start'):
	beta_tag = elem.tag
        beta_attr = elem.attrib

for elem in tree.iterfind('taskList/task/task/task[@id="f19.LaunchPhase.final"]/taskScenario/start'):
	final_tag = elem.tag
        final_attr = elem.attrib

def sanitize_output(element):
	string = ' '.join('{0}{1}'.format(key, val) for key, val in sorted(element.items()))
	blacklist = ["humanReadable"]
	for i in range(len(blacklist)):
		string = string.replace(blacklist[i],"")
	blacklist = ["-"]
	for i in range(len(blacklist)):
		string = string.replace(blacklist[i]," ")
	return string

alpha = sanitize_output(alpha_attr)
beta = sanitize_output(beta_attr)
final = sanitize_output(final_attr)

output_alpha = """%s""" % (alpha)
output_beta = """%s""" % (beta)
output_final = """%s""" % (final)

a.write(output_alpha)
a.close
b.write(output_beta)
b.close
f.write(output_final)
f.close
