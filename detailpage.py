# -*- coding: iso-8859-1 -*- 
from familybasefile import Familybase

class Firstpage:
    
    def __init__(self):
        pass
        
    def build_page(self):
        self.build_head()
        self.build_body()
        self.close_script()
    
    def build_head(self):
        print ('Content-type:text/html\r\n\r\n') #�ndra till utf8. Se johans. 
        print('''<!DOCTYPE html> 
        <html lang = "sv">
        <head>
            <title>Ditt eget Sl�kttr�d</title>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
        </head>''')
        
    def build_body(self):
        form = cgi.FieldStorage()
        ident = form.getvalue('ident')
        table_name = form.getvalue('table_name')     
        fambase = Family_base(tabla_name)
        fambase.get_persondetail_by_id(ident)
        print(
        '''<body>
            <h1>V�lkommen att bygga ditt eget sl�kttr�d!</h1>
            <h3>Detaljer f�r '''+ person.get_firstname()+'''</h3>''')
        print('f�rnamn %s')%(person.get_firstname())
        print('efternamn %s')%(person.get_lastname())
        print ('f�dd %s') % (person.get_birhdata())
        print ('d�d %s') % (person.get_death())
        print ('Mor %s %s') % (person.get_mother_firstname(), person.get_mother_lastname())
        print ('Far %s %s') % (person.get_father_firstname(), person.get_father_lastname())
        print ('Fakta %s') % (person.get_comment())
        print('''</body>''')
        
        
        
    def close_script(self):
        print ('''</html>''')
        