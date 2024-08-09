from setuptools import setup, find_packages

setup(
    name='informatikunterricht',
    version='0.1.3',
    author='Henning Mattes',
    author_email='henning_mattes@gmx.de',
    description='Ein Paket für den Informatikunterricht, das Module zur Bildverarbeitung und Diagrammerstellung enthält.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/IhrGitHub/informatikunterricht',
    packages=find_packages(),
    install_requires=[
        'matplotlib',  # Da beide Module matplotlib verwenden, nehmen wir es in die Installationsanforderungen auf.
        'numpy',       # Wenn bildverarbeitung NumPy verwendet.
        'Pillow'       # Wenn bildverarbeitung PIL/Pillow verwendet.
    ],
    license='MIT with additional terms',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Education',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='bildung informatik bildverarbeitung diagramme informatikunterricht',
    package_data={
        '': ['LICENSE.txt', 'README.md', 'csedu_package_img_small.png']
    },
    include_package_data=True,
    python_requires='>=3.7',
)
