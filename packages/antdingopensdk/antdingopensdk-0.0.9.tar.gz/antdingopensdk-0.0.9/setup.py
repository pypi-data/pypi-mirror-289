import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="antdingopensdk",
    version="0.0.9",
    author="alipay ant ding open",
    # url='xxx',
    # author_email="xxx",
    description="alipay ant ding open sdk for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)