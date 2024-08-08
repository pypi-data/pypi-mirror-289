from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='my_custom_messagebox',
    version='1.2.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Pillow',
    ],
    description='A custom messagebox package for Tkinter applications.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dean',
    author_email='s770207@yahoo.com.tw',
    url='https://your.url.here',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
