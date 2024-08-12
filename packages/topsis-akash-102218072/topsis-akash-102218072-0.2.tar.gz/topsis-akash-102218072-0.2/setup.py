from setuptools import setup, find_packages

setup(
    name='topsis-akash-102218072',
    version='0.2',
    author='Akash Khatri',
    author_email='akashkhatri2403@gmail.com',
    description='A Python package for TOPSIS method',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'topsis-akash-102218072 = topsis_akash_102218072.topsis:main'
        ],
    },
    install_requires=[
        'numpy',
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

