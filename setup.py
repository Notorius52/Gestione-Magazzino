from setuptools import setup, find_packages

setup(
    name="magazzino-manager",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'Pillow>=9.0.0',
        'matplotlib>=3.7.0',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Sistema di gestione magazzino con interfaccia grafica",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/magazzino-manager",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'magazzino-manager=src.main:main',
        ],
    },
) 