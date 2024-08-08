from distutils.core import setup
# import setuptools
pkg_name = 'bdup'
packages = [pkg_name]
setup(name=pkg_name,
      version='0.0.3',
      author='xigua, ',
      author_email="2587125111@qq.com",
      url=f'https://pypi.org/project/{pkg_name}/#files',
      long_description='''
      世界上最庄严的问题：我能做什么好事？
      ''',
      packages=packages,
      package_dir={'requests': 'requests'},
      license="MIT",
      python_requires='>=3.6',
      )
