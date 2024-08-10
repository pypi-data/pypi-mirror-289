from setuptools import setup, find_packages

setup(
    name='streamsys',
    version='1.0.0',
    description='Advanced Streaming System | Avaible with 24/7 Stream',
    author='Javi17mod',
    author_email='javi17mod@gmail.com',  # Cambia esto por tu email
    packages=find_packages(where='StreamSYS'),
    package_dir={'': 'StreamSYS'},
    install_requires=[],  # Aquí puedes listar las dependencias si las hay
    entry_points={
        'console_scripts': [
            'streamsys=StreamSYS.StreamSYS:main',  # Este es el punto de entrada para el script
        ],
    },
    include_package_data=True,
    python_requires='>=3.6',  # Ajusta según la versión de Python que necesites
)
