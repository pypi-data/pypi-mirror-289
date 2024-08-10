import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='BuckTheDuck',
    version='0.0.4',
    author='Yoav Alroy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(exclude=('test', 'test.*')),
    author_email="yoavalro@gmail.com",
    license="MIT",
    entry_points={
        "console_scripts": [
            "buck=BuckTheDuck.__main__:main",
        ]
    },
    install_requires=["setuptools", "importlib_resources", "pygit2", "unidiff", "google-generativeai", "IPython",
                      "throttle", "openai", "py_mini_racer"],
    keywords=['GIT', 'GENAI', 'AUTOMATION', 'CLI'],
    python_requires='>=3.9'
)
