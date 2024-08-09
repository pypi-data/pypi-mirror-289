from setuptools import setup, find_packages

setup(
    name='COPEX_high_rate_compression_quality_metrics',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    author='VisioTerra',
    author_email='info@visioterra.fr',
    description='COPEX high rate compression quality metrics',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/VisioTerra/COPEX_high_rate_compression_quality_metrics',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
