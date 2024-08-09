from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='linex2',
    version='1.1.15',

    description='Lipid Network Explorer 2 (LINEX2) package. Python backend to the LINEX web-app',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://exbio.wzw.tum.de/linex/',
    project_urls={  # Optional
        'Source': 'https://gitlab.lrz.de/lipitum-projects/linex2_package',
        'Publication': "https://doi.org/10.1093/bib/bbac572"
    },

    author="Tim Daniel Rose, Nikolai Koehler, Olga Lazareva, Josch Konstantin Pauling",
    author_email="tim.rose@tum.de, nikolai.koehler@tum.de",

    license='AGPLv3',

    packages=find_packages(),
    install_requires=['networkx', "pandas", "matplotlib", "numpy", "pyvis",
                      "scikit-learn", "statsmodels", "jinja2", "seaborn"],
    python_requires=">=3.8",

    package_data={'linex2': ["templates/vis_main.html",
                                 "templates/vis_dynamic.html",
                                 "templates/lipid_colours.json",
                                 "data/*.csv", "data/*.txt"]},
    zip_safe=False,


    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3"

    ]
)
