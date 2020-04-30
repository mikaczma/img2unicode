from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='img2unicode',
    version='0.1a2',
    description='Convert images to unicode based on font templates. Especially usable in terminal.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/matrach/img2unicode',
    author='Maciej Matraszek',
    author_email='matraszek.maciej@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={
        'img2unicode': ['*.npz', '*.npy'],
    },
    install_requires=[
          'numpy',
          'pandas',
          'scikit-image',
          'pillow',
          'n2', # For FastRenderer
    ],
    extras_require={
        'develop': [
            'pytest',
            'pytest-cov',
            'sphinx',
            'sphinx_autodoc_typehints',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    zip_safe=False)
