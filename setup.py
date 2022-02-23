import re
from setuptools import setup


versio = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('gather/gather.py').read(),
    re.M
    ).group(1)


with open("readme.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(name='powerBI-EIO-NPP',
      version=versio,
      description='Script for gathering data from other apiclients and refreshing Power BI workbooks',
      long_description=long_descr,
      long_description_content_type='text/markdown',
      url='https://github.com/NilPujolPorta/powerBI-EIO-NPP',
      author='Nil Pujol Porta',
      author_email='nilpujolporta@gmail.com',
      license='GNU',
      packages=['gather'],
      install_requires=[
          'keyboard',
          'argparse',
          "setuptools>=42",
          "wheel",
          "CatbackupAPI-NPP",
          "HyperbackupAPI2-NPP",
          "PandoraFMS-API",
          "SynologyAPI-NPP",
          "PowerBI-refresher-NPP"
      ],
	  entry_points = {
        "console_scripts": ['powerBI-EIO-NPP = gather.gather:main']
        },
      zip_safe=False)
