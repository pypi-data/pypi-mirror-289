from setuptools import setup, find_packages

setup(
    name='total_netwk',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'networkx',
    ],
    description='A package for network analysis and community detection',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Gongruihao',
    author_email='202031200039@mail.bnu.edu.cn',
    
    license='MIT',  # 或者你选择的其他许可证
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
)
