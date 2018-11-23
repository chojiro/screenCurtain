# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "screenCurtain",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Screen Curtain"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""Proof of concept implementation of screen curtain (NVDA Core issue 7857)"""),
	# version
	"addon_version" : "18.08",
	# Author(s)
	"addon_author" : u"Babbage B.V., Joseph Lee <joseph.lee22590@gmail.com>",
	# URL for the add-on documentation support
	"addon_url" : "https://addons.nvda-project.org/",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported
	"addon_minimumNVDAVersion" : "2018.2",
	# Last NVDA version supported/tested
	"addon_lastTestedNVDAVersion" : "2019.1",
	# Minimum Windows version supported
	"addon_minimumWindowsVersion" : "6.2.9200",
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "*.py"),
os.path.join("addon", "appModules", "*.py"),
os.path.join("addon", "globalPlugins", "wintenObjs", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
