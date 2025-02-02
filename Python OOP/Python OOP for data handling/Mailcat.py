import pickle

class Mailcat_object():
    def __init__(self, user_id, name, email, list_items = []):
        self.id: int
        self.user_id = user_id
        self.name = name
        self.email = email
        self.list_items = list_items
        
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_list_data(self):
        return self.list_data

class Mailcat_collection():
    def __init__(self):
        self.Mailcat = {}
        self.counter = 0
    def add_Mailcat_object(self, Mailcat_object):
        self.counter += 1
        self.Mailcat[self.counter] = Mailcat_object


class create_catalog():
    def __init__(self):
        self.data = Mailcat_collection()
        self.data.add_Mailcat_object(Mailcat_object(1, 'Pesho', 'pesho@pesho.com', [1,2, 'bira', 3.14, 'ajkdoaksid897']))
        self.data.add_Mailcat_object(Mailcat_object(15, 'Ivan', 'vankata@pesho.com'))
        self.data.add_Mailcat_object(Mailcat_object(3, 'John Smith', 'john.smith@google.com', [34, 28, 'cat', 'dog', 3.14, 'Bitcoins']))

    def list_Mailcat_objects(self):
        for mail_obj in self.data.Mailcat.values():
            print(mail_obj.user_id, mail_obj.name, mail_obj.email, mail_obj.list_items)

    def serialize_Mailcat_objects(self):
        response = []
        header = ["UserID", "Name", "Email", "string1", "string2", "string3", "string4", "string5", "string6", "string7", "string8"]
        response.append(header)
        for mail_obj in self.data.Mailcat.values():
            response.append([str(mail_obj.user_id), mail_obj.name, mail_obj.email, *[str(i) for i in mail_obj.list_items]])
        return response
        
        
# Create object instance 
Mail_c = create_catalog()
# Call both methods for testing
Mail_c.list_Mailcat_objects()
Mail_c.serialize_Mailcat_objects()

database = open('db.obj', 'wb')
pickle.dump(Mail_c, database)
database.close()

del Mail_c
# print(Mail_c) # to show that the object Mail_c no longer exist. The line below will throw an error
# Mail_c.list_Mailcat_objects()

# Here we use the object from the database file
database = open('db.obj', 'rb')
Mail_c = pickle.load(database)
database.close()
print(Mail_c.serialize_Mailcat_objects())


