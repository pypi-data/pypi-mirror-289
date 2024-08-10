from setuptools import setup, find_packages

setup(
    name="spotiv3",
    version="0.3.9",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    description="A Python module for bypassing reCAPTCHA v3",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/spotiv3",  # GitHub reposu veya başka bir URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)