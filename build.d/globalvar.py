#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file defines all variable needed to be edited during the release cycle (alpha, beta...).
release={
    'prev_id':     '18',
    'curr_id':     '19',
    'next_id':     '20',
    'curr_name':   'Schroedinger\'s Cat',
    'next_name':   '',
    'curr_state':  '',             # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_arm_state':  '',         # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_ppc64_state':  '',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_s390_state':  '',        # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_state':  '',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'prev_arm_id': '17',
    'prev_ppc64_id': '17',
    'prev_s390_id': '17',
    'curr_arm_id': '18',
    'curr_ppc64_id': '18',
    'curr_s390_id': '18',
    'curr_cloud_id': '19',
    'next_arm_id': '19',
    'next_ppc64_id': '19',
    'next_s390_id': '19',
    'next_cloud_id': '20',
}

path={
    'torrent':         'http://torrent.fedoraproject.org/torrents',
    'torrent_spins':   'http://torrent.fedoraproject.org/spins',
    'download':        'http://download.fedoraproject.org/pub/fedora/linux/releases',
    'download_spins':  'http://download.fedoraproject.org/pub/alt/releases',
    'download_arch':   'http://download.fedoraproject.org/pub/fedora-secondary/releases',
    'mirrors':         'http://mirrors.fedoraproject.org/metalink?path=pub/fedora/linux/releases',
    'checksums':       'https://fedoraproject.org/static/checksums',
    'doc':             'http://docs.fedoraproject.org/en-US/Fedora'
}

iso_size={
    'x86_64_DVD':          '4.3',       # In GB
    'i386_DVD':            '4.4',       # In GB
    'source_DVD':          '8.8',       # In GB
    'i686_Live_Desktop':   '889',       # In MB
    'x86_64_Live_Desktop': '916',       # In MB, default download from F18
    'i686_Live_KDE':       '805',       # In MB
    'x86_64_Live_KDE':     '831',       # In MB
    'i686_Live_LXDE':      '654',       # In MB
    'x86_64_Live_LXDE':    '682',       # In MB
    'i686_Live_XFCE':      '662',       # In MB
    'x86_64_Live_XFCE':    '691',       # In MB
    'i386_Netinstall':     '327',       # In MB
    'x86_64_Netinstall':   '294',       # In MB
    'i686_Live_Security':  '694',       # In MB
    'x86_64_Live_Security':'724',       # In MB
    'i686_Live_Games':     '3.8',       # In GB
    'x86_64_Live_Games':   '3.79',      # In GB
    'i686_Live_Elab':      '1.9',       # In GB
    'x86_64_Live_Elab':    '1.9',       # In GB
    'i686_Live_Soas':      '546',       # In MB
    'x86_64_Live_Soas':    '576',       # In MB
    'i686_Live_Design':    '928',       # In MB
    'x86_64_Live_Design':  '961',       # In MB
    'i686_Live_Sci-kde':   '2.7',       # In GB
    'x86_64_Live_Sci-kde': '2.7',       # In GB
    'i686_Live_Robotics':  '1.6',       # In GB
    'x86_64_Live_Robotics':'1.6',       # In GB
    'i686_Live_Jam':       '1.4',       # In GB
    'x86_64_Live_Jam':     '1.4',       # In GB
    'i686_Live_Mate':      '1.4',       # In GB
    'x86_64_Live_Mate':    '1.4',       # In GB
    'PPC64_DVD':           '4.2',       # In GB
    'PPC64_Netinstall':    '303',       # In MB
    's390_DVD':            '4.0'        # In GB
}
