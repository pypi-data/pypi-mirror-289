from setuptools import setup, find_packages

setup(
    name="yt-rss-dl",
    version="0.0.2",
    author="Joannes J.A. Wyckmans",
    author_email="johan.wyckmans@gmail.com",
    description="A YouTube RSS Video Downloader",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thisisawesome1994/yt-rss-dl",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "feedparser",
        "yt-dlp",
    ],
    entry_points={
        'console_scripts': [
            'yt-rss-dl=ytrssdl.main:main',
        ],
    },
)
