scenes_time = int(input())
scenes_num = int(input())
scene_duration = int(input())
terrain_prep_time = scenes_time * 0.15
 
time_needed = terrain_prep_time + (scene_duration * scenes_num)
if time_needed <= scenes_time:
    print(f"You managed to finish the movie on time! You have {round(scenes_time - time_needed)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(time_needed - scenes_time)} minutes.")
