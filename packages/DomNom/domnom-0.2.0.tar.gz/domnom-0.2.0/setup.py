from setuptools import setup, find_packages

setup(
    name='DomNom',
    version='0.2.0',
    description='A Python package for routing and web application management.',
    author='Hiralal Singh',
    author_email='hiralals221@gmail.com',
    url='https://github.com/yourusername/DomNom',  # Update with your GitHub repo URL
    packages=find_packages(),
    install_requires=[
        'Flask>=2.0',           # Example: If using Flask for routing
        'requests>=2.26',       # Example: If using requests for HTTP handling
        
    ],
    tests_require=[
        'pytest>=7.0',
        'pytest-cov>=3.0'
    ],
    extras_require={
        'dev': [
            'tox>=3.0',
            'black>=22.0',      # Optional: Code formatting tool
            'flake8>=4.0',      # Optional: Linting tool
        ],
    },
    setup_requires=['wheel'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
