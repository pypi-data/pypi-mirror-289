from setuptools import setup, find_packages

setup(
    name='SpotiTube',
    version='0.0.1',
    author='Snehashish Laskar',
    author_email='snehashishlaskar.dev@example.com',
    description='A package to download songs from Spotify using YouTube',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/snehashish090/song_downloader',  # Update with your GitHub repo URL
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'pytube>=12.1.0',
        'spotipy>=2.19.0',
        'moviepy>=1.0.3',
        'eyed3>=0.9.5',
        'pytubefix>=1.0.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
)
