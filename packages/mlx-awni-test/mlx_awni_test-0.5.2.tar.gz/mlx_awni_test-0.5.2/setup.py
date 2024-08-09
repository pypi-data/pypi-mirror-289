# Copyright © 2024 Apple Inc.

from setuptools import setup

setup(
    name="mlx-awni-test",
    version="0.5.2",
    description="LLMs on Apple silicon with MLX and the Hugging Face Hub",
    long_description="Description",
    long_description_content_type="text/markdown",
    readme="README.md",
    author_email="mlx@group.apple.com",
    author="MLX Contributors",
    url="https://github.com/ml-explore/mlx-examples",
    license="MIT",
    packages=["mlx_awni_test"],
    python_requires=">=3.8",
    extras_require={
        "testing": ["datasets"],
    },
)
