from setuptools import setup


def get_readme():
    with open('README.md') as f:
        return f.read()


def get_license():
    with open('LICENSE.txt') as f:
        return f.read()


setup(
    name='paul6325106.pytest-multiple-webdrivers-fallthrough',
    version='1.0.dev0',
    description='Example of reusing browser instances for single and multiple browser tests',
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    author='paul6325106',
    license=get_license(),
    python_requires='>=3.7',
    install_requires=[
        'selenium'
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-runner'
        ],
        'lint': [
            'mypy',
            'pycodestyle'
        ]
    },
    zip_safe=False
)
