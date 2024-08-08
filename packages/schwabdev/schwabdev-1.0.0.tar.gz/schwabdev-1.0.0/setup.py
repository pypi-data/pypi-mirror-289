from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Schwab API Python Client (unofficial)'
with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='schwabdev',
    version=VERSION,
    author='Tyler Bowers',
    author_email='tylerebowers@gmail.com',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.11',
    install_requires=[
        'requests',
        'websockets',
    ],
    keywords=['python', 'schwab', 'api', 'client', 'finance', 'trading', 'stocks', 'equities', 'options', 'forex', 'futures'],
    classifiers=[
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ],
    project_urls={
        'Source': 'https://github.com/tylerebowers/Schwab-API-Python',
        'Youtube': 'https://www.youtube.com/playlist?list=PLs4JLWxBQIxpbvCj__DjAc0RRTlBz-TR8',
        'PyPI': 'https://pypi.org/project/schwabdev/'
    }
)
