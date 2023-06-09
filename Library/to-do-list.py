import re
from datetime import datetime


class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False
        self.date_pattern = r'^([0][1-9]|[12][0-9])\/([0][1-9]|[1][012])\/([12][0-9]{3})$'
        self.date_format = "%d/%m/%Y"
        
    def date_format_check(self, input_date):
        
        match = re.search(self.date_pattern, input_date)
        if match != None:
            datetime_object = datetime.strptime(match.string, self.date_format)
            current_date = datetime.now()
            if current_date <= datetime_object:
                new_date = datetime_object.strftime("%m/%d/%Y")
                return new_date
            return "Choose a future date!"
        return "Please enter a valid date fomat!"
    
    def change_name(self, new_name: str):
        if self.name != new_name:
            self.name = new_name
            return self.name
        return "Name cannot be the same."
        
        
    def change_due_date(self, new_date: str):
            if self.due_date != new_date :
                self.due_date = self.date_format_check(new_date)
                return self.due_date
            return "Date cannot be the same."


    def add_comment(self, comment: str):
        self.comments.append(comment)
        
        
    def edit_comment(self, comment_number: int, new_comment: str):
        if len(self.comments) > comment_number or comment_number >= 0:
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        return "Cannot find comment."
        
        
    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
        

# Test code:        
# print(task.change_name("Go to University"))
# print(task.change_due_date(input()))
# print(task.change_due_date(input()))
# print(task.change_due_date(input()))
# print(task.change_due_date(input()))
# print(task.change_due_date(input()))
# task.add_comment("Don't forget laptop")
# print(task.change_due_date("09/06/2023"))
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
