from setuptools import setup, find_packages



VERSION = '1.1.0'
DESCRIPTION = 'Package to convert lowerr case to upper case letter'
# LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

# Setting up
setup(
    name="upper_102218038",
    version=VERSION,
    author="thebrownkidd",
    author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    # long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'text', 'paragraph', 'lower case', 'upper case', 'string'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)