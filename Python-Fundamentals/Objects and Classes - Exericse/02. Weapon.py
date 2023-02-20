class Weapon:
    
    def __init__(self, bullets):
        self.bullets = bullets
        
    def shoot(self):
        if self.bullets >= 1:
            self.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"
        
    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"
        
bullets_num = int(input())        
weapon_obj = Weapon(bullets_num)

print(weapon_obj.shoot())
print(weapon_obj.shoot())
print(weapon_obj.shoot())
print(weapon_obj)
