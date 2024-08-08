from setuptools import setup, find_packages

setup(
    name="notification-sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias
    ],
    author="Jean Palomino",
    author_email="jeancarlo.palomino.g@gmail.com",
    description="Una breve descripción de tu paquete",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/jeancarlo-dev/notification-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
