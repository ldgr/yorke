import setuptools


setuptools.setup(
    name='yorke',
    version='0.0.1',
    url='https://github.com/ldgr/yorke',
    license='Apache',
    author='Ldgr Corporation',
    author_email='patrick@ldgr.io',
    description='Experimental encryption tools. ',
    long_description=open('README.md').read(),
    py_modules=['yorke'],
    include_package_data=True,
    platforms='any',
    scripts=['bin/yorke'],
)
