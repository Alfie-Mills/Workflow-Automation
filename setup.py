from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'workflow-automation',
    version = '0.0.1',
    author = 'Alfie Mills',
    author_email = 'me@alfiemills.co.uk',
    license = 'gpl-3.0',
    description = 'A tool for automating web development workflow.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/Alfie-Mills/Workflow-Automation',
    packages=['app'],
    install_requires = [requirements],
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        wa=app.main:cli
    '''
)