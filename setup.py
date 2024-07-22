from setuptools import setup, find_packages

setup(
    name='ipqsapi',
    version='1.0.0',
    description='API wrapper - www.ipqualityscore.com',
    long_description=open('README.md').read(),  # Длинное описание из README.md
    long_description_content_type='text/markdown',  # Формат длинного описания
    author='SawaPlayGO',  # Ваше имя
    author_email='sawaglumov2006@gmail.com',  # Ваш email
    url='',  # URL репозитория
    packages=find_packages(),  # Найти все пакеты в проекте
    install_requires=[
        'requests>=2.25.1',  # Зависимости, например requests
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Минимальная версия Python
)