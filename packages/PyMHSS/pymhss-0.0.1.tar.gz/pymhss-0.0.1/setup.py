from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Metropolis-Hastings with Scalable Subsampling'

# Setting up
setup(
        name="PyMHSS", 
        version=VERSION,
        author="Estevao Prado, Christopher Nemeth, Chris Sherlock",
        author_email="<e.prado1@lancaster.ac.uk>",
        description=DESCRIPTION,
        readme = "README.md",
        packages=find_packages(),
        install_requires=['time', 'numpy', 'tqdm', 'statsmodels', 'scipy', 'tensorflow', 'pickle'], 
        keywords=['Python package', 'Metropolis-Hastings with Scalable Subsampling', 'Tuna Metropolis-Hastings algorithm', 'Scalable Metropolis-Hastings'],
        python_requires=">=3.9.6",
        project_urls={
            "Paper": "https://arxiv.org/pdf/2407.19602",
            "GitHub": "https://github.com/ebprado/MH-with-scalable-subsampling",
    },
)
