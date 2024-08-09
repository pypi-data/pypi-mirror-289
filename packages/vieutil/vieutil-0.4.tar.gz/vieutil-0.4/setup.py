from distutils.core import setup

setup(
    name="vieutil",  # How you named your package folder (MyLib)
    packages=["vieutil"],  # Chose the same as "name"
    version="0.4",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="Password encryption",  # Give a short description about your library
    author="Fabio Toniolo Vieira Junior",  # Type in your name
    author_email="ftoniolo@viemar.com.br",  # Type in your E-Mail
    url="https://github.com/ftonioloviemar/vieutil",  # Provide either the link to your github or to your website
    download_url="https://github.com/ftonioloviemar/vieutil/archive/refs/tags/V_0.3.tar.gz",  # I explain this later on
    keywords=[
        "viemar",
        "util",
        "cryptography",
        "logging",
        "send_email",
    ],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        "cryptography",
        "tenacity",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3.0",  # Specify which python versions that you want to support
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
