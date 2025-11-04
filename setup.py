from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="elrahpy",
    version="0.1.7",
    packages=find_packages(),
    description="Package pour renforcer mes compétences, améliorer ma productivité et partager mon expertise avec la communauté ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Harlequelrah",
    author_email="maximeatsoudegbovi@example.com",
    url="https://github.com/Harlequelrah/Library-ElrahPy",
    license="LGPL-3.0-only",
    python_requires=">=3.10",
    install_requires=["python-dateutil", "pytest", "pytest-mock"],
)
