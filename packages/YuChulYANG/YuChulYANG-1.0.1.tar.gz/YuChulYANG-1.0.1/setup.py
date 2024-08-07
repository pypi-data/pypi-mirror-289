import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="YuChulYANG", # Replace with your own username
    version="1.0.1",
    author="YuChul YANG",
    author_email="yuchulyang@naver.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pipy.org/project/YuChulYANG/",
    packages=setuptools.find_packages(),
#    classifiers=[
#        "Programming Language :: Python :: 3",
#        "License :: ",
#        "Operating System :: OS",
#    ],
#    python_requires='>=3.6',
)
