health = int(input())
virus = input()
while virus != "end":
    virus_strength = 0
    for i in virus:
        virus_strength += ord(i)
    virus_strength /= 3
    health -= int(virus_strength)
    time_to_defeat_virus = virus_strength * len(virus)
    print(f"Virus {virus}: {int(virus_strength)} => {int(time_to_defeat_virus)} seconds\n{virus} defeated in {time_to_defeat_virus // 60}m {time_to_defeat_virus % 60}s.\nRemaining health: {health}")
    virus = input()
