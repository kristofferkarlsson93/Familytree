# -*- coding: iso-8859-1 -*- 
from webpagefile import Webpage


class Firstpage(Webpage):
    """Inherits the head and footer from the Webpage-class and prints out a 
    webpage"""
    
    def __init__(self):
        pass
        
            
    def build_body(self):
        """Builds the body of the page where the user can input a tree-name to
        create or load a familytree. The user is beeing sent to the 
        addtable.cgi file by a form"""
        
        print('''
        <body style = "background-color: #FFBF19">
            <br/>
          <div style = "color:black; width:400px; margin:0px auto;">
                <h1 style = "text-align:center">V�lkommen!</h1>            
                <h3 style = "text-align:center">
                B�rja med att namnge ditt sl�kttr�d.</h3>
                <p style = "text-align:center"> Om du redan skapat ett tr�d; 
                skriv in samma namn f�r att 
                forts�tta bygga och visa.</p>
                        
                <form action =
                'https://www8.cs.umu.se/~kv14kkn/5da000/familytree/addtable.cgi' 
                method = 'post' >
                    <p>Namnge tr�d <input type = "text" name = "tree_name">
                <input type = "submit" value = "Skapa/ladda!"></p>
            </div>

            </form>
        </body>''')
        