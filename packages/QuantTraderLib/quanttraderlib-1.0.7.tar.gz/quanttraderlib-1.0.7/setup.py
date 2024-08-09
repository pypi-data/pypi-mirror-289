from setuptools import setup, find_packages
setup(
    name='QuantTraderLib',
    version='1.0.7',
    author='Le Minh Quan',
    author_email='leminhquan19092004@gmail.com',
    description='PyQuantTrader là một thư viện Python hỗ trợ những vấn đề về quant trading.',
    url='https://github.com/Gnosis-Tech/PyQuantTrader_Dev',  # Project homepage URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add any dependencies your package needs here
    ],
)