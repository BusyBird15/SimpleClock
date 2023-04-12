# pyproject.toml

[build-system]
requires      = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "SimpleClock"
version = "1.0"
description = "Simplified functions of the time module for newbies."
readme = "README.md"
authors = [{ name = "Busybird15", email = "busybird15@mail.com" }]
license = { file = "LICENSE.md" }
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]
keywords = ["time", "clock", "easy", "simple"]
dependencies = [
    "time",
]
requires-python = ">=3.9"

[project.optional-dependencies]
dev = ["black", "bumpver", "isort", "pip-tools", "pytest"]

[project.urls]
Homepage = "https://github.com/busybird15/simpleclock"

[project.scripts]
realpython = "reader.__main__:main"
