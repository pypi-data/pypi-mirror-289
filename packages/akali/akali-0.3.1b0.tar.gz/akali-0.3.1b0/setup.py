from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="akali",
    version="0.3.1-beta",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "transformers>=4.43.1,<5.0.0",
        "torch",
        "accelerate",
        "bitsandbytes>=0.39.0",
        "nest-asyncio",
        "click",
        "pandas",
        "matplotlib",
    ],
    extras_require={
        "dev": ["pytest>=6.2.5,<7.0.0", "pytest-cov>=2.12.1,<3.0.0", "mypy>=0.910,<1.0.0"],
    },
    entry_points={
        'console_scripts': [
            'akali=akali.cli:cli',
        ],
    },
    author="Ali Eren Ak",
    author_email="akali@sabanciuniv.edu",
    description="AKALI library for language model augmentation and interfaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alierenak/akali",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.8',
    license="Proprietary",
    keywords="NLP, language models, data augmentation, AI",
)