from setuptools import setup, find_packages

setup(
    name="CapyScript",
    version="0.0.1",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'CapyScript = main:main',
        ],
    },
    install_requires=[
        # Lista de dependencias si las hay
    ],
    author="Daniel Cerritos",
    description="Un framework personalizado para generar HTML, CSS y JS desde una sintaxis simple.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/tuusuario/my_custom_framework",  # Cambia por tu URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
