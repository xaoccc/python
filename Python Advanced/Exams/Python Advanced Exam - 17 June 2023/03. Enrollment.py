def gather_credits(needed_credits, *args):
    collected_credits, total_courses = 0, []
    if needed_credits == 0:
        return f"Enrollment finished! Maximum credits: {collected_credits}.\nCourses: {', '.join(sorted(total_courses))}"

    for course in args:
        course_name, course_credits = course

        if course_name not in total_courses:
            collected_credits += course_credits
            total_courses.append(course_name)

        if collected_credits >= needed_credits:
            return f"Enrollment finished! Maximum credits: {collected_credits}.\nCourses: {', '.join(sorted(total_courses))}"

    return f"You need to enroll in more courses! You have to gather {needed_credits - collected_credits} credits more."

