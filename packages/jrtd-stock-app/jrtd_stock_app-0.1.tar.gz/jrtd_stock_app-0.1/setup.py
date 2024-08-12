from setuptools import setup, find_packages

setup(
    name='jrtd_stock_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'yfinance',
        'matplotlib',
        'seaborn',
        'mplfinance',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'stockplot=enhanced_stock_visualization:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to visualize stock data with enhanced charts',
    url='https://github.com/yourusername/my_stock_app',  # Update this with your actual repo URL
)
