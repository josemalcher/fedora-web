#!/bin/env python

import ConfigParser

'''
This script takes the contents of the website-specific LINGUAS file, constructs an options menu for the languages contained therein.
'''

language_map = ConfigParser.ConfigParser().readfp('translations.ini')

with open(sys.argv[1], r) as linguas: # Linguas is where available languages are stored
    with open(sys.argv[2], w) as output: # Output is a genshi template
        output.write('''
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml"
              xmlns:py="http://genshi.edgewall.org/"
              xmlns:xi="http://www.w3.org/2001/XInclude"
              py:strip="">
              ''')
        try:
            for lang in linguas:
                lang = lang.strip()
                if lang and not lang.startswith('#'):
                    output.write('    <option value="' + lang + '" py:attrs="{\'selected\': lang == \'' + lang + '\' and \'selected\' or None}">' + language_map.get(lang) + '</option>')
        finally:
            f.close()
        output.write('''</html>
''')

