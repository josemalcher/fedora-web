#!/usr/bin/python

# Hideous hack to fix docs links.
# Please remove this as soon as it's possible.

import sys
import glob
import subprocess

default_language = 'en-US'

old_urls = [
'http://docs.fedoraproject.org/installation-quick-start-guide/',
'http://docs.fedoraproject.org/install-guide/',
'http://docs.fedoraproject.org/install-guide/f13/',
'http://docs.fedoraproject.org/install-guide/f13/en-US/html/ch-new-users.html#sn-making-media',
'http://docs.fedoraproject.org/install-guide/f13/en-US/html/ch-new-users.html#sn-which-arch',
'http://docs.fedoraproject.org/install-guide/f13/en-US/html/ch-upgrade-x86.html',
'http://docs.fedoraproject.org/readme-burning-isos/en_US/sn-validating-files.html',
'http://docs.fedoraproject.org/release-notes/',
'http://docs.fedoraproject.org/release-notes/f13/',
]

new_urls = [
'http://docs.fedoraproject.org/%s/Fedora/14/html/Installation_Quick_Start_Guide/index.html',
'http://docs.fedoraproject.org/%s/Fedora/14/html/Installation_Guide/index.html',
'http://docs.fedoraproject.org/%s/Fedora/14/html/Installation_Guide/index.html',
'http://docs.fedoraproject.org/%s/Fedora/14/html/Installation_Guide/sn-making-media.html',
'http://docs.fedoraproject.org/%s/Fedora/14/html/Installation_Guide/ch-new-users.html#sn-which-arch',
'http://docs.fedoraproject.org/%s/Fedora/14/html/Installation_Guide/ch-upgrade-x86.html',
'http://docs.fedoraproject.org/%s/Fedora/14/html/Burning_ISO_images_to_disc/sect-Burning_ISO_images_to_disc-Validating_the_Files.html',
'http://docs.fedoraproject.org/%s/Fedora/14/html/Release_Notes/index.html',
'http://docs.fedoraproject.org/%s/Fedora/14/html/Release_Notes/index.html',
]

avail_langs = {
'Installation_Guide': [ 'en-US' ],
'Burning_ISO_images_to_disc': [ 'en-US', 'zh-CN', 'cs-CZ', 'nl-NL', 'fi-FI', 'fr-FR', 'id-ID', 'pl-PL', 'pt-PT', 'ru-RU', 'sr-RS', 'sr-Latn-RS', 'sv-SE', 'uk-UA', 'de-DE' ],
'Installation_Quick_Start_Guide': [ 'en-US', 'zh-CN', 'cs-CZ', 'nl-NL', 'fr-FR', 'pl-PL', 'pt-PT', 'ru-RU', 'es-ES', 'sv-SE', 'uk-UA' ],
'Release_Notes': [ 'en-US', 'cs-CZ', 'nl-NL', 'fr-FR', 'it-IT', 'ja-JP', 'pl-PL', 'pt-PT', 'ru-RU', 'es-ES', 'sv-SE', 'uk-UA', 'zh-CN', 'he-IL' ],
}

language_map = {
'cs': 'cs-CZ',
'de': 'de-DE',
'en': 'en-US',
'es': 'es-ES',
'fi': 'fi-FI',
'fr': 'fr-FR',
'he': 'he-IL',
'id': 'id-ID',
'it': 'it-IT',
'ja': 'ja-JP',
'nl': 'nl-NL',
'pl': 'pl-PL',
'pt': 'pt-PT',
'ru': 'ru-RU',
'sr': 'sr-RS',
'sv': 'sv-SE',
'uk': 'uk-UA',
'zh_CN': 'zh-CN',
}

url_map = dict(zip(old_urls, new_urls))

def get_doc(url):
    return url.split('/')[7]

def main():
    if len(sys.argv) < 2:
        print 'Usage: %s [language]' % sys.argv[0]
        sys.exit(1)

    language = sys.argv[1]
    language_code = language_map.get(language, default_language)

    command_line = [ '/bin/sed', '-i' ]

    for old, new in url_map.iteritems():
        doc = get_doc(new)
        new_url = ''
        if language_code not in avail_langs[doc]:
            new_url = new % default_language
        else:
            new_url = new % language_code
        regex = 's@"%s"@"%s"@g' % (old, new_url)
        command_line += [ '-e', regex ]

    html_files = glob.glob('out/*.html.%s' % language)
    if not html_files:
        print 'No files, doing nothing.'
        sys.exit(0)

    command_line += html_files

    rc = subprocess.call(command_line)
    if rc != 0:
        print 'WARNING: command failed!'

    sys.exit(rc)

if __name__== '__main__':
    main()
