#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': 'qgroundcontrol'}]
build_prefix = 'extra-aarch64'
time_limit_hours = 4

def pre_build():
    aur_pre_build('qgroundcontrol')
    add_arch(['aarch64'])
    add_makedepends(['qt5-x11extras', 'qt5-wayland'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main('extra-x86_64')
