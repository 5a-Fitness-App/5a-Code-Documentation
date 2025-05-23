# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'FitFish App Documentation'
copyright = '2025, 5a'
author = 'Team 5A'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output



# Path to static files



html_logo = '_static/Logo.png'

html_context = {
    "display_github": False,
}


html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': True,
    
}

#html_sidebars = {
 #   '**': [
 #       'globaltoc.html',
 #       'relations.html',
 #       'searchbox.html',
 #  ]
#}

def setup(app):
    app.add_css_file("custom.css")

# -- Options for EPUB output
epub_show_urls = 'footnote'
