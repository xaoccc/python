def students_credits(*args):
    creadits_earned = 0
    courses = {}
    result = ""
    for i in range(len(args)):
        data = args[i].split("-")
        course_name, credits, max_test_pts, diyan_pts = data[0], int(data[1]), int(data[2]), int(data[3])
        current_score = credits * (diyan_pts / max_test_pts)
        creadits_earned += current_score
        courses[course_name] = current_score
        
    if creadits_earned >= 240:
        result += f"Diyan gets a diploma with {creadits_earned:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - creadits_earned:.1f} credits more for a diploma.\n"
        
    courses = dict(sorted(courses.items(), key=lambda x: -x[1]))
    for course, score in courses.items():
        result += f"{course} - {score:.1f}\n"
    return result

print(
    students_credits(
        "Python Development-15-200-200",
        "Python Development-20-300-300",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)