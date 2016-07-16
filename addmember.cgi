#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*-
import cgi, cgitb
from mainpagefile import Mainpage
from familybasefile import Familybase
from personfile import Person
cgitb.enable()
"""Imports the users input and creats a person object with the person-class. 
The object is being sent to the database in the Familybase-class. Then the
webpage is being created with updated info."""

form = cgi.FieldStorage()
table_name = str(form.getvalue('tree_name'))
firstname = str(form.getvalue('firstname'))
lastname = str(form.getvalue('lastname'))
born = str(form.getvalue('born'))
death = str(form.getvalue('death'))
mother_id = int(form.getvalue('mother_id'))
father_id = int(form.getvalue('father_id'))
comment = str(form.getvalue('comment'))
person = Person(firstname, lastname, born, death, mother_id, father_id, comment)
fambase = Familybase(table_name)
fambase.enter_familymember(person)
page = Mainpage(table_name)
page.build_page()