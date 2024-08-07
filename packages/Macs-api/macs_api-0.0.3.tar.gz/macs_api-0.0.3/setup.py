from setuptools import setup, find_packages

setup(
    name='Macs-api',  # Installation name
    version='0.0.3',
    packages=find_packages(include=['macsploit', 'macsploit.*']),
    install_requires=[],  # List any dependencies here
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
