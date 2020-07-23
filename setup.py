import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="alectio",
    version="0.1",
    author="Alectio",
    author_email="admin@alectio.com",
    description="Alectio Python CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://alectio.com",
    packages=setuptools.find_packages(),
    install_requires=["requests>=2", "gql", "keras", "opencv-python", "asyncio", "aiogqlc"],
    classifiers=[
        'Development Status :: 3 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=["alectio"],
)