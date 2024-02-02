def accommodate_new_pets(capacity, w_limit, *pets):
    pet_types = {}
    for pet in pets:

        if capacity == 0:
            result = "You did not manage to accommodate all pets!\nAccommodated pets:\n"
            pet_types = dict(sorted(pet_types.items()))
            for key, value in pet_types.items():
                result += f"{key}: {value}\n"
            return result

        if pet[1] > w_limit:
            continue

        if pet[0] not in pet_types.keys():
            pet_types[pet[0]] = 0
        pet_types[pet[0]] += 1
        capacity -= 1

    result = f"All pets are accommodated! Available capacity: {capacity}.\nAccommodated pets:\n"
    pet_types = dict(sorted(pet_types.items()))
    for key, value in pet_types.items():
        result += f"{key}: {value}\n"
    return result






