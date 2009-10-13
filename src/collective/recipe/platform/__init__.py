
import sys, platform

def getplatform():
    if sys.platform == 'darwin':
        mac_ver = platform.mac_ver()
        if mac_ver[0].startswith('10.6'):
            return 'darwin10'
        elif mac_ver[0].startswith('10.5'):
            return 'darwin9'
    return sys.platform

class Recipe(object):

    # TODO:
    #   1. auto-generate empty options if there is no platform match
    #   2. allow platform submatches: e.g.: darwin matches all darwinXX
    def __init__(self, buildout, name, options):
        options['platform'] = getplatform()
        for key in options.keys():
            if '-' in key and key.startswith(options['platform']):
                options[key.split('-', 1)[1].strip()] = options[key]

    def install(self):
        return tuple()

    def update(self):
        pass
