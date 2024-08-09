from setuptools import setup, find_packages

setup(
    name='cwpytube',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pytube>=10.9.3',
        'moviepy>=1.0.3',
    ],
    author='Zied Boughdir',
    author_email='Ziedboughdir@gmail.com',
    description='For download and convert YouTube videos into multi format and watch videos.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zinzied/Convert-Watch-Youtube-Lib/',  # Trailing slash added
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)