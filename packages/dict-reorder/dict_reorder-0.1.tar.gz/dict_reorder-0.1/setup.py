from setuptools import setup
import dict_reorder

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="dict-reorder",
    version=dict_reorder.__version__,
    description=dict_reorder.__description__,
    long_description=readme,
    long_description_content_type="text/markdown",
    author=dict_reorder.__author__,
    maintainer=dict_reorder.__author__,
    url="https://github.com/xyzpw/dict-reorder/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],
    keywords=[
        "dictionaries",
        "manipulator",
    ],
    license=dict_reorder.__license__,
)
