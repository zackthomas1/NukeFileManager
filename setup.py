try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Nuke File Manger',
    'author' : 'Zach Thomas',
    'url' : 'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email' : 'My Email',
    'version' : '0.1',
    'install_requires' : ['pyside2'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'NukeFileManger'
}

set(**config)
