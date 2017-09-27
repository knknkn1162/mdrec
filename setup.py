from setuptools import setup, find_packages

install_requires = [
    "pandas",
    "grip",
    "pytablewriter",
    ]

setup(name='mdrec',
      version='0.1',
      description='record python object in markdown file & convert to html.',
      packages=find_packages("mdrec"),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
""")
