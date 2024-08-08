from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    README = f.read()

setup(
    name='reluai',
    version='1.0.0',
    description='A command-line assistant powered by Gemini AI to enhance productivity',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Giovanny Jimenez',
    author_email='gjimenezdeza@gmail.com',
    url='https://github.com/techatlasdev/relu-cli',
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        'requests>=2.25.1',
        'google-generativeai',  # Añadida la librería google-generativeai
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'relu=relu.cli:main',
        ],
    },
    keywords=['LLM', 'API', 'assistant', 'gemini', 'google', 'data', 'python', 'cli', 'ReLU', 'AI', 'Gemini AI'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/techatlasdev/relu-cli/issues',
        'Documentation': 'https://github.com/techatlasdev/relu-cli#readme',
        'Source Code': 'https://github.com/techatlasdev/relu-cli',
    },
)
