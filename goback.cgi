#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*- 
import cgi, cgitb
import sys
cgitb
from mainpagefile import Mainpage
""" Redirect the user to the Mainpage """

form = cgi.FieldStorage()
table_name = str(form.getvalue("table_name"))
webpage = Mainpage(table_name)
webpage.build_page()