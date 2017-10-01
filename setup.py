from setuptools import setup, find_packages

install_requires = [
    "pandas",
    "grip",
    "pytablewriter",
    "ipython",
    "pyyaml",
    ]

with open("README.md") as f:
    long_description = f.read()

setup(name='mdrec',
      version='0.1',
      description='record python object to markdown file & convert to html.',
      long_description=long_description,
      classifiers=[
          "Programming Language :: Python :: 3 :: Only",
          "Framework :: IPython",
      ],
      packages=find_packages(exclude=["tests"]),
      url="https://github.com/knknkn1162/mdrec",
      author="knknkn1162",
      author_email="knknkn1162@gmail.com",
      include_package_data=True,
      zip_safe=False,
      test_suite="tests",
      license="MIT",
      keywords="",
      install_requires=install_requires,
      entry_points="""
""")
