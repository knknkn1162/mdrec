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
      description='record python object to markdown file & convert to html.',
      classifiers=[
          "Programming Language :: Python :: 3 :: Only",
          "Framework:: IPython",
      ],
      packages=find_packages(exclude=["tests"]),
      include_package_data=True,
      zip_safe=False,
      test_suite="tests",
      install_requires=install_requires,
      entry_points="""
""")
