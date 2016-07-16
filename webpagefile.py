# -*- coding: iso-8859-1 -*- 

class Webpage:
    """ Builds a tamplate for a webpage. Builds the head and closes the script
    Other classes should inherit this."""
    
    def __init__(self):
        pass
        
    def build_page(self):
        self.build_head()
        self.build_body()
        self.close_script()
    
    def build_head(self):
        """ Builds the head """
        
        print ('Content-type:text/html\r\n\r\n')
        print('''<!DOCTYPE html> 
        <html lang = "sv">
        <head>
            <title>Släktträd</title>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
        </head>''')
        
    def build_body(self):
        """ This is the function we want to change in the other classes """
        pass
        
        
    def close_script(self):
        
        """ Closes script """
        print ('''</html>''')
        