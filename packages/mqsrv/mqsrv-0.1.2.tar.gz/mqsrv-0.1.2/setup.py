from setuptools import setup, find_packages

setup(
    name='mqsrv',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'greenthread>=0.1.1',
        'kombu>=5.1',
        'tblib>=3.0',
        'jsonpickle>=3.0',
        'msgpack-python',
        'msgpack-numpy',
        'loguru>=0.5',
    ],
    include_package_data=True,
    description='A message queue-based RPC and event publish/subscribe system.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tsinghtech/mqsrv',
    author='daleydeng',
    author_email='daleydeng@qingtong123.com',
    license='MIT',
)