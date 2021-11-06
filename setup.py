from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='PackagePyPITest',
    version='0.0.1',
    url='https://github.com/DiegoAbreu/PyPITest',
    license='MIT License',
    author='Diego Abreu',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='',
    keywords='Pacote',
    description=u'Teste de Publicação de pacote PyPI',
    packages=['PackagePyPITest'],
    install_requires=[])