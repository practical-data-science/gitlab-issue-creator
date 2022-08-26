from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='GitLab Issue Creator',
    packages=['gitlab_issue_creator'],
    version='0.001',
    license='MIT',
    description='GitLab Issue Creator is a Python package for creating GitLab issues.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Matt Clarke',
    author_email='matt@practicaldatascience.co.uk',
    url='https://github.com/practicaldatascience/gitlab-issue-creator',
    download_url='https://github.com/practicaldatascience/gitlab-issue-creator/archive/master.zip',
    keywords=['python', 'gitlab'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=['python-gitlab']
)
