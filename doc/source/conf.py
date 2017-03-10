# -*- coding: utf-8 -*-
#
# RTD-example documentation build configuration file, created by
# sphinx-quickstart on Fri Mar 10 14:49:28 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import subprocess, sys
from os.path import abspath, join
from os import listdir, mkdir
import pip

pip.main(['install', 'breathe'])

def __mkdir(path):
    try:
        mkdir(path)
    except OSError:
        pass  # directory exists, just carry on


'''
documentation root path: /home/me/docproj/
breathe path: /home/me/docproj/ext/breathe/
doxygen xml output: /home/me/docproj/doxyxml/
'''

project_source_dir = abspath(join('..', '..', 'src'))
doc_root_dir = abspath('..')
doxygen_dir = join(doc_root_dir, 'doxygen')
__mkdir(doxygen_dir)
breathe_dir = join(doc_root_dir, 'breathe')
__mkdir(breathe_dir)
doxygen_xml_dir = join(doxygen_dir, 'xml')

sys.path.append( breathe_dir )
breathe_projects = { "rtd-example-breathe": doxygen_xml_dir }
breathe_default_project = "rtd-example-breathe"


my_doxygen_xml_dir = None

def __run_doxygen(working_dir, doxyfile):
    """Run the doxygen make command in the designated folder"""

    try:
        ret = subprocess.call('doxygen {}'.format(doxyfile), cwd=working_dir, shell=True)
        if ret != 0:
            sys.stderr.write('doxygen terminated by signal {}\n'.format(ret))
    except OSError as e:
        sys.stderr.write('doxygen execution failed: {}'.format(e))


def __parse_doxyfile(doxyfile_in, doxyfile):
    with open(doxyfile_in, 'r') as _doxyfile_in:
        conf = _doxyfile_in.read()

    conf = conf.replace('@doxy_main_page@', ' ')
    global project_source_dir
    conf = conf.replace('@PROJECT_SOURCE_DIR@', project_source_dir)
    conf = conf.replace('@PROJECT_BINARY_DIR@', ' ')

    with open(doxyfile, 'w') as _doxyfile:
        _doxyfile.write(conf)


def __generate_doxygen_xml(app):
    """Run the doxygen make commands if we're on the ReadTheDocs server"""

    read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

    if read_the_docs_build:
        global doc_root_dir, doxygen_dir
        doxyfile = join(doxygen_dir, 'Doxyfile')
        print('>>>>> ddd BEFORE {} is doxygen_dir\n\t{}\n'.format(doxygen_dir, listdir(doxygen_dir)))
        __parse_doxyfile(join(doc_root_dir, 'Doxyfile.in'), doxyfile)
        print('>>>>> DDD AFTER {} is doxygen_dir\n\t{}\n'.format(doxygen_dir, listdir(doxygen_dir)))
        __run_doxygen(doxygen_dir, doxyfile)
        try:
            ret = subprocess.call('ls -alh', cwd=doxygen_xml_dir, shell=True)
            if ret != 0:
                sys.stderr.write('cannot list {} with error {}\n'.format(doxygen_xml_dir, ret))
        except OSError as e:
            sys.stderr.write('listing of {} failed: {}'.format(doxygen_xml_dir, e))



def setup(app):

    # Add hook for building doxygen xml when needed
    app.connect("builder-inited", __generate_doxygen_xml)

print('>>>>> {} is my_doxygen_xml_dir\n'.format(my_doxygen_xml_dir))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'breathe']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'RTD-example'
copyright = u'2017, Dzhoshkun Ismail Shakir, Another One'
author = u'Dzhoshkun Ismail Shakir, Another One'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'RTD-exampledoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'RTD-example.tex', u'RTD-example Documentation',
     u'Dzhoshkun Ismail Shakir, Another One', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'rtd-example', u'RTD-example Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'RTD-example', u'RTD-example Documentation',
     author, 'RTD-example', 'One line description of project.',
     'Miscellaneous'),
]



