import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ytube_data_and_transcript",  # Replace with your package name
    version="0.1.0",
    author="Devansh Lingamaneni",
    author_email="l.devansh2073@gmail.com",
    description="A python package that utilizes the YouTube Data V3 API to get all transcripts from a given channel/playlist.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DevanshL/youtube-channel-transcript-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.32.3',
        'google-api-python-client>=2.138.0',
        'youtube-transcript-api>=0.6.2',
    ],
)