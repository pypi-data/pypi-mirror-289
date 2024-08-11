from setuptools import setup, find_packages

setup(
    name='BlockScoutSDK',
    version='1.0.0',
    packages=find_packages(),
    license='GNU General Public License v3.0',
    description='A python wrapper for the BlockScout eth,optimism, base, blast and polygon apis',
    long_description=open('README.md').read(),
    install_requires=[
        'requests',
    ],
    url='https://github.com/kbm9696/BlockScout-SDK',
    author='Balamurugan',
    author_email='kbala007.1996@gmail.com',
    long_description_content_type='text/markdown'
)