from setuptools import setup, find_packages

setup(
    name='synccord',  # Name of the package
    version='0.1.0',  # Package version
    packages=find_packages(),  # Automatically find and include all packages in the directory
    description='A firefly developer tools for AI integration',  # Short description
    long_description=open('README.md').read(),  # Long description from README
    long_description_content_type='text/markdown',  # Format of long description
    author='Jane Doe',  # Your name
    author_email='JanDoe237@gmail.com',  # Your email
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],  # Classifiers help users find your package and understand its compatibility
    python_requires='>=3.6',  # Specify Python version requirement
    # Add any package dependencies here
    install_requires=[
        'pywinauto',
    ],
)
