#!/usr/bin/python
# vim: set ts=4 sw=4 et
'''
build.py - A script to generate static, translated HTML pages from Genshi
templates/PO files.

Some code/design taken from python.org's website build script
(https://svn.python.org/www/trunk/beta.python.org/build/new-build/)
'''

import os
import sys
import timing
import re
import shutil
import csv
import iniparse
import urlparse
import operator
import locale

from optparse import OptionParser

from gettext import GNUTranslations

from genshi.filters import Translator
from genshi.template import TemplateLoader

from genshi.core import Markup

from pkg_resources import get_distribution 

locale.setlocale(locale.LC_COLLATE, 'en_US')

vcsloc = {
  'hg': '/srv/hg',
  'bzr': '/srv/bzr',
  'git': '/srv/git',
  'mtn': '/srv/mtn',
  'svn': '/srv/svn'
}

def process(args):
    if os.path.exists(options.output) and options.erase:
        shutil.rmtree(options.output)
    if not os.path.exists(options.output):
        os.makedirs(options.output)
    if options.static is not None:
        static = options.static.split(',');
        for dir in static:
            outpath = os.path.join(options.output, dir)
            if os.path.exists(outpath):
                shutil.rmtree(outpath)
            copytree(dir, outpath)
    if options.trac and os.path.isdir(options.trac):
        # If we are building VCS-only projects along with Trac projects, join
        if options.vcs:
            projects = read_vcs(options.vcs)
            prjs = read_trac(options.trac)
            if prjs:
                for id,prj in prjs.items():
                    # Overwrite with trac data if there's any
                    projects[id] = prj
        else:
            projects = read_trac(options.trac)
    else:
        if options.data:
            projects = read_data(options.data)
        else:
            projects = {}
    projects.keys().sort()
    timing.start()
    for dirpath, dirnames, filenames in os.walk(options.input):
        try:
            process_dir(dirpath, filenames, projects)
        except:
            if options.keepgoing:
                print 'Error!'
            else:
                raise
    timing.finish()
    print 'Website build time: %s' % timing.milli()

def read_vcs(vcslist):
    projects = {}
    for vcs in vcslist:
        if not vcs in vcsloc.keys():
            continue
        vcspath = vcsloc[vcs]
        if os.path.isdir(vcspath):
            for item in os.listdir(vcspath):
                if (os.path.isdir(os.path.join(vcspath, item))# Dirs
                    and not os.path.islink(os.path.join(vcspath, item))# No links
                    and not item.endswith('.old')):#Ugly, I know, any better idea?
                    project = {
                        'group': item[0].upper(),
                        'url': 'http://%(vcs)s.fedorahosted.org/%(vcs)s/%(project)s' % {'vcs': vcs, 'project': item},
                        'desc': 'Project %(project)s under %(vcs)s' % {'project': item.split('.')[0], 'vcs': vcs},
                        'title': item.split('.')[0],
                        'vcs': vcs,
                        'vcsbase': item
                    }
                    projects[item.split('.')[0]] = project
    return projects

def read_data(filename):
    projects = {}
    for line in csv.reader(open(filename, 'r')):
        if not line[0].startswith('#'):
            project = {
                'group': line[0][0].upper(),
                'url': 'https://fedorahosted.org/%s/' % (line[0]),
                'desc': line[1].decode('utf-8'),
                'title': line[1].decode('utf-8')
            }
            if len(line) > 2:
                project['vcs'] = line[2]
                project['vcsbase'] = ''
                project['vcsweburl'] = 'https://fedorahosted.org/%s/browser/' % (line[0])
            projects[line[0]] = project
    return projects

def read_trac(path):
    projects = {}
    for dir in os.listdir(path):
        filename = os.path.join(path, dir, 'conf', 'trac.ini')
        if os.path.isfile(filename):
            print filename
            conf = iniparse.INIConfig(file(filename, 'r'))
            base_url = 'https://fedorahosted.org/%s' % dir
            if 'base_url' in conf['trac'] and conf['trac']['base_url']:
                base_url = conf['trac']['base_url']
            descr = ''
            if 'descr' in conf['project']:
                descr = conf['project']['descr']

            project = {
                'group': base_url.rstrip('/').split('/')[-1][0].upper(),
                'url': base_url,
                'desc': conf['project']['name'].decode('utf-8'),
                'title': descr.decode('utf-8')
            }
            if 'repository_type' in conf['trac']:
                project['vcs'] = conf['trac']['repository_type']
                # What happens if this is a trac-only project?
                if 'repository_dir' in conf['trac'] and conf['trac']['repository_dir']:
                    project['vcsbase'] = os.path.realpath(
                            conf['trac']['repository_dir']).replace('/srv/%s/' % project['vcs'], '', 1)
                else:
                    project['vcsbase'] = ''
                project['vcsweburl'] = urlparse.urljoin(
                    base_url.rstrip('/') + '/', 'browser')
            projects[base_url.rstrip('/').split('/')[-1]] = project
    return projects

def process_dir(dirpath, filenames, projects):
    '''
    Process a directory
    '''
    translations = GNUTranslations(open(os.path.join(options.podir, options.lang + '.mo')))
    if int(get_distribution('genshi').version[2]) < 6:
       loader = TemplateLoader(['.'], callback=lambda template: template.filters.insert(0, Translator(translations.ugettext)))
    else:
       loader = TemplateLoader(['.'], callback=lambda template: template.filters.insert(0, Translator(translations)))
    for fn in filenames:
        if fn.endswith('~') or fn.endswith('.swp'):
            continue
        src_file = os.path.join(dirpath, fn)
        dest_file = os.path.join(options.output, src_file[len(options.input):]) + '.' + options.lang # Hideous
        curpage = src_file[len(options.input):].rstrip('.html')
        relpath = '../' * (dest_file.count('/') - 1)
        relpath = relpath.rstrip('/')
        if relpath == '': relpath = '.'
        if not os.path.exists(os.path.dirname(dest_file)):
            os.makedirs(os.path.dirname(dest_file))
        template = loader.load(src_file)
        # Variables made availble to all templates
        page = template.generate(
            _=lambda text: Markup(translations.ugettext(text)),
            lang=options.lang,
            path=options.basepath,
            relpath=relpath,
            curpage=curpage,
            projects=projects
            ).render(method='html', doctype='html')
        output = open(dest_file, 'w')
        output.write(page)
        output.close()

def copytree(src, dest):
    '''
    Recursively copy a directory, skipping .git directories.
    '''
    os.makedirs(dest)
    ls = os.listdir(src)
    for name in ls:
        if name == '.git':
            continue
        orig = os.path.join(src, name)
        new = os.path.join(dest, name)
        if os.path.isdir(orig):
            copytree(orig, new)
        else:
            shutil.copy(orig, new)

def main():
    global options
    parser = OptionParser()
    parser.add_option('-p', '--podir', dest='podir',
        help='Directory containing PO files', metavar='PODIR')
    parser.add_option('-l', '--lang', dest='lang',
        help='Language to generate', metavar='LANG')
    parser.add_option('-i', '--input', dest='input',
        help='Input directory', metavar='INPUT')
    parser.add_option('-o', '--output', dest='output',
        help='Directory to output to', metavar='OUTPUT')
    parser.add_option('-s', '--static', dest='static',
        help='Comma separated static directories to copy', metavar='STATIC')
    parser.add_option('-b', '--base', dest='basepath',
        help='Base website path', metavar='BASEPATH')
    parser.add_option('-k', '--keepgoing',
        action='store_true', dest='keepgoing', default=False,
        help='keep going past errors if possible')
    parser.add_option('-e', '--erase',
        action='store_true', dest='erase', default=False,
        help='Erase any existing output directory first')
    parser.add_option('-d', '--data', dest='data', default=None,
        help='Filename to read project data from')
    parser.add_option('-t', '--trac', dest='trac', default=None,
        help='Path to read Trac project data from under')
    parser.add_option('-c', '--vcs', dest='vcs', action='append',
        help='Append these version control systems')
    base_path = os.path.dirname(os.path.abspath(__file__))
    (options, args) = parser.parse_args()
    options.basepath = options.basepath.rstrip('/')
    options.input = options.input.rstrip('/') + '/'
    options.output = options.output.rstrip('/') + '/'
    process(args)

if __name__ == "__main__":
    main()
