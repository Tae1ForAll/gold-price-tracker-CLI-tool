from setuptools import setup

setup(
    name='gold-price-tracker-CLI',
    version='0.1.0',
    py_modules=[
        'app', 
        'sender', 
        'model', 
        'get_gold_price',
        'error',
        'commands',
        'scheduler',
        'condition_parser'],
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