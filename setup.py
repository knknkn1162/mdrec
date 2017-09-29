from setuptools import setup, find_packages

install_requires = [
    "pandas",
    "grip",
    "pytablewriter",
    "ipython",
    "pyyaml",
    ]

setup(name='mdrec',
      version='0.1dev',
      description='record python object in markdown file & convert to html.',
      packages=find_packages("mdrec"),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
""")
