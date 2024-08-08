from setuptools import setup, find_packages

# Function to parse requirements.txt
def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

# Read requirements from requirements.txt
install_requires = parse_requirements('src/requirements.txt')

setup(
    name='Wiggles',
    version='2.5',
    license = "MIT License with attribution requirement",
    author="Ranit Bhowmick",
    author_email='bhowmickranitking@duck.com',
    description='''This library makes signal processing easy! A great tool for students to easily visualise and test their sigals virtually. Whether you're working with continuous or discrete signals, Wiggles provides a wide range of functionalities to make signal processing straightforward and intuitive. It supports operations in both the time domain and frequency domain, including Fast Fourier Transform (FFT) and inverse FFT, and allows for easy conversion between different representations.
Wiggles is designed to be easy to use and integrate into your existing Python workflows, making it a valuable tool for engineers, researchers, and anyone interested in signal processing.''',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Kawai-Senpai/Wiggles',
    download_url='https://github.com/Kawai-Senpai/Wiggles',
    keywords=["Signal Processing",'Education','Discrete signal','Continuous signal','Basic signal operations'],
    install_requires=install_requires
)