from setuptools import setup, find_packages

setup(
    # Project metadata
    name="test_make",
    version="0.1",  # Dynamic version will be filled by setuptools_scm
    description="Testing a package.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="ruchi",
    author_email="ruchimali24@gmail.com",
    keywords=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    license="Apache-2.0",
    url="",
    project_urls={
    },
    python_requires=">=3.8",
    install_requires=[
        "pydantic >= 2.0",
        "tiktoken",
        "aiohttp",
        "python-dotenv",
        "pytest",
    ],
    extras_require={
        "dev": ["ruff == 0.4.5", "pre-commit >= 3.5.0", "black == 24.4.2"],
        "tests": [
            "pytest >= 7.4.0",
            "pytest-asyncio",
            "nest-asyncio",
            "pytest-timeout",
            "pytest-codspeed",
        ],
        "openai": ["openai >= 1.0.0"],
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
