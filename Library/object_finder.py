#Works only inside the app class

def __find_object(self, OBJECT_PARAMETER):
    for OBJECT in self.LIST_OF_OBJECTS:
        if OBJECT.OBJECT_PARAMETER == OBJECT_PARAMETER:
            return OBJECT
