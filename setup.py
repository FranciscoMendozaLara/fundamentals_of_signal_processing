from setuptools import setup, find_packages

setup(
    name="signal_processing_course",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "pywavelets",
        "librosa"
    ],
    author="Carlos Francisco Mendoza Lara",
    description="A course on signal processing fundamentals with Python examples.",
)
