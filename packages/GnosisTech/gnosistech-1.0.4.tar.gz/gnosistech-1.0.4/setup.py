from setuptools import setup, find_packages
setup(
    name='GnosisTech',
    version='1.0.4',
    author='Le Minh Quan',
    author_email='leminhquan19092004@gmail.com',
    description='PyQuantTrader là một thư viện Python hỗ trợ những vấn đề về quant trading.',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ],
    python_requires='>=3.6',
)