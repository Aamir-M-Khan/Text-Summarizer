import setuptools

# Read the README file for the long description of the package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package metadata
__version__ = "0.0.0"  # Version number of the package
REPO_NAME = "Text-Summarizer-Project"  # Name of the GitHub repository
AUTHOR_USER_NAME = "Aamir-M-Khan"  # GitHub username of the package author
SRC_REPO = "TextSummarizer"  # Name of the source repository
AUTHOR_EMAIL = "aamir11amu@gmail.com"  # Email of the package author

# Setup configuration for the package
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",  # Description of the package
    long_description=long_description,  # Detailed description from README file
    long_description_content="text/markdown",  # Type of content in long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL of the GitHub repository
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # URL for bug tracking
    },
    package_dir={"": "src"},  # Package directory
    packages=setuptools.find_packages(where="src")  # Find all packages in "src" directory
)
