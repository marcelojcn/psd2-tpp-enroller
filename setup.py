import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="psd2-tpp-enroller",
    version="1.0.0",
    author="Marcelo Nunes",
    author_email="marcelojcnunes@hotmail.com",
    description="A tpp client library to call PSD2 API, taking care of security setup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcelojcn/psd2-tpp-enroller",
    project_urls={
        "Bug Tracker": "https://github.com/marcelojcn/psd2-tpp-enroller/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
