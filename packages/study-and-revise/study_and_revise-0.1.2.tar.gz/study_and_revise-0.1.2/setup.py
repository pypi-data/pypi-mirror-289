from setuptools import setup, find_packages

setup(
    name='study_and_revise',
    version='0.1.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'review=study_and_revise.sr:main',  # 命令行入口
        ],
    },
    author='txs',
    description='查看复习项目',
    long_description=open('README.md', encoding="utf-8").read(),  # 从 README.md 中读取长描述
    long_description_content_type='text/markdown',  # 长描述的格式
    license='GPLv3',
    python_requires='>=3.0',  # Python 版本要求
)
