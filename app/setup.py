from setuptools import setup, find_namespace_packages

setup(
	name="magneto.app",
    version="1.0",
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    zip_safe=True,

	# Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    #install_requires=['docutils>=0.3'],
	setup_requires=["pytest-runner"],
    tests_require=["pytest","pytest-cov"],
    )