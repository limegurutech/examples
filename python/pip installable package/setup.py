import setuptools

setuptools.setup(
    name='limeguru',
    version='0.0.1',
    description='limeguru python module',
    url='https://stash.aexp.com/stash/projects/AIM500001213/repos/mlops-utils/browse',
    author='Limeguru',
    author_email='contact@limeguru.com',
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'pytest'
    ],
    long_description='limeguru python module',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
)