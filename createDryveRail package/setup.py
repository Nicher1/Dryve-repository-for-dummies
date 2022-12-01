import setuptools
try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()
setuptools.setup(
    name="createdryverail",
    version="2.5.6",
    author="Nichlas Overgaard Laugesen, Elias Thomassen Dam",
    description="Dryve D1 script created by 2 undergraduate robotic students of Aalborg University",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["createdryverail"],
    url="https://github.com/Nicher1/Dryve-repository-for-dummies.git",
    licence="MIT",
    keywords='robotics DryveD1 Python Script Rail Create',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    project_urls={
        'Documentation': 'https://github.com/Nicher1/Dryve-repository-for-dummies/blob/main/createDryveRail%20package/How%20to%20control%20the%20Dryve%20D1%20over%20Python.pdf',
        'Source': 'https://github.com/Nicher1/Dryve-repository-for-dummies',
        'Tracker': 'https://github.com/Nicher1/Dryve-repository-for-dummies/issues',
    },
    install_requires=['sockets'],
    python_requires='>=3.6,==3.*',
    package_data={
        'Guide': ['How to control the Create Rail over Dryve D1 over Python.pdf'],
    },
)
