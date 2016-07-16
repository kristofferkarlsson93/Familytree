class Person:
    """ This class function in the project is to create a person-object wich is
    being used when a complete person is being used"""
    
    def __init__(self, firstname, lastname, born, death, mother_id, father_id, 
                 comment):
        """ Creates the object """
        self.firstname = firstname
        self.lastname = lastname
        self.born = born
        self.death = death
        self.mother_id = mother_id
        self.father_id = father_id
        self.comment = comment 
        
    def get_firstname(self):
        """ Returns the firstname """
        return str(self.firstname)
    
    def get_lastname(self):
        """ Returns the lastname """
        return str(self.lastname)
    
    def get_birthdata(self):
        """ Returns the birth info"""
        return str(self.born)
    
    def get_death(self):
        """ Returns the death data """
        return str(self.death)
    
    def get_mother_id(self):
        """ Returns the mother id """
        return int(self.mother_id)
        
    def get_father_id(self):
        """ Returns the father id """
        return int(self.father_id)
    
    def get_comment(self):
        """ Returns the comment """
        return str(self.comment)