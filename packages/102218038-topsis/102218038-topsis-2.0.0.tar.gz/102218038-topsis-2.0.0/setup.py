from setuptools import setup, find_packages



VERSION = '2.0.0'
DESCRIPTION = 'Runs topsis algorythm for pre trained models'
# LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

# Setting up
setup(
    name="102218038-topsis",
    version=VERSION,
    author="thebrownkidd",
    description=DESCRIPTION,
    # long_description_content_type="text/markdown",
    # long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas','numpy'],
    keywords=['python', 'topsis', 'machine learning'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)