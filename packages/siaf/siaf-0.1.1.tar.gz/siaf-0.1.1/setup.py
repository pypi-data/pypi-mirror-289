from setuptools import setup, find_packages  

setup(  
    name='siaf',  
    version='0.1.1',    
    packages=find_packages(),    
    install_requires=[
        'numpy>=1.26.4',
        'pandas>=2.2.2',  
        'matplotlib>=3.8.0', 
        'omegaconf>=2.3.0',
        'vrplib>=1.4.0',
        'pyDOE2>=1.3.0'
    ],  
    author='alex',  
    author_email='lsj178@139.com',  
    description='Swarm Intelligence Algorithm Framework',  
    long_description=open('README.md').read(),    
    long_description_content_type='text/markdown',  
    url='https://github.com/lshengjian/siaf',    
    classifiers=[  
        'Programming Language :: Python :: 3',  
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',  
    ],  
    python_requires='>=3.8',  
)