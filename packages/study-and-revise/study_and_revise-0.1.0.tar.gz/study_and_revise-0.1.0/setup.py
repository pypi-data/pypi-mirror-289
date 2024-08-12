from setuptools import setup, find_packages

setup(
    name='study_and_revise',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'review=review.sr:main',  # 命令行入口
        ],
    },
    author='txs',
    description='查看复习项目',
    license='GPLv3',
    python_requires='>=3.0',  # Python 版本要求
)
