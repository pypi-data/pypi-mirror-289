from setuptools import setup, find_packages

setup(
    name='youtube_wrapper',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'google-api-python-client',
        'requests',
    ],
    test_requires=[
        'pytest',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A wrapper for YouTube Data API and YouTube Transcript API',
    url='https://github.com/yourusername/youtube_wrapper',
)

