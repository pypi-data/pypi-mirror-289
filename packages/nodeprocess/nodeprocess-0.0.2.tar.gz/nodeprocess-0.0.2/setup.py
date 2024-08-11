from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Node Process Community Detection'
LONG_DESCRIPTION = 'Package for temporal community detection, using link data as well as correlations between processes on nodes'

# Setting up
setup(
        name="nodeprocess", 
        version=VERSION,
        author="Patrick Gildersleve",
        author_email="<p.gildersleve@lse.ac.uk>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['numpy', 'pandas', 'igraph', 'leidenalg'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'network science', 'community detection', 'Wikipedia'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)