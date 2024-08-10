from setuptools import setup, find_packages

setup(
    name="azrailv3",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    description="A module to bypass reCAPTCHA v3 challenges.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/azrailv3",  # GitHub repo URL'nizi buraya ekleyin
    author="Fatih",
    author_email="your.email@example.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
