#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file defines all variable needed to be edited during the release cycle (alpha, beta...).
release={
    'prev_id':     '18',
    'curr_id':     '19',
    'next_id':     '20',
    'curr_name':   u'Schrödinger’s Cat',
    'next_name':   'Heisenbug',
    'curr_state':  'Beta',             # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_arm_state':  'Beta',         # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_ppc64_state':  '',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_s390_state':  '',        # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_state':  'Beta',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'prev_arm_id': '18',
    'prev_ppc64_id': '18',
    'prev_s390_id': '18',
    'curr_arm_id': '19',
    'curr_ppc64_id': '19',
    'curr_s390_id': '19',
    'curr_cloud_id': '19',
    'next_arm_id': '20',
    'next_ppc64_id': '20',
    'next_s390_id': '20',
    'next_cloud_id': '20',
    'cloud_composedate': '20130627',
    'pre_cloud_composedate': '20130918',
    'RC_gold': '4'                      # insert the number of the RC version declared GOLD
}

path={
    'torrent':         'http://torrent.fedoraproject.org/torrents',
    'torrent_spins':   'http://torrent.fedoraproject.org/torrents',
    'download':        'http://download.fedoraproject.org/pub/fedora/linux/releases',
    'download_spins':  'http://download.fedoraproject.org/pub/alt/releases',
    'download_arch':   'http://download.fedoraproject.org/pub/fedora-secondary/releases',
    'mirrors':         'http://mirrors.fedoraproject.org/metalink?path=pub/fedora/linux/releases',
    'checksums':       'https://fedoraproject.org/static/checksums',
    'doc':             'http://docs.fedoraproject.org/en-US/Fedora'
}

iso_size={
    'x86_64_DVD':          '4.2',       # In GB
    'i386_DVD':            '4.3',       # In GB
    'source_DVD':          '7.5',       # In GB
    'i686_Live_Desktop':   '919',       # In MB
    'x86_64_Live_Desktop': '951',       # In MB, default download from F18
    'i686_Live_KDE':       '843',       # In MB
    'x86_64_Live_KDE':     '878',       # In MB
    'i686_Live_LXDE':      '656',       # In MB
    'x86_64_Live_LXDE':    '691',       # In MB
    'i686_Live_XFCE':      '588',       # In MB
    'x86_64_Live_XFCE':    '621',       # In MB
    'i386_Netinstall':     '353',       # In MB
    'x86_64_Netinstall':   '317',       # In MB
    'i686_Live_Security':  '730',       # In MB
    'x86_64_Live_Security':'764',       # In MB
    'i686_Live_Games':     '3.9',       # In GB
    'x86_64_Live_Games':   '3.9',       # In GB
    'i686_Live_Elab':      '2.0',       # In GB
    'x86_64_Live_Elab':    '2.0',       # In GB
    'i686_Live_Soas':      '599',       # In MB
    'x86_64_Live_Soas':    '634',       # In MB
    'i686_Live_Design':    '1.3',       # In GB
    'x86_64_Live_Design':  '1.3',       # In GB
    'i686_Live_Sci-kde':   '2.7',       # In GB
    'x86_64_Live_Sci-kde': '2.7',       # In GB
    'i686_Live_Robotics':  '1.7',       # In GB
    'x86_64_Live_Robotics':'1.7',       # In GB
    'i686_Live_Jam':       '1.5',       # In GB
    'x86_64_Live_Jam':     '1.5',       # In GB
    'i686_Live_Mate':      '660',       # In MB
    'x86_64_Live_Mate':    '694',       # In MB
    'PPC64_DVD':           '4.3',       # In GB
    'PPC64_Netinstall':    '333',       # In MB
    's390_DVD':            '4.0',       # In GB
    'i686_sda.qcow2':      '225',       # In MB
    'x86_64_sda.qcow2':    '226',       # In MB
    'i686_raw':            '137',       # In MB
    'x86_64_raw':          '129'        # In MB
}
