from setuptools import setup, find_packages

setup(
    name='extract_moodle',
    version='0.1.1',
    description='A tool to extract Moodle files and organize them based on questions.',
    author='Your Name',
    author_email='your_email@example.com',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your package needs here
    ],
    entry_points={
        'console_scripts': [
            'extract_moodle=extract_moodle.main:wrapper',  # Point to the wrapper function
        ],
    },
    python_requires='>=3.6',  # Specify the Python version requirement
)
