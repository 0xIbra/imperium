import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='imperium',
    version='0.0.5',
    author='Ibragim Abubakarov',
    author_email='ibragim.ai95@gmail.com',
    description='Imperium is a micro python package that allows you to easily evaluate conditional expressions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ibragim64/imperium',
    packages=['imperium'],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)