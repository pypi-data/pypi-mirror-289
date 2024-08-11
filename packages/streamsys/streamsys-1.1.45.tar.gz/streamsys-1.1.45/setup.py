from setuptools import setup, find_packages

setup(
    name='streamsys',
    version='1.1.45',  # Asegúrate de que esta versión no esté ya en PyPI
    description='Advanced Streaming System | Available with 24/7 Stream',
    author='Javi17mod',
    author_email='javi17mod@gmail.com',
    packages=find_packages(),  # Encuentra todos los paquetes automáticamente
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
