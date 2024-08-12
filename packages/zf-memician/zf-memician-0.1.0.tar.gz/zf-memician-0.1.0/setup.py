import setuptools
from os import path as os_path

PACKAGE_NAME = "zf-memician"
AUTHOR_NAME = "Zeff Muks"
AUTHOR_EMAIL = "zeffmuks@gmail.com"

with open("README.md", "r") as f:
    readme = f.read()


def read_version():
    version_file = os_path.join(os_path.dirname(__file__), "memician", "version.py")
    with open(version_file) as file:
        exec(file.read())
    version = locals()["__version__"]
    print(f"Building {PACKAGE_NAME} v{version}")
    return version

setuptools.setup(
    name=PACKAGE_NAME,
    version=read_version(),
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Memician is a state of the art Memelord",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={
        "memician": [
            "Resources/*/*"
        ]
    },
    packages=setuptools.find_packages(
        include=[
            'memician',
            'memician.*'
        ],
        exclude=[
            'venv',
            'venv.*'
        ]
    ),
    license="PROPRIETARY",
    install_requires=[
        "pillow",
        "requests",
        "loguru"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)