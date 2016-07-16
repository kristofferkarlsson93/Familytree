#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*- 
import cgi, cgitb
import sys
cgitb.enable()
from familybasefile import Familybase
from mainpagefile import Mainpage
""" Takes in table_name and index and sends it to Familybase-class and the 
funktion delete_person which deletes it and then sends the user to Mainpage """

form = cgi.FieldStorage()
table_name = str(form.getvalue("table_name"))
ident = int(form.getvalue("ident"))
fambase = Familybase(table_name)
fambase.delete_person(ident)
page = Mainpage(table_name)
page.build_page()