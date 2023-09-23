class BabysitterApp:
    def __init__(self):
        self.parents = []
        self.children = []
        self.neighbourhoods = []

    def add_parent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)


    def add_neighbourhood(self, neighbourhood):
        if neighbourhood not in self.neighbourhoods:
            self.neighbourhoods.append(neighbourhood)


    def add_child_to_parent(self):
        #check if parent and child are in the same neghbourhood, if not - error!
        pass

    def search_for_babysitter(self):
        pass
