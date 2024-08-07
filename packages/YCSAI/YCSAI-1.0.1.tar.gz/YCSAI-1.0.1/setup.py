from setuptools import setup, find_packages

setup(
    name='YCSAI',
    version='1.0.1',
    description='AI Training API developed by SphereAX.',
    author='Changseob',
    author_email='yuncs@sphereax.com',
    url='https://github.com/changsubi/YCSAI.git',
    install_requires=['omegaconf', 'numpy', 'tqdm', 'matplotlib', 'requests', 'pandas', 'psutil', 'hydra-core', 'Pillow==9.5.0', 'seaborn', 'scipy', 'torch', 'torchvision', 'torchaudio'],
    packages=find_packages(exclude=[]),
    keywords=['Train', 'Predict', 'Detection', 'Classification'],
    python_requires='>=3.9',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ],
)
