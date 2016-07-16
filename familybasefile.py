# -*- coding: iso-8859-1 -*-
import cgi
import sqlite3 
from personfile import Person

class Familybase:
    """ Handles all the database communication in the project """
    
    def __init__(self, table_name): 
        """ Connects to the database Familybase.db and takes in the table_name
        """
        
        self._conn = sqlite3.connect("Familybase.db")
        self.c = self._conn.cursor()
        self.table_name = table_name
        
        
    def create_family_table(self):
        """ Creates a Family-table wich stores all the familys. If the 
        familyname exists id does not creates a new one. It then creates the
        table with the users table name. It contains the columns.
        - ident 
        - Firstname
        - lastname
        - born
        - dead
        - Mother_id
        - father_id
        - comment"""
        
        self.c.execute('''CREATE TABLE IF NOT EXISTS Familys (ident INTEGER 
        PRIMARY KEY AUTOINCREMENT, familyname TEXT)''')
        
        familyname_list = []
        self.c.execute('''SELECT familyname FROM Familys''')
        for row in self.c.fetchall():
            familyname_list.append(row[0])
        
        if self.table_name not in familyname_list:
            self.c.execute('''INSERT INTO Familys(familyname) VALUES
            (?)''', (self.table_name,))
        
        self.c.execute('''CREATE TABLE IF NOT EXISTS ''' + self.table_name + '''
        (ident INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT,
        born TEXT, death TEXT, mother_id INTEGER, father_id INTEGER, 
        comment TEXT)''')         
        
    def enter_familymember(self, person):  
        """ Puts the person-info in the users table. Uses a person-object 
        from the Person-class"""
        
        self.c.execute('''INSERT INTO ''' + self.table_name + '''(firstname, 
        lastname, born, death, mother_id, father_id, comment) VALUES
        (?, ?, ?, ?, ?, ?, ?)''', (person.get_firstname(), 
                                         person.get_lastname(),
                                         person.get_birthdata(), 
                                         person.get_death(),
                                         person.get_mother_id(),
                                         person.get_father_id(),
                                         person.get_comment()))
        self._conn.commit()   
        self.c.close()
        self._conn.close()
        
    def get_all_names(self):
        """ Gets all the name and ident in the users table. Puts them in a 
        list of dictionarys. The dictionary repressents a person"""
        
        result = []
        self.c.execute('''SELECT ident, firstname, lastname FROM ''' + 
                       self.table_name)
        
        for row in self.c.fetchall():
            person = {"id":row[0], "firstname":row[1], "lastname":row[2]}
            result.append(person)
        
        return result
    
    def get_persondetail_by_id(self, ident):
        """ Takes out all information for one person (except the Ident) and 
        creates a person-object with te Person-class"""
        
        self.c.execute('''SELECT firstname, lastname, born, death, 
        mother_id, father_id, comment FROM ''' + self.table_name + ''' WHERE 
        ident = ?''', (ident,))
        
        (firstname, lastname, born, death, mother_id, 
         father_id, comment) = self.c.fetchone()
        
        return Person(firstname, lastname, born, death, mother_id, father_id, 
                      comment)
    
    def get_parents(self, person):
        """ Takes out a persons parents using the users ID. returns a list of 
        dictionarys which repressents a person"""
        
        parent_list = []
        self.c.execute('''SELECT ident, firstname, lastname from '''+ 
                       self.table_name +''' WHERE ident = ? OR ident = ?
                       ''', (person.get_mother_id(),
                             person.get_father_id()))
        
        for row in self.c.fetchall():
            parent = {"id":row[0], "firstname":row[1], "lastname":row[2]}
            parent_list.append(parent)   
            
        return parent_list
        
        
    def get_siblings(self, person, ident):
        """ Takes out a persons siblings using ident from the person and puts
        it in a list of dictionarys. Siblings is everyone that has the same
        father and mother ident. It checks so the sibling is not the person
        itself and if the siblings has parents ident = 0 it does not add it.
        0 is default if parents are unknown."""
        
        sibling_list = []
        self.c.execute('''SELECT ident, firstname, lastname, mother_id, 
        father_id FROM ''' + self.table_name + ''' WHERE mother_id = ? AND 
        father_id = ?
        ''', (person.get_mother_id(), person.get_father_id()))
        
        for row in self.c.fetchall():
            if int(row[0]) != ident and int(row[3]) != 0 and int(row[4]) != 0:
                sibling = {"id":row[0], "firstname":row[1], "lastname":row[2]}
                sibling_list.append(sibling)
        return sibling_list
    
    def get_children(self, ident):
        """ Takes out the persons siblings and returns them in a list of 
        dictionarys """
        children_list = []
        self.c.execute('''SELECT ident, firstname, lastname FROM ''' + 
                      self.table_name + ''' WHERE mother_id = ? OR father_id = ?
                      ''', (ident, ident))
        
        for row in self.c.fetchall():
            child = {"id":row[0], "firstname":row[1], "lastname":row[2]}
            children_list.append(child) 
            
        self.c.close()
        self._conn.close()        
        return children_list

    def delete_person(self, ident):
        """ Deletes the person using its ident """
        
        self.c.execute('''DELETE FROM ''' + self.table_name +''' WHERE ident = ?
        ''', (ident,))
        self._conn.commit() 
        
    def modify_person(self, person, ident):
        """ Modifys the person using its ident """
        
        self.c.execute('''UPDATE ''' + self.table_name + ''' set firstname = ?,
        lastname = ?, born = ?, death = ?, mother_id = ?, father_id = ?, 
        comment = ? WHERE ident = ?
        ''', (person.get_firstname(), person.get_lastname(), 
              person.get_birthdata(), person.get_death(), 
              person.get_mother_id(), person.get_father_id(),
              person.get_comment(), ident))
        
        self._conn.commit()