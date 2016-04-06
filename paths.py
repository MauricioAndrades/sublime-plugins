import os

LOCAL = '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/git/bin:/usr/local/bin/node_modules/.bin'
# modPY = '/Users/Op/Library/Application Support/Sublime Text 3/Packages/Python PEP8 Autoformat/libs/py33:/Users/Op/Library/Application Support/Sublime Text 3/Packages/Python PEP8 Autoformat/libs'
# Sublime's default path is
# /usr/bin:/bin:/usr/sbin:/sbin
os.environ['PATH'] = LOCAL
