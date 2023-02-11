class Party:
    def __init__(self):
        self.people = []
    def get_info(self):
        all_party_people = self.people[]
        return f"""Going: {", ".join(all_party_people)}
        Total: {len(all_party_people)}""" 
        
party = Party()    
command = input()
while command != "End":
    party.people.append(command)
    command = input()
    
print(party.get_info())

