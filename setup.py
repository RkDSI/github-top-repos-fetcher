from setuptools import setup, find_packages

setup(
    name='repo_analyst',
    version='0.1.0',
    author='Your Name',
    author_email='rkopaee@gmail.com',
    description='A Python package for analyzing GitHub repositories.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RkDSI/github-top-repos-fetcher',
    packages=find_packages(),
    install_requires=[
        'requests',
        'matplotlib',
        'pyyaml'
        # Add any other necessary packages here
    ],
    python_requires='>=3.6',
    # Add any additional package metadata here
)

