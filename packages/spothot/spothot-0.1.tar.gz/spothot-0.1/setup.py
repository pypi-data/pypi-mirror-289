from setuptools import setup, find_packages

setup(
    name='spothot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'spothot=spothot.main:main',
        ],
    },
    author='Shadan',
    author_email='shadankhantech@gmail.com',
    description='Spothot is a Python package designed to transform a Raspberry Pi into a Wi-Fi hotspot with an easy-to-use Flask web interface. Users can configure the hotspot and connect to available Wi-Fi networks directly through the web interface. Ideal for creating a portable Wi-Fi solution or for network testing purposes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/skshadan/SpotHot',  # Replace with your GitHub repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
