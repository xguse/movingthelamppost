# -*- coding: utf-8 -*-
import sys, os
import tinkerer
import tinkerer.paths        


# adds local extension directory to python path
sys.path.append(os.path.abspath('ext'))


# **************************************************************
# TODO: Edit the lines below
# **************************************************************

# Change this to the name of your blog
project = "moving the lamppost"                   

# Change this to the tagline of your blog
tagline = 'random musings of a molecular biologist turned code jockey in the era of big data and open science.'                  

# Change this to the description of your blog
description = tagline

# Change this to your name
author = 'W Augustine Dunn'

# Change this to your copyright string
copyright = '2013, ' + author         

# Change this to your blog root URL (required for RSS feed)
website = 'http://movingthelamppost.com/blog/html/'                              

# **************************************************************
# More tweaks you can do
# **************************************************************

# Add your Disqus shortname to enable comments powered by Disqus
disqus_shortname = 'movingthelamppost'

# Change your favicon (new favicon goes in _static directory)
html_favicon = 'tinkerer.ico'           

# Pick another Tinkerer theme or use your own
html_theme = "flat_enhanced_dark_pastel"

# Theme-specific options, see docs
html_theme_options = { }                                  

# Link to RSS service like FeedBurner if any, otherwise feed is
# linked directly
rss_service = "http://feeds.feedburner.com/MovingTheLamppost"
rss_generate_full_posts = True

# Number of blog posts per page
posts_per_page = 5

# **************************************************************
# Edit lines below to further customize Sphinx build
# **************************************************************

# Configure sphinx-natbib
#natbib = {file:'_static/bib/zzzz.bib'}


# Add other Sphinx extensions here

sys.path.append(os.path.abspath('ext'))
sys.path.append(os.path.abspath('sphinxext'))

extensions = [	'ipython_directive',
		'ipython_console_highlighting',
		'sphinxcontrib.youtube',
		'tinkerer.ext.blog',
		'tinkerer.ext.disqus',
		'sphinx.ext.mathjax', ] 

# Add other template paths here
templates_path = ['_templates']

# Add other static paths here
html_static_path = ['_static', tinkerer.paths.static]

# Add other theme paths here
html_theme_path = ['_themes', tinkerer.paths.themes]                 

# Add file patterns to exclude from build
exclude_patterns = ["drafts/*", "_templates/*"]

# Add templates to be rendered in sidebar here
html_sidebars = {
	"**": ["email_subscribe.html","searchbox.html","categories.html","tags_cloud.html"]
}

# choose which pygments style to use for code highlighting
pygments_style = 'solarizedlight'


# **************************************************************
# Do not modify below lines as the values are required by 
# Tinkerer to play nice with Sphinx
# **************************************************************

source_suffix = tinkerer.source_suffix
master_doc = tinkerer.master_doc
version = tinkerer.__version__
release = tinkerer.__version__
html_title = project
html_use_index = False
html_show_sourcelink = False
html_add_permalinks = None
