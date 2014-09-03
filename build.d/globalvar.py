#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file defines all variable needed to be edited during the release cycle (alpha, beta...).
release={
    'prev_id':     '19',
    'curr_id':     '20',
    'next_id':     '21',
    'curr_name':   'Heisenbug',
    'next_name':   '',
    'curr_state':  'Alpha',             # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_arm_state':  'Alpha',         # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_ppc64_state':  '',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_s390_state':  '',        # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_state':  'Alpha',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'prev_arm_id': '19',
    'prev_ppc64_id': '19',
    'prev_s390_id': '19',
    'prev_cloud_id': '19',
    'curr_arm_id': '20',
    'curr_ppc64_id': '20',
    'curr_s390_id': '20',
    'curr_cloud_id': '20',
    'next_arm_id': '21',
    'next_ppc64_id': '21',
    'next_s390_id': '21',
    'next_cloud_id': '21',
    'composedate': '20140407',
    'pre_cloud_composedate': '20131106',
    'RC_gold': '5'                      # insert the number of the RC version declared GOLD
}

path={
    'torrent':         'http://torrent.fedoraproject.org/torrents',
    'torrent_spins':   'http://torrent.fedoraproject.org/torrents',
    'download':        'http://download.fedoraproject.org/pub/fedora/linux/releases',
    'dl':              'http://download.fedoraproject.org/pub/fedora/linux/updates',
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
    'PPC64_Netinstall':    '340',       # In MB
    's390_DVD':            '4.6',       # In GB
    'i686_sda.qcow2':      '199',       # In MB
    'x86_64_sda.qcow2':    '201',       # In MB
    'i686_raw':            '115',       # In MB
    'x86_64_raw':          '117',       # In MB
    'x86_64_server_DVD':   '1.9',       # In GB
    'i386_server_DVD':     '2.0',       # In GB
    'x86_64_server_net':   '399',       # In MB
    'i386_server_net':     '459',       # In MB
    'x86_64_workstation':  '1.3',       # In GB
    'i386_workstation':    '1.2',       # In GB
    'x86_64_cloud':        '1.9',       # In GB
    'i386_cloud':          '2.0',       # In GB
    'x86_64_cloud_net':    '399',       # In MB
    'i386_cloud_net':      '459'        # In MB
}
