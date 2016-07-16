#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*- 
import cgi, cgitb
import sys
from detailpagefile import Detailpage
cgitb.enable()
""" Creates the webpage Detailpage """

detailpage = Detailpage()
detailpage.build_page()