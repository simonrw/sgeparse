from setuptools import setup, find_packages

setup(name='sgeparse',
      author='Simon Walker',
      author_email='s.r.walker101@googlemail.com',
      description='For parsing running SGE jobs',
      long_description=open('README.rst').read(),
      url='https://pypi.python.org/pypi/sgeparse',
      version='0.0.2',
      license='MIT',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          ],
      )
