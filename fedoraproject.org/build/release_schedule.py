#!/usr/bin/python
# This script will parse the f-19-key-milestones.tjx file and retrieve three relevant
# dates: Alpha Release Public Availability, Beta Release Public Availability and Final Release Public Availability.

import urllib
from StringIO import StringIO
import gzip
from lxml import etree

a = open('build/schedule_alpha.cache', 'w')
b = open('build/schedule_beta.cache', 'w')
g = open('build/schedule_final.cache', 'w')

u = urllib.urlopen('http://fedorapeople.org/groups/schedule/f-19/f-19-key-milestones.tjx')
buf = StringIO(u.read())
f = gzip.GzipFile(fileobj=buf)
data = f.read().strip() # looks like there is a leading space in the file

root = etree.fromstring(data)

alpha_release = root.xpath('//task[@id="f19.TestingPhase.alpha.alpha_drop"]/taskScenario/start/@humanReadable')
beta_release = root.xpath('//task[@id="f19.TestingPhase.beta.beta_drop"]/taskScenario/start/@humanReadable')
final_release = root.xpath('//task[@id="f19.LaunchPhase.final"]/taskScenario/start/@humanReadable')

a.write(alpha_release[0])
a.close
b.write(beta_release[0])
b.close
g.write(final_release[0])
g.close
