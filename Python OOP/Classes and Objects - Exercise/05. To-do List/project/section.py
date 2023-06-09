from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.cleaned = 0
    
    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"
        
    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"
        
    def clean_section(self):
        for task in self.tasks:
            if task.completed:
                self.cleaned += 1
                self.tasks.remove(task)
        return f"Cleared {self.cleaned} tasks."
    
    def view_section(self):
        output = [f"Section {self.name}:"]
        for task in self.tasks:
            output.append(f"{task.details()}")
        return '\n'.join(output)




