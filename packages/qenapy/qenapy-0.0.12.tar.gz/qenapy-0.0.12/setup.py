from setuptools import find_packages, setup

setup(
    name="qenapy",
    version="0.0.12",
    description="This is Qena's microservice library",
    author="Naol Arega",
    author_email="narega@qena.dev",
    url="https://github.com/abrsh4/qenapy.git",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "pydantic>=2",
        "motor",
        "httpx",
        "python-dotenv",
        "python-jose",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
