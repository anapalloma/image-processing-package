from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "image-processing-package",
    version = "0.0.1",
    author = "Ana Palloma Rocha Fernandes",
    author_email = "anapallomarocha@gmail.com",
    description = "Pacote de processamento de imagens",
    long_description = page_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/anapalloma/image-processing-package.git",
    packages = find_packages(),
    install_requires = requirements,
    python_requires = '>= 3.8'
)