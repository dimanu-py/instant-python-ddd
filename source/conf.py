# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'python-skeleton'
copyright = '2025, dimanu-py'
author = 'dimanu-py'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'myst_parser', 'sphinx.ext.napoleon', 'sphinx_wagtail_theme']

html_theme = 'sphinx_wagtail_theme'

html_theme_options = dict(
	project_name = 'Instant Boilerplate for Python Projects',
	logo = 'img/thunder.svg',
	logo_alt = '⚡️',
	github_url = 'https://github.com/dimanu-py/python-skeleton/docs',
	html_show_sphinx = False,
)

html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = []
