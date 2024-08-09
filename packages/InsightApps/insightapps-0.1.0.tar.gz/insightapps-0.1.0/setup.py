from setuptools import setup, find_packages
import os

def build_frontend():
    os.system('cd InsightApps && npm install && ng build --prod')

build_frontend()

setup(
    name='InsightApps',
    version='0.1.0',
    description='A Django backend with an Angular frontend',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Rajashekar',
    author_email='rajashekarreddypr24@gmail.com',
    url='https://github.com/yourusername/your-repo',
    packages=find_packages(where='Project'),
    package_dir={'': 'Project'},
    include_package_data=True,  # Ensure that static files are included
    install_requires=[
        'django',
        # Add other Python dependencies
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
