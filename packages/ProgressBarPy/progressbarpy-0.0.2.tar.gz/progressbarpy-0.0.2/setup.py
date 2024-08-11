from setuptools import setup, find_packages
import pathlib

__version__ = "0.0.2"

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text(encoding='utf-8')

setup(
    name='ProgressBarPy',
    version=__version__,

    url='https://github.com/Vladislavus1/ProgressBarPy',
    author='Vladislavus1',
    author_email='vlydgames@gmail.com',

    description='This package adds simple windowed progressbar.',
    long_description=README,
    long_description_content_type='text/markdown',

    packages=find_packages(),
)