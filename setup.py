from setuptools import setup, find_packages

setup(
        name='sgeparse',
        author='Simon Walker',
        author_email='s.r.walker101@googlemail.com',
        version='0.0.1',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        )
