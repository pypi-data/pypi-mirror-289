from setuptools import setup, find_packages

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setup(
    name="slack_progress_bar_kjh",
    version="1.0.6",
    author="jaehyeong.kim",
    author_email="rlawogud970301@gmail.com",
    description="Modify from Michael Lizzi's slack_progress_bar. Thank you.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JaeHeong/slack-progress-bar_kjh",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=["slack_sdk"],
)
