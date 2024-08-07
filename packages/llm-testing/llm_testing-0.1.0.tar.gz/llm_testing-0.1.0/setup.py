from setuptools import setup, find_packages

setup(
    name='llm-testing',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'google-generativeai'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for generating code using various AI models.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
