from setuptools import setup, find_packages

setup(
    name='free-search',  
    version='0.2.0',  
    description='A simple vector database with CRUD and search functionality',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Ken',  
    author_email='ai.free.team@gmail.com', 
    url='https://github.com/AI-FREE-Team/free-search',
    packages=find_packages(),
    install_requires=[
        'numpy==1.26.4',
        'torch==2.3.1',
        'transformers==4.42.4',
        'faiss-cpu==1.8.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)