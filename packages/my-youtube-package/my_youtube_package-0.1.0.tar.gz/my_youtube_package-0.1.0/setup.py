from setuptools import setup, find_packages

setup(
    name='my_youtube_package',
    version='0.1.0',
    author='Souvik Sen',
    author_email='souviks1008@gmail.com',
    description='A package to interact with YouTube Data API and YouTube Transcript API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    install_requires=[
        'google-api-python-client',
        'youtube-transcript-api',
        'pytest'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
