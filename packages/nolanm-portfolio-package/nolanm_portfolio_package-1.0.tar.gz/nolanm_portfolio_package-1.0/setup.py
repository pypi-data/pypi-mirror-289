from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt', 'r', encoding='utf-8') as req_file:
        return [line.strip() for line in req_file if line.strip()]


setup(
    name='nolanm_portfolio_package',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'setup-env=nolanm_portfolio_package.setup:main',
        ],
    },
)
