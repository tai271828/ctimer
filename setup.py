#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ["pandas", "bokeh", "calmap", "matplotlib"]

test_requirements = ['pytest>=3', ]

setup(
    author="Liting Chen",
    author_email='litingchen16@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Office/Business :: Scheduling',
    ],
    description="Pomodoro is a famous time management technique aka tomato clock. Pomodoro C-timer is written in "
                "python and tkinter. This is a well maintained project. Your contributions are welcome on github!",
    entry_points={
        'console_scripts': [
            'ctimer=ctimer.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software license",
    long_description=readme + '\n',
    include_package_data=True,
    keywords=['timer', 'concentration', 'pomodoro', 'time management'],
    name='pomodoro-ctimer',
    packages=find_packages(include=['ctimer', 'ctimer.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/zztin/pomodoro-ctimer',
    version='2.0.2',
    zip_safe=False,
)
