from setuptools import setup, find_packages


setup(
    name="Timeline_Manager",  # The name of your package
    version="1.1.0",  # The version of your package
    author="Vassalis",  # Your name or organization
    author_email="anri.tvalabeishvili@gmail.com",  # Your contact email
    description="A job scheduling library that supports various time intervals",  # A short description of your package
    long_description=open("README.md").read(),  # Long description read from a file
    long_description_content_type="text/markdown",  # The format of the long description (usually 'text/markdown')
    url="https://github.com/anri-Tvalabeishvili/Timeline-Manager",  # URL to your project's homepage (GitHub, etc.)
    packages=find_packages(),  # Automatically find and include all packages in the project
    install_requires=[
        # List your package dependencies here
        # Example: 'requests', 'numpy', etc.
    ],
    project_urls={
        'Documentation': 'https://timeline-manager.readthedocs.io/en/latest/index.html',
        'HomePage': 'https://github.com/anri-Tvalabeishvili/Timeline-Manager',
        'Tracker': 'https://github.com/anri-Tvalabeishvili/Timeline-Manager/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",  # Specify the Python versions supported
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",  # OS compatibility
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)