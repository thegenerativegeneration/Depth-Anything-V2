from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="depth-anythingV2",
    version="0.1.0",
    author="DepthAnything",
    author_email="author@example.com",  # Replace with actual author email
    description="Depth Anything V2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thegenerativegeneration/Depth-Anything-V2",  # Replace with actual URL
    packages=["depth_anything_v2", "depth_anything_v2.util", "depth_anything_v2.dinov2_layers"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "opencv-python-headless==4.8.0.74",
        "torch",
        "torchvision",
        "matplotlib",
    ],
    include_package_data=True,
)