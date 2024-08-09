from setuptools import setup, find_packages

setup(
    name='evalgen',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'sqlalchemy',
        'langchain',
        'openai',
        'mkdocs',
        'mkdocstrings[python]',
        'mkdocs-material',
        'python-dotenv',
        'pandas',
        'pyyaml',
        'tabulate'
    ],
    entry_points={
        'console_scripts': [
            'evalgen=evalgen.cli:main',
        ],
    },
    # Additional metadata
    author='Scribble Data, Inc',
    author_email='support@scribbledata.io',
    description='A description of the evalgen package',
    url='https://github.com/scribbledata/evalgen',  # Replace with your repository URL
    license='MIT',  # Replace with your license
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
