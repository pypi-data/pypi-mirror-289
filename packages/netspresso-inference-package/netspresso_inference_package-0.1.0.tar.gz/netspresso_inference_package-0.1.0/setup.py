from setuptools import setup, find_packages

setup(
    name="netspresso_inference_package",
    version="0.1.0",
    author="NetsPresso",
    author_email="netspresso@nota.ai",
    description="Inference module.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nota-github/netspresso_inference_package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
