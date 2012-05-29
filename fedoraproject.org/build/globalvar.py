#!/usr/bin/python
# This file defines all variable needed to be edited during the release cycle (alpha, beta...).
release={
    'prev_id':     '16',
    'curr_id':     '17',
    'next_id':     '18',
    'curr_name':   'Beefy Miracle',
    'next_name':   '',
    'curr_state':  ''         # either 'Alpha', 'Beta' or '' (i.e empty)
}

path={
    'torrent':         'http://torrent.fedoraproject.org/torrents',
    'download':        'http://download.fedoraproject.org/pub/fedora/linux/releases',
    'download_spins':  'http://download.fedoraproject.org/pub/alt/releases',
    'mirrors':         'http://mirrors.fedoraproject.org/metalink?path=pub/fedora/linux/releases',
    'checksums':       'https://fedoraproject.org/static/checksums'
}

iso_size={
    'x86_64_DVD':          '3.6',       # In GB
    'i386_DVD':            '3.6',       # In GB
    'source_DVD':          '6.1',       # In GB
    'i686_Live_Desktop':   '646',       # In MB
    'x86_64_Live_Desktop': '645',       # In MB, default download from F17
    'i686_Live_KDE':       '695',       # In MB
    'x86_64_Live_KDE':     '692',       # In MB
    'i686_Live_LXDE':      '590',       # In MB
    'x86_64_Live_LXDE':    '587',       # In MB
    'i686_Live_XFCE':      '672',       # In MB
    'x86_64_Live_XFCE':    '670'        # In MB
}
