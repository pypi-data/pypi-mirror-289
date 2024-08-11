import os,sys
from setuptools import setup
from pkg_resources import require, DistributionNotFound, VersionConflict

try:
    require('pytest-allure-adaptor')
    print("""
    You have pytest-allure-adaptor installed.
    You need to remove pytest-allure-adaptor from your site-packages
    before installing allure-pytest-il, or conflicts may result.
    """)
    sys.exit()
except (DistributionNotFound, VersionConflict):
    pass

PACKAGE = "allure-pytest-il"

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Framework :: Pytest',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Software Development :: Testing',
    'Programming Language :: Python :: 3.8',
]

setup_requires = [
    "setuptools_scm"
]


install_requires = [
    "pytest>=4.5.0"
]


def prepare_version():
    from setuptools_scm import get_version
    configuration = {"root": "..",  "relative_to": __file__}
    version = get_version(**configuration)
    install_requires.append(f"allure-python-commons=={version}")
    return configuration


def get_readme(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def main():
    setup(
        name=PACKAGE,
        # use_scm_version=prepare_version,
        dynamic = ["version"],
        description="Allure pytest integration",
        url="https://allurereport.org/",
        project_urls={
            "Documentation": "https://allurereport.org/docs/pytest/",
            "Source": "https://github.com/allure-framework/allure-python",
        },
        author="Qameta Software Inc., Stanislav Seliverstov",
        author_email="sseliverstov@qameta.io",
        license="Apache-2.0",
        classifiers=classifiers,
        keywords="allure reporting pytest",
        long_description=get_readme("README.md"),
        long_description_content_type="text/markdown",
        packages=["allure_pytest_il"],
        package_dir={"allure_pytest_il": "src"},
        entry_points={"pytest11": ["allure_pytest_il = allure_pytest_il.plugin"]},
        setup_requires=setup_requires,
        install_requires=install_requires
    )

if __name__ == '__main__':
    main()

