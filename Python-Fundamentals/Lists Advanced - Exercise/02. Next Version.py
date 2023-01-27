old_version = input().split(".")
old_version = "".join(old_version)
new_version = str(int(old_version) + 1)

print(f"{new_version[0]}.{new_version[1]}.{new_version[2]}")
