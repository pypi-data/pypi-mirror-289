from setuptools import setup, find_packages

setup(
    name='llmassist',
    version='0.1.0',
    description='A easy assist package for Large Language model inference and fine-tuning.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yinghao Li',
    author_email='shiyi.yinghao@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.11',
)

