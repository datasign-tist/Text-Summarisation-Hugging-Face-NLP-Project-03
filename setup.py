import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarisation-Project-03"
AUTHOR_USER_NAME = "AbhishekSharma"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "abhishek.kumar.sharma2697@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarization Project 03",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AbhishekSharma/Text-Summarization-Project-03",
    project_urls = {
        "Bug Tracker": "https://github.com/AbhishekSharma/Text-Summarization-Project-03/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src") )

