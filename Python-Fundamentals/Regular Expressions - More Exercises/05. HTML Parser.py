import re
webpage_content = input()
title = re.finditer(r'(?P<title>(?<=<title).+(?=title>))', webpage_content)
content = re.finditer(r'(?P<content>(?<=<body).+(?=body>))', webpage_content)
final_title, final_content = "", ""
for show in title:
    filtered_content1 = re.finditer(r'(?<=>)[\w\W][^<>]+(?=<)', show['title'])
    for i in filtered_content1:
        final_title += i.group()
print(f"Title: {final_title}")        
for show in content:
    filtered_content2 = re.finditer(r'(?<=>)[\w\W][^<>]+(?=<)', show['content'])
    for i in filtered_content2:
        final_content += i.group()
final_content = final_content.replace("\\n", "")        
print(f"Content: {final_content}")
