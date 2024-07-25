from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ipqsapi',
    version='1.0.5',
    description='API wrapper - www.ipqualityscore.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='SawaPlayGO',
    author_email='sawaglumov2006@gmail.com',
    url='https://github.com/SawaPlayGO/ipqsapi',
    install_requires=[
        'requests>=2.25.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    keywords='IPQualityScore API wrapper proxy VPN email validation phone validation. Darknet username, email, password checker.',
)