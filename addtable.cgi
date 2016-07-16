#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*- 
import cgi, cgitb
from mainpagefile import Mainpage
from familybasefile import Familybase
cgitb.enable()

"""Puts in the familyname in a table and creates a new table for the family if
it do not exists. It then build the Mainpage - wich is the page the user uses 
the most"""

form = cgi.FieldStorage()
table_name = str(form.getvalue('tree_name'))
fambase = Familybase(table_name)
fambase.create_family_table()
page = Mainpage(table_name)
page.build_page()