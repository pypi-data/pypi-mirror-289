from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="tictactoelibrary",
    version="0.0.1",
    author="Amos Xiao",
    author_email="AmosXiao1000020@proton.me",
    description="Python Tic-Tac-Toe Library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/your-repo",
    packages=find_packages(),
    classifiers=[],
    python_requires='>=3.10',
)
