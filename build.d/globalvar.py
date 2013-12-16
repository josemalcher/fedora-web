#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file defines all variable needed to be edited during the release cycle (alpha, beta...).
release={
    'prev_id':     '19',
    'curr_id':     '20',
    'next_id':     '21',
    'curr_name':   'Heisenbug',
    'next_name':   '',
    'curr_state':  '',             # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_arm_state':  '',         # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_ppc64_state':  '',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_s390_state':  '',        # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_state':  '',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'prev_arm_id': '19',
    'prev_ppc64_id': '18',
    'prev_s390_id': '18',
    'prev_cloud_id': '19',
    'curr_arm_id': '20',
    'curr_ppc64_id': '19',
    'curr_s390_id': '19',
    'curr_cloud_id': '20',
    'next_arm_id': '21',
    'next_ppc64_id': '20',
    'next_s390_id': '20',
    'next_cloud_id': '21',
    'cloud_composedate': '20131211',
    'pre_cloud_composedate': '20131106',
    'RC_gold': '5'                      # insert the number of the RC version declared GOLD
}

path={
    'torrent':         'http://torrent.fedoraproject.org/torrents',
    'torrent_spins':   'http://torrent.fedoraproject.org/torrents',
    'download':        'http://download.fedoraproject.org/pub/fedora/linux/releases',
    'download_spins':  'http://download.fedoraproject.org/pub/alt/releases',
    'download_arch':   'http://download.fedoraproject.org/pub/fedora-secondary/releases',
    'mirrors':         'http://mirrors.fedoraproject.org/metalink?path=pub/fedora/linux/releases',
    'checksums':       './static/checksums',
    'doc':             'http://docs.fedoraproject.org/en-US/Fedora'
}

iso_size={
    'x86_64_DVD':          '4.3',       # In GB
    'i386_DVD':            '4.4',       # In GB
    'source_DVD':          '9.2',       # In GB
    'i686_Live_Desktop':   '922',       # In MB
    'x86_64_Live_Desktop': '953',       # In MB, default download from F18
    'i686_Live_KDE':       '896',       # In MB
    'x86_64_Live_KDE':     '928',       # In MB
    'i686_Live_LXDE':      '598',       # In MB
    'x86_64_Live_LXDE':    '633',       # In MB
    'i686_Live_Xfce':      '614',       # In MB
    'x86_64_Live_Xfce':    '648',       # In MB
    'i386_Netinstall':     '357',       # In MB
    'x86_64_Netinstall':   '321',       # In MB
    'i686_Live_Security':  '769',       # In MB
    'x86_64_Live_Security':'805',       # In MB
    'i686_Live_Games':     '3.7',       # In GB
    'x86_64_Live_Games':   '3.7',       # In GB
    'i686_Live_Elab':      '2.1',       # In GB
    'x86_64_Live_Elab':    '2.1',       # In GB
    'i686_Live_Soas':      '633',       # In MB
    'x86_64_Live_Soas':    '668',       # In MB
    'i686_Live_Design':    '1.3',       # In GB
    'x86_64_Live_Design':  '1.3',       # In GB
    'i686_Live_Sci-kde':   '3.4',       # In GB
    'x86_64_Live_Sci-kde': '3.4',       # In GB
    'i686_Live_Robotics':  '1.9',       # In GB
    'x86_64_Live_Robotics':'1.9',       # In GB
    'i686_Live_Jam':       '1.5',       # In GB
    'x86_64_Live_Jam':     '1.5',       # In GB
    'i686_Live_Mate':      '715',       # In MB
    'x86_64_Live_Mate':    '750',       # In MB
    'PPC64_DVD':           '4.3',       # In GB
    'PPC64_Netinstall':    '333',       # In MB
    's390_DVD':            '4.0',       # In GB
    'i686_sda.qcow2':      '201',       # In MB
    'x86_64_sda.qcow2':    '204',       # In MB
    'i686_raw':            '114',       # In MB
    'x86_64_raw':          '116'        # In MB
}
