import setuptools

with open('README.md', encoding='utf-8') as f:  # README.md 내용 읽어오기
    long_description = f.read()

setuptools.setup(
    name="goatfarm",
    version="0.0.1",
    license='MIT License',
    author="tonythefreedom",
    author_email="tonymustbegreat@gmail.com",
    long_description_content_type = 'text/markdown',
    description="TBD",
    long_description=long_description,
    url="https://github.com/tonythefreedom/goatfarm",
    zip_safe = False,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)