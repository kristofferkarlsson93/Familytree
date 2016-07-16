# -*- coding: iso-8859-1 -*-
import cgi
from familybasefile import Familybase
from webpagefile import Webpage


class Mainpage(Webpage):
    """This class builds the biggest page in the project. It lets the user see 
    the members of the tree and create new members
    Inherits the head and footer from the Webpage-class and prints out a 
    webpage"""
    
    def __init__(self, table_name):
        """ Takes in the table name and creats a dictionary with al the names 
        and IDs in the table"""
        
        self.table_name = table_name
        self.fambase = Familybase(self.table_name)
        self.all_names = self.fambase.get_all_names()          
    
    def build_body(self):        
        """ Builds the body that shows the added persons and offers the user to
        add new members. It also divids the page to do the layout"""
        
        print('''
        <body style = "background-color: #FFBF19">
        <div style = "color:black">
                <h1 style = "text-align:center"> 
                Hantera trädet ''' + self.table_name + ''' </h1>
        <br/></div>
        <div style = "float:left">
        <h3> Personer i trädet</h3>
        <p> Klicka för att visa eller redigera person</p>''')
        self.link_to_person()
        print ('''<br/>''')
        self.create_back_button()
        print ('''
        </div>
        <div style = "color:black; width:300px; margin:0px auto;">''')
        self.print_form()
        print ('''<br/>
        </div></body>
        ''')
        
    
    def print_form(self):
        """ Creates a table with a form in so the user can add persons.
        The information is sent to addmember.cgi"""
        
        print('''
            <h3>Fyll i de uppgifter som efterfrågas</h3>
            <form action = 
            'https://www8.cs.umu.se/~kv14kkn/5da000/familytree/addmember.cgi' 
            method = 'post'>
                <input type = "hidden" name = 'tree_name', value = 
                '''+ self.table_name + '''>
                <table>
                <tr>
                    <td>Förnamn</td>
                    <td><input type = "text" name = 'firstname'></td>
                </tr>
                <tr>
                    <td>Efternamn</td>
                    <td><input type = "text" name = 'lastname'></td>
                </tr>
                <tr>
                    <td>Född</td>
                    <td><input type = "text" name = 'born', value = "YY-MM-DD">
                    </td>
                </tr>
                <tr>
                    <td>Död</td>
                    <td><input type = "text" name = 'death', value = "YY-MM-DD">
                    </td>
                </tr>
                <tr>
                    <td>Mor</td>
                    <td><select name = "mother_id"> ''')
        self.create_options()
        print (''' </select></td>
                <tr>
                    <td>Far</td>
                    <td><select name = father_id>''')
        self.create_options()
        
        print('''
        </select></td>
                <tr>
                    <td>Fakta</td>
                    <td><input type = "text" name = 'comment'></td>
                </tr>
                    <td> </td>
                    <td><input type = "submit" value = "Lägg till släktingen">
                    </td>
            </table>
            </form>''')
        
    def link_to_person(self):
        """ Prints out all the persons in the table/tree and gives them a link
        to the persondetail.cgi. It uses the all_names list that is generated 
        in Familybase-class and stored in the init function of this class."""
        
        for person in self.all_names:
            print ('''<a href = 
            https://www8.cs.umu.se/~kv14kkn/5da000/familytree/persondetail.cgi?ident=%i&table_name=%s>
            %s %s </a><br/>''')%(person["id"], self.table_name, 
                                 person["firstname"], person["lastname"])
    def create_back_button(self):
        """ Creates the backbutton so the user can go back to index.cgi."""
        print('''<form action =
        'https://www8.cs.umu.se/~kv14kkn/5da000/familytree/index.cgi' 
        method = 'post'>
            <input type = "submit" value = "Tillbaka till startsidan">
        </form>''')       
            
    def create_options(self):
        """Creates the options in the select-tag in the form. The options is 
        the added persons in the tree."""
        
        print ('''<option value = 0> okänd </option>''')
        for person in self.all_names:
            print ('''<option value = %i> %s''' + ' ' +''' %s</option>
            ''') % (person["id"], person["firstname"], person["lastname"])