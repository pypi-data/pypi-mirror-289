from setuptools import setup, find_packages

setup(
    name='modelmaster',
    version='0.1.0',
    description='A Model Management package for model archive including upload and download from AWS S3 and Huggingface Hub.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yinghao Li',
    author_email='shiyi.yinghao@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.11',
)

