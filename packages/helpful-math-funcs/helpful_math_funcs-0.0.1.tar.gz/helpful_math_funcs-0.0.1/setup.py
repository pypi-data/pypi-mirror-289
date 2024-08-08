import setuptools

with open("helpful_math_funcs/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helpful_math_funcs",
    version="0.0.1",
    author="Niklas Knapp",
    author_email="niklas.knapp@telekom.de",
    description="A package for mathematical calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/helpful_math_funcs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)