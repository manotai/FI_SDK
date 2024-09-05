from setuptools import setup, find_packages

setup(
    name="feedbackIntelligence",
    version="0.1.5",
    author="Tigran Kostanyan",
    author_email="tigran@manot.ai",
    description="An SDK for Feedback Intelligence data insertion",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
