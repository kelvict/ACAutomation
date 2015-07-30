__author__ = 'ding'
from distutils.core import setup, Extension


setup(
    name="ACAutomation",
    description="ACAutomation python wrapper,support unicode",
    author="Yaguang Ding",
    author_email="dingyaguang117@gmail.com",
    url="http://github.coom/dingyaguang117",
    packages=['ACAutomation'],
    ext_modules = [
        Extension("_ACAutomation", sources=['ACAutomation/wrapper.cpp', 'ACAutomation/_ACAutomation.cpp'])
    ],
    keywords='ac-automation ac automation',
    version='0.2'

)