from setuptools import setup

setup(name='node2vec',
        version='0.1',
        description='Node to vector models',
        packages=['node2vec'],
        install_requires=['numpy', 'scipy', 'networkx', 'gensim']
        )
