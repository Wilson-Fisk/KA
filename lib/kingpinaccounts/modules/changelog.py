# -*- coding: utf-8 -*-
"""
	Kingpin Accounts
"""

from kingpinaccounts.modules.control import addonPath, addonVersion, joinPath
from kingpinaccounts.windows.textviewer import TextViewerXML


def get():
	kingpinaccounts_path = addonPath()
	kingpinaccounts_version = addonVersion()
	changelogfile = joinPath(kingpinaccounts_path, 'changelog.txt')
	r = open(changelogfile, 'r', encoding='utf-8', errors='ignore')
	text = r.read()
	r.close()
	heading = '[B]Kingpin Accounts -  v%s - ChangeLog[/B]' % kingpinaccounts_version
	windows = TextViewerXML('textviewer.xml', kingpinaccounts_path, heading=heading, text=text)
	windows.run()
	del windows