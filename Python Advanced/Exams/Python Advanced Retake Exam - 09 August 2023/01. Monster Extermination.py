from collections import deque

m_armor, s_damage = deque([int(i) for i in input().split(",")]), deque([int(i) for i in input().split(",")])
killed_monsters = 0

while m_armor and s_damage:
    current_m_armor = m_armor.popleft()
    current_s_damage = s_damage.pop()

    if current_s_damage >= current_m_armor:
        current_s_damage -= current_m_armor
        killed_monsters += 1

        if s_damage:
            s_damage[-1] += current_s_damage
        elif not s_damage and current_s_damage > 0:
            s_damage.append(current_s_damage)
    else:
        m_armor.append(current_m_armor - current_s_damage)

if not m_armor:
    print("All monsters have been killed!")

if not s_damage:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")