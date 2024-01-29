from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, contact_info, unique_id):
        self.name = name
        self.contact_info = contact_info
        self.unique_id = unique_id

    def __str__(self):
        return f"Name: {self.name},Contact Info: {self.contact_info},ID: {self.unique_id}"
    
    def edit(self, new_contact_info=None):
        self.contact_info = new_contact_info or self.contact_info

    @abstractmethod
    def describe_person(self):
        pass

