from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.1.0'
DESCRIPTION = 'Simple, storage efficient solution to find definitions with ease.'
LONG_DESCRIPTION = (Path('README.md')).read_text()

setup(
    name="english_dict",
    version=VERSION,
    author='dsochamp',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['bs4'],
    keywords=['dictionary', 'meaning', 'english', 'easy to use'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Natural Language :: English',
    ]
)