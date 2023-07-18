from setuptools import setup


setup(
    name='decstro',
    author='Max Braun',
    version='0.1',
    description='Decstro is a declarative type safe XML parsing library',
    author_email='maxbraun97@web.de',
    keywords='declarative type safe xml',
    python_requires='>=3.8',
    install_requires=[
        'lxml~=4.9.3'
    ],

    extras_require={
        'test': [
            'pytest~=7.4.0'
        ]
    }
)
