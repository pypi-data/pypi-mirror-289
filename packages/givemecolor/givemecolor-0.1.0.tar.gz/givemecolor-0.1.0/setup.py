from setuptools import setup, find_packages

setup(
    name="givemecolor",
    version="0.1.0",
    description="Giveme Color is a random color generator package. Every time it returns a new random color and copies it to your clipboard.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="imparth",
    url="https://github.com/imparth7/giveme-color-py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["random", "color"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "givemecolor=givemecolor:givemecolor",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/imparth7/giveme-color-py/issues",
        "Homepage": "https://github.com/imparth7/giveme-color-py#readme",
    },
)
