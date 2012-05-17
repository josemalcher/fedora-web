#!/usr/bin/python
# This file defines all variable needed to be edited during the release cycle (alpha, beta...).
# We still have to edit the following files have the right release date:
# - data/content/index.html
# - static/js/release-counter-ext.js

release={
    'curr_id':     '16',
    'next_id':     '17',
    'curr_name':   'Verne',
    'next_name':   'Beefy Miracle',
    'curr_state':  'Beta'         # either 'Alpha', 'Beta' or '' (i.e empty)
}

path={
    'torrent':         'http://torrent.fedoraproject.org/torrents',
    'download':        'http://download.fedoraproject.org/pub/fedora/linux/releases',
    'download_spins':  'http://download.fedoraproject.org/pub/alt/spins/linux/releases',
    'mirrors':         'http://mirrors.fedoraproject.org/metalink?path=pub/fedora/linux/releases',
    'checksums':       'https://fedoraproject.org/static/checksums'
}

iso_size={
    'x86_64_DVD':          '3.5',       # In GB
    'i386_DVD':            '3.5',       # In GB
    'source_DVD':          '5.9',       # In GB
    'i686_Live_Desktop':   '605',       # In MB
    'x86_64_Live_Desktop': '604',       # In MB, default download from F17
    'i686_Live_KDE':       '697',       # In MB
    'x86_64_Live_KDE':     '696',       # In MB
    'i686_Live_LXDE':      '542',       # In MB
    'x86_64_Live_LXDE':    '541',       # In MB
    'i686_Live_XFCE':      '627',       # In MB
    'x86_64_Live_XFCE':    '625'        # In MB
}
