from setuptools import setup
from setuptools.command.build_py import build_py
from distutils.spawn import spawn, find_executable

class Build(build_py):
    def run(self):
        spawn([find_executable('protoc'), '--python_out=.', 'protobuf/message.proto'])
        build_py.run(self)

setup(
    name='protobuf_parser',
    version='1.0.0',
    description='Разбор потока length-prefixed Protobuf сообщений на Python',
    long_description="",
    zip_safe=False,
    packages=['protobuf', 'protobuf_parser'],
    cmdclass={
        'build_py': Build
    },
)
