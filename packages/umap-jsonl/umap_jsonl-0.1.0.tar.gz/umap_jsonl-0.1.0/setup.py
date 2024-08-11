from setuptools import setup, find_packages

setup(
    name='umap-jsonl',
    version='0.1.0',
    author='David Steinberg',
    author_email='david@resium.com',  # Replace with your email
    description='A command-line tool for generating UMAP plots and KMeans clustering from JSONL data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/david4096/umap-jsonl',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'umap-learn',
        'scikit-learn',
        'matplotlib',
        'jsonlines'
    ],
    entry_points={
        'console_scripts': [
            'umap-jsonl=umap_jsonl.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
