from setuptools import setup, find_packages

setup(
    name="crackeduuid",
    version="0.1",
    packages=find_packages(),
    description="Fetches online and offline UUIDs for Minecraft usernames.",
    author="Your Name",
    author_email="proxdegaming@gmail.com",
    install_requires=[
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'crackeduuid=mcuuid.cli:main',  # Update this line if the module name is changed
        ],
    },
)
