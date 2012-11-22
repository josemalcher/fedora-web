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
    'torrent_spins':   'http://torrent.fedoraproject.org/spins',
    'download':        'http://download.fedoraproject.org/pub/fedora/linux/releases',
    'download_spins':  'http://download.fedoraproject.org/pub/alt/releases',
    'mirrors':         'http://mirrors.fedoraproject.org/metalink?path=pub/fedora/linux/releases',
    'checksums':       'https://fedoraproject.org/static/checksums',
    'doc':             'http://docs.fedoraproject.org/en-US/Fedora'
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
    'x86_64_Live_XFCE':    '670',       # In MB
    'i386_Netinstall':     '199',       # In MB
    'x86_64_Netinstall':   '162',       # In MB
    'i686_Live_Security':  '616',       # In MB
    'x86_64_Live_Security':'617',       # In MB
    'i686_Live_Games':     '3.8',       # In GB
    'x86_64_Live_Games':   '3.79',      # In GB
    'i686_Live_Elab':      '1.51',      # In GB
    'x86_64_Live_Elab':    '1.52',      # In GB
    'i686_Live_Soas':      '508',       # In MB
    'x86_64_Live_Soas':    '509',       # In MB
    'i686_Live_Design':    '788',       # In MB
    'x86_64_Live_Design':  '790',       # In MB
    'i686_Live_Sci-kde':   '2.48',      # In GB
    'x86_64_Live_Sci-kde': '2.49',      # In GB
    'i686_Live_Robotics':  '1.29',      # In GB
    'x86_64_Live_Robotics':'1.3',       # In GB
}