input_line = input()
lines_num = 1

while input_line != "end of comments":
    if lines_num == 1:
        print(f"<h1>\n    {input_line}\n</h1>")
    elif lines_num == 2:
        print(f"<article>\n    {input_line}\n</article>")
    else:
        print(f"<div>\n    {input_line}\n</div>")
    input_line = input()
    lines_num += 1
