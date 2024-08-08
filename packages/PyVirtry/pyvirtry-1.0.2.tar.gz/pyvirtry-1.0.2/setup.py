from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="PyVirtry",
    version="1.0.2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="powerjsv",
    author_email="powerjsv12@gmail.com",
    url="https://github.com/powerjsv/jsv_package_test",
    install_requires=[
        "pip==23.3.1",
        "accelerate==0.25.0",
        "tqdm==4.66.1",
        "transformers==4.36.2",
        "diffusers==0.25.0",
        "einops==0.7.0",
        "bitsandbytes==0.39.0",
        "scipy==1.11.1",
        "opencv-python",
        "transformers",
        "huggingface_hub",
        "fvcore",
        "omegaconf",
        "av",
        "onnxruntime",
    ],
    packages=find_packages(exclude=[]),
    include_package_data=True,
    keywords=["vton", "powerjsv", "toy project", "pypi"],
    python_requires=">=3.10",
    package_data={"PyVirtry": ["configs/**/*"]},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
