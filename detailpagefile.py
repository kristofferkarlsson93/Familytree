# -*- coding: iso-8859-1 -*- 
from familybasefile import Familybase
from webpagefile import Webpage
import cgi

class Detailpage(Webpage):
    """ Prits the details for chosen person and offers the user to modify it.
    Inherits the head and footer from the Webpage-class and prints out a 
    webpage"""
    
    def __init__(self):
        """ Takes in the persons id and the table_name. It also takes in a 
        person-object from the Familybase-class."""
        
        self.form = cgi.FieldStorage()
        self.ident = int(self.form.getvalue('ident'))
        self.table_name = str(self.form.getvalue('table_name'))
        self.fambase = Familybase(self.table_name)        
        self.person = self.fambase.get_persondetail_by_id(self.ident)
        self.all_names = self.fambase.get_all_names()
        
    
        
    def build_body(self):
        """ Builds the body of the page where it prints out a table with person
        info and creates a form to offers the user to modify the person"""
        
        print('''
        <body style = "background-color: #FFBF19">
            <h1>Detaljer för ''' + self.person.get_firstname() + '''</h1>''')
        
        print('''
        <div style = "float:left">
            <table border = "1">
                <tr>
                   <td>Förnamn</td>
                   <td> "%s"</td>
                </tr>
                <tr>
                   <td>Efternamn</td>
                   <td> "%s"</td>
                </tr>
                <tr>
                   <td>Född</td>
                   <td> "%s"</td>
                </tr>
                <tr>
                   <td>Död</td>
                   <td> "%s"</td>
                </tr>
                <tr>
                    <td> Föräldrar</td>
                    <td> 
            ''') % (self.person.get_firstname(), 
                         self.person.get_lastname(), 
                         self.person.get_birthdata(), self.person.get_death())
        
        self.print_parents()
        print('''
                    </td>
                </tr>
                <tr>
                    <td>Syskon</td>
                    <td>''')
        self.print_siblings()
        
        print('''
                    </td>
                </tr>
                <tr>
                    <td>Barn</td>
                    <td>''')
        self.print_children()
        print('''
                    </td>
                </tr>
                <tr>
                    <td>Fakta</td>
                    <td> %s </td>
                </tr>
            </table>
        <br/>''') % (self.person.get_comment())
        
        self.print_buttons()
        
        print('''
        </div>
        <div style = "width:300px; margin:0px auto;">''')
        
        self.option_modify_person()
        
        print('''
        </div></body>''')
        
    def print_parents(self):
        """ Takes in a list of dictionarys from Familybases function get_parents
        and prints it out with a link to the person"""
        
        parent_list = self.fambase.get_parents(self.person)
        for parent in parent_list:
            print('''
            <a href = 
            https://www8.cs.umu.se/~kv14kkn/5da000/familytree/persondetail.cgi?ident=%i&table_name=%s>
            %s %s </a><br/>''') % (parent['id'], self.table_name, 
                                   parent['firstname'], 
                                   parent['lastname'])
        
    def print_siblings(self):
        """ Takes in a list of dictionarys from Familybases function 
        get_siblings and prints it out with a link to the person """
        
        sibling_list = self.fambase.get_siblings(self.person, self.ident)
        for sibling in sibling_list:
            print('''
            <a href = 
            https://www8.cs.umu.se/~kv14kkn/5da000/familytree/persondetail.cgi?ident=%i&table_name=%s>
            %s %s </a><br/>''') % (sibling['id'], self.table_name, 
                                   sibling['firstname'], 
                                   sibling['lastname'])
            
    def print_children(self):
        """ Takes in a list of dictionarys from Familybases function 
        get_children and prints it out with a link to the person"""
        
        children_list = self.fambase.get_children(self.ident)
        for child in children_list:
            print('''<a href = 
            https://www8.cs.umu.se/~kv14kkn/5da000/familytree/persondetail.cgi?ident=%i&table_name=%s>
            %s %s </a><br/>''') % (child['id'], self.table_name, 
                                   child['firstname'], child['lastname'])
        
        print ("<br/>")
        
        
        
    def print_buttons(self):
        """ Print out two buttons. One to delete person which goes to 
        deleteperson.cgi and one that takes the user back to tha Mainpage by
        goback.cgi."""
        
        print('''<form action = 
        "https://www8.cs.umu.se/~kv14kkn/5da000/familytree/deleteperson.cgi" 
        method = "post">
        <input type = "hidden" name = "table_name" value = "%s">
        <input type = "hidden" name = "ident" value = %s>
        <table style = "float:left">
            <tr>
                <td><input type = "submit" value = "Ta bort person"></td>
        </form>''') % (self.table_name, self.ident)
        
        print('''<form action = 
        "https://www8.cs.umu.se/~kv14kkn/5da000/familytree/goback.cgi" 
        method = "post">
        <input type = "hidden" name = "table_name" value = "%s">
                <td><input type = "submit" value = "Tillbaka till listan"></td>
            </tr>
        </table></form>''') % (self.table_name)
        
    def option_modify_person(self):
        """ Creates the modidy-form which goes to modify.cgi. """
        
        print ('''
        
        <h3>Redigera personinfo</h3>
        <form action = 
        'https://www8.cs.umu.se/~kv14kkn/5da000/familytree/modifyperson.cgi' 
        method = 'post'>
            <input type = "hidden" name = 'tree_name', value = "%s">
            <input type = "hidden" name = 'ident', value = "%i">
            <table>
                <tr>
                    <td>Förnamn</td>
                    <td><input type = "text" name = 'firstname', value = "%s">
                    </td>
                </tr>
                <tr>
                    <td>Efternamn</td>
                    <td><input type = "text" name = 'lastname', value = "%s">
                    </td>
                </tr>
                <tr>
                    <td>Född</td>
                    <td><input type = "text" name = 'born', value = "%s"></td>
                </tr>
                <tr>
                    <td>Död</td>
                    <td><input type = "text" name = 'death', value = "%s"></td>
                </tr>
             ''') % (self.table_name, self.ident, self.person.get_firstname(), 
                     self.person.get_lastname(), self.person.get_birthdata(), 
                     self.person.get_death())
        
        print ('''
                <tr>
                    <td>Mor</td>
                    <td><select name = "mother_id">''')
        self.create_options()
        print (''' 
                    </select></td>
                </tr>
                <tr>
                    <td>Far</td>
                    <td><select name = "father_id">''')
        self.create_options()
        
        print('''
                    </select></td>
                </tr>
                <tr>
                    <td>Fakta</td>
                    <td><input type = "text" name = 'comment', value = "%s">
                    </td>
                </tr>
                <tr>
                    <td> </td>
                    <td><input type = "submit" value = "Redigera"></td>
                </tr>
            </table>
        </form>
        ''') % (self.person.get_comment())
 

    def create_options(self):
        """Creates the options in the select-tag in the form. The options is 
        the added persons in the tree."""
        
        print('''<option value = 0> okänd </option>''')
        for person in self.all_names:
            print('''<option value = %i> %s''' + ' ' +''' %s</option>
            ''') % (person["id"], person["firstname"], person["lastname"])
            
            
