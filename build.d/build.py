#!/usr/bin/python
# imported from the spins directory.
# TODO: fedorahosted.org use a specific one. Should we merge?

'''
build.py - A script to generate static, translated HTML pages from Genshi
templates/PO files.

Some code/design taken from python.org's website build script
(https://svn.python.org/www/trunk/beta.python.org/build/new-build/)
'''

import os, sys, timing, re, shutil
from pkg_resources import get_distribution
from optparse import OptionParser
from gettext import GNUTranslations
from genshi.filters import Translator
from genshi.template import TemplateLoader
import fileinput

# We import build/rss.py if exists
sys.path.append('build')
try:
		from rss import *
except ImportError:
		feedparse = None
		pass

# Import of build/release_schedule.py
os.system("../fedoraproject.org/build/release_schedule.py")

try:
    import globalvar
except ImportError:
    print "globalvar.py is missing. It is needed as it provides release specific variables"
    raise

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
    if options.input is not None:
        timing.start()
        for dirpath, dirnames, filenames in os.walk(options.input):
            try:
                process_dir(dirpath, filenames)
            except:
                if options.keepgoing:
                    print 'Error!'
                else:
                    raise
        timing.finish()
        if not options.rss:
            print 'Website build time: %s' % timing.milli()

def process_dir(dirpath, filenames):
    '''
    Process a directory
    '''
    if options.podir and options.lang:
        translations = GNUTranslations(open(os.path.join(options.podir, options.lang + '.mo')))
        if int(get_distribution('genshi').version[2]) < 6:
            loader = TemplateLoader(['.'], callback=lambda template: template.filters.insert(0, Translator(translations.ugettext)))
        else:
            loader = TemplateLoader(['.'], callback=lambda template: template.filters.insert(0, Translator(translations)))
    for fn in filenames:
        if fn.endswith('~') or fn.endswith('.swp'):
            continue
        src_file = os.path.join(dirpath, fn)
        if options.rss:
            sys.setrecursionlimit(1500)
            for line in fileinput.input(src_file):
                if line.find('feedparse')>0:
                    match = re.split('^.*feedparse\(\'', line)
                    feedurl = re.split('\'\)', match[1])
                    feedparse(feedurl[0])
            continue;
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
            _=lambda text: translations.ugettext(text),
            feedparse=feedparse,
            lang=options.lang,
            relpath=relpath,
            path=options.basepath,
            curpage=curpage,
            global_variables=globalvar,
            ).render(method='html', doctype='html', encoding='utf-8')
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
    parser.add_option('-r', '--rss-cache',
        action='store_true', dest='rss', default=False,
        help='Cache RSS feeds')
    base_path = os.path.dirname(os.path.abspath(__file__))
    (options, args) = parser.parse_args()
    options.basepath = options.basepath.rstrip('/')
    if options.input is not None:
        options.input = options.input.rstrip('/') + '/'
    if options.output is not None:
        options.output = options.output.rstrip('/') + '/'
    process(args)

if __name__ == "__main__":
    main()
