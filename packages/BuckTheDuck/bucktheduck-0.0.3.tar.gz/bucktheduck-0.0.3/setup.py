import setuptools

setuptools.setup(
    name='BuckTheDuck',
    version='0.0.3',
    author='Yoav Alroy',
    description='This package will help you have more meaningful commit messages',
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
