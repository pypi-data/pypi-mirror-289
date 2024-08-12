from setuptools import setup, find_packages

setup(
    name='hamlang',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hamlang=hamlang.__main__:main'
        ]
    },
    author='HshMaker',
    author_email='hshmakerss@gmail.com',
    description="그냥 히읗이 많이 들어간 언어입니다.",
    long_description=open("./README.md", "r", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HshMaker/hamlang",
    keywords=['hamlang', 'hshmaker', 'Esolang'],
    python_requires='>=3.6',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)