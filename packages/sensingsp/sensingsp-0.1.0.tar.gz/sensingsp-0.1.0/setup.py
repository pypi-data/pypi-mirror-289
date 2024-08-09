from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='sensingsp',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'bpy==4.0.0',
        'certifi==2024.7.4',
        'charset-normalizer==3.3.2',
        'contourpy==1.2.1',
        'cycler==0.12.1',
        'Cython==3.0.11',
        'fonttools==4.53.1',
        'idna==3.7',
        'kiwisolver==1.4.5',
        'llvmlite==0.43.0',
        'mathutils==3.3.0',
        'matplotlib==3.9.1.post1',
        'numba==0.60.0',
        'numpy==2.0.1',
        'opencv-python==4.10.0.84',
        'packaging==24.1',
        'pillow==10.4.0',
        'pyparsing==3.1.2',
        'python-dateutil==2.9.0.post0',
        'requests==2.32.3',
        'scipy==1.14.0',
        'six==1.16.0',
        'urllib3==2.2.2',
        'zstandard==0.23.0',
    ],
    url='https://gitlab.com/sparc-snt/sensing-signal-processing',
    license='MIT',
    author='Moein Ahmadi',
    author_email='moein.ahmadi@uni.lu, gmoein@gmail.com',
    description='SensingSP™ is a Blender-based open-source library for simulating the electromagnetic based sensing systems and signal processing algorithms implementations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
)
