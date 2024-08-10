from setuptools import setup, find_packages

setup(
    name='mobile_automation_library',
    version='0.1',
    description='Uma biblioteca para automação mobile com Robot Framework',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Tiago Dias',
    author_email='tiagooliveira.qa@gmail.com',
    url='https://github.com/Skisperd/libray_robotframework',
    packages=find_packages(),
    install_requires=[
        'robotframework',
        'Appium-Python-Client',
        'robotframework-appiumlibrary'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Robot Framework',
    ],
    python_requires='>=3.6',
)
