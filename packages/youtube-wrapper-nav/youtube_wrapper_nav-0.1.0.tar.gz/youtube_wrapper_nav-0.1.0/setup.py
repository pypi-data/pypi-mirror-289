from setuptools import setup, find_packages

setup(
    name='youtube_wrapper_nav',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'google-api-python-client',
        'youtube-transcript-api'
    ],
    author='Navroop Chandwani',
    author_email='navroopchandwani@gmail.com',
    description='A Python wrapper for YouTube Data API and YouTube Transcript API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/navroop-ch/youtube_wrapper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
