# -*- coding: utf-8 -*-
"""
	Kingpin Accounts
"""

from kingpinaccounts.modules.control import addonPath, addonVersion, joinPath
from kingpinaccounts.windows.textviewer import TextViewerXML

def get(file):
	kingpinaccounts_path = addonPath()
	kingpinaccounts_version = addonVersion()
	helpFile = joinPath(kingpinaccounts_path, 'lib', 'kingpinaccounts', 'help', file + '.txt')
	r = open(helpFile, 'r', encoding='utf-8', errors='ignore')
	text = r.read()
	r.close()
	heading = '[B]Kingpin Accounts -  v%s - %s[/B]' % (kingpinaccounts_version, file)
	windows = TextViewerXML('textviewer.xml', kingpinaccounts_path, heading=heading, text=text)
	windows.run()
	del windows