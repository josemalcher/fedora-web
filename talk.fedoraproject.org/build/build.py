#!/usr/bin/python
'''
build.py - A script to generate static, translated HTML pages from Genshi
templates/PO files.

Some code/design taken from python.org's website build script
(https://svn.python.org/www/trunk/beta.python.org/build/new-build/)
'''

import os, sys, timing, re, shutil

from optparse import OptionParser

from gettext import GNUTranslations

from genshi.filters import Translator
from genshi.template import TemplateLoader

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
    print 'Website build time: %s' % timing.milli()

def process_dir(dirpath, filenames):
    '''
    Process a directory
    '''
    translations = GNUTranslations(open(os.path.join(options.podir, options.lang + '.mo')))
    loader = TemplateLoader(['.'], callback=lambda template: template.filters.insert(0, Translator(translations.ugettext)))
    for fn in filenames:
        if fn.endswith('~') or fn.endswith('.swp'):
            continue
        src_file = os.path.join(dirpath, fn)
        dest_file = os.path.join(options.output, src_file[len(options.input):]) + '.' + options.lang # Hideous
        curpage = src_file[len(options.input):].rstrip('.html')
        if not os.path.exists(os.path.dirname(dest_file)):
            os.makedirs(os.path.dirname(dest_file))
        template = loader.load(src_file)
        # Variables made availble to all templates
        page = template.generate(
            _=lambda text: translations.ugettext(text),
            lang=options.lang,
            path=options.basepath,
            curpage=curpage,
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
    base_path = os.path.dirname(os.path.abspath(__file__))
    (options, args) = parser.parse_args()
    options.basepath = options.basepath.rstrip('/')
    options.input = options.input.rstrip('/') + '/'
    options.output = options.output.rstrip('/') + '/'
    process(args)

if __name__ == "__main__":
    main()
