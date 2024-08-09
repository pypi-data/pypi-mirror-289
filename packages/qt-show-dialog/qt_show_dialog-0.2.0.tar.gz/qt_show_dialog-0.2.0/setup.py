from pathlib import Path

from setuptools import setup

import src.show_dialog

PROJECT_ROOT = Path(__file__).parent
ASSETS_DIR = PROJECT_ROOT / 'assets'

with open(PROJECT_ROOT / 'README.md') as f:
    long_description = f.read()

setup(
    name='show-dialog',
    version=src.show_dialog.__version__,
    py_modules=['show_dialog'],
    provides=['show_dialog'],
    description='Easily show a dialog',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Joao Coelho',
    author_email='6wfon3p6d@mozmail.com',
    url='https://github.com/joaonc/show_dialog',
    keywords='qt, qt6',
    # install_requires=REQUIREMENTS,
    license='MIT License',
    python_requires='>=3.10',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
