health = int(input())
virus, known_viruses = input(), []
current_health = health
while virus != "end":
    virus_strength = 0
    for i in virus:
        virus_strength += ord(i)
    virus_strength = int(virus_strength / 3)
    if virus not in known_viruses:
        time_to_defeat_virus = virus_strength * len(virus)
    else:
        time_to_defeat_virus = virus_strength * len(virus) // 3
    current_health -= int(time_to_defeat_virus)
    known_viruses.append(virus)
    if current_health <= 0:
        print(f"Virus {virus}: {int(virus_strength)} => {int(time_to_defeat_virus)} seconds")
        print("Immune System Defeated.")
        break
    else:
        print(f"Virus {virus}: {int(virus_strength)} => {int(time_to_defeat_virus)} seconds\n{virus} defeated in {int(time_to_defeat_virus // 60)}m {int(time_to_defeat_virus % 60)}s.\nRemaining health: {int(current_health)}")
        if current_health * 1.2 <= health:
            current_health = int(current_health) * 1.2
        else:
            current_health = health
    virus = input()
if current_health > 0:
    print(f"Final Health: {int(current_health)}")
