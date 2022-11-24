import setuptools
try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()
setuptools.setup(
    name="Create Drive Rail",
    version="1.0.0",
    author="Nichlas Overgaard Laugesen, Elias Thomassen Dam",
    description="Dryve D1 script created by 2 undergraduate robotic students of Aalborg University",
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=["createdriverail"],
    url="https://github.com/Nicher1/Dryve-repository-for-dummies.git",
    licence="Mozilla Public License",
    keywords='robotics DryveD1 Python Script Rail Create',
    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers/Robotic students at AAU Create',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Mozilla Public License',
        'programming Language :: Python :: 3.11',
    ],
    project_urls={
        'Documentation': 'https://github.com/Nicher1/Dryve-repository-for-dummies',
        'Source': 'https://github.com/Nicher1/Dryve-repository-for-dummies',
        'Tracker': 'https://github.com/Nicher1/Dryve-repository-for-dummies/issues',
    },
    install_requires=['socket'],
    python_requires='>=3.6',
    package_data={
        'Guide': ['How to control the Create Rail over Dryve D1 over Python.pdf'],
    },
)
