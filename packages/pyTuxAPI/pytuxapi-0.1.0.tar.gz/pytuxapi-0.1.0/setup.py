from setuptools import setup, find_packages

setup(
    name='pyTuxAPI',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Перечислите зависимости вашего пакета здесь
    ],
    description='Python client for the TuxAPI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ваше Имя',
    author_email='ваш.email@example.com',
    url='https://github.com/ваш-репозиторий/pyTuxAPI',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
