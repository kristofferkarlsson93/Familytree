#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*- 
import cgi, cgitb
from firstpagefile import Firstpage

"""Creates the initial webpage by calling the Firstpage-class"""

page = Firstpage()
page.build_page()