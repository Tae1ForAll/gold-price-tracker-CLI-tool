from setuptools import setup, find_packages
from gprice import __version__

setup(
    name='gprice',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'requests',
        'schedule',
        'python-dotenv'
    ],
    entry_points={
        "console_scripts": [
            "gprice=gprice.app:main"
        ]
    }
)