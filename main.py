with open("blog_input.txt", "r", encoding="utf-8") as file:
    blog_text = file.read()
print (blog_text[:500])
print ("Blog content loaded successfully")

lines = blog_text.split("\n")

sections = []
links = []

for line in lines:
    if line.strip().startswith("#"):
        sections.append(line.strip())
    if "http" in line:
        links.append(line.strip())

print(f"Total sections found: {len(sections)}")
print(f"Total links found: {len(links)}")
