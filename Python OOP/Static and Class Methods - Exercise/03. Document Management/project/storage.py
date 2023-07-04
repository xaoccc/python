from project.category import Category
from project.topic import Topic
from project.document import Document

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []
        
    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)
    
    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)
    
    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)
            
    def edit_category(self, category_id, new_name):
        for category in self.categories:
            if category.id == category_id:
                category.name = new_name
                break

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.topic = new_topic
                topic.storage_folder = new_storage_folder
                break
    
    def edit_document(self, document_id, new_file_name):
        for document in self.documents:
            if document.id == document_id:
                document.file_name = new_file_name
                break
                
    def delete_category(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                self.categories.remove(category)
                break
    
    def delete_topic(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                self.topics.remove(topic)
                break
            
    def delete_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                self.documents.remove(document)
                break

    def get_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document
                
    def __repr__(self):
        result = ""
        for doc in self.documents:
            result += f"{doc}\n"
        result = result.strip('\n')  
        return result