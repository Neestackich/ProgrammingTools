import setuptools

setuptools.setup(
    name='simple-serializer',
    version='1.0',
    author='Victor Agibaylov',
    author_email='neestackich@gmail.com',
    description='Python Simple Serializer',
    url='https://github.com/Neestackich/ProgrammingTools/Python-Simple-Serializers',
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    install_requires=[
        'PyYAML==5.4.1',
        'toml==0.10.0'
    ],
)
