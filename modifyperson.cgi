#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*- 
import cgi, cgitb
import sys
cgitb.enable()
from familybasefile import Familybase
from mainpagefile import Mainpage
from personfile import Person
""" Takes in the person info and creates a person-object wich is being sent to
Familybase and uses the function modify_person wich modifyes it."""

form = cgi.FieldStorage()
table_name = str(form.getvalue('tree_name'))
ident = int(form.getvalue('ident'))
firstname = str(form.getvalue('firstname'))
lastname = str(form.getvalue('lastname'))
born = str(form.getvalue('born'))
death = str(form.getvalue('death'))
mother_id = int(form.getvalue('mother_id'))
father_id = int(form.getvalue('father_id'))
comment = str(form.getvalue('comment'))
person = Person(firstname, lastname, born, death, mother_id, father_id, comment)

fambase = Familybase(table_name)
fambase.modify_person(person, ident)

mainpage = Mainpage(table_name)
mainpage.build_page()