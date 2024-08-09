from setuptools import setup, find_packages

VERSION = '0.2.22'
DESCRIPTION = 'Tokenizing and processing text inputs with transformer models'
LONG_DESCRIPTION = ('A package that provides functionalities for tokenizing and processing text inputs using '
                    'transformer models and other NLP tools.')

setup(
    name="tokenize-text",
    version=VERSION,
    author="Urdu NLTK",
    author_email="urdu-nltk@uts.rf.gd",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "transformers",
        "textblob",
        "requests",
        "json5",
        "pyarmor"
    ],
    package_data={
        'tokenized.dist': ['*.so', '*.py', 'pytransform/*'],
    },
    include_package_data=True,
    keywords=['tokenization', 'text-processing', 'nlp', 'transformers'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)