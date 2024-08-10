from setuptools import setup, find_packages
from ytrssdl import __version__ 

setup(
    name='yt-rss-dl',
    version=__version__,
    description='A RSS feed downloader for YouTube Channels',
    author='Joannes J.A. Wyckmans',
    author_email='johan.wyckmans@gmail.com',
    url='https://github.com/thisisawesome1994/yt-rss-dl',  # Replace with your GitHub repo URL
    packages=find_packages(),
    install_requires=[
        'feedparser',
        'yt-dlp',
    ],
    entry_points={
        'console_scripts': [
            'yt-rss-dl = ytrssdl.main:main',  # Assuming your main function is in a file called 'main.py'
        ],
    },
)