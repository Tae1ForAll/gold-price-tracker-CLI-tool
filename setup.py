from setuptools import setup

setup(
    name='gold-price-tracker-CLI',
    version='0.1.0',
    py_modules=['app', 'sender', 'model', 'set_handler'],
    install_requires=[
        'requests',
        'schedule',
        'python-dotenv'
    ],
    entry_points={
        "console_scripts": [
            "gprice=app:main"
        ]
    }
)