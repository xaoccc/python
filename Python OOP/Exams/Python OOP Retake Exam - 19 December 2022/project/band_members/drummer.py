from project.band_members.musician import Musician


class Drummer(Musician):
    def learn_new_skill(self, new_skill: str): 
        available_skills = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        if new_skill not in available_skills:
            raise ValueError(f"{new_skill} is not a needed skill!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."