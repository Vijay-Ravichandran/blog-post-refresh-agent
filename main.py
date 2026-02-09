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

# Rule 1 - I am creating a simple link evaluation logic here - to access and usefulness

weak_domains = ["oldsite.net"]

for line in lines:
    if "http" in line:
        words = line.split()
        for word in words:
            if word.startswith("http"):
                url = word.strip(",.")
                if url.startswith("http://") or any(domain in url for domain in weak_domains):
                    print(f"Weak link detected: {url}")
                else:
                    print(f"Link seems reliable: {url}")

# Rule 2 - Bringing Structure clarity - refresh blog post should be <=6 sections and decide which is to keep, rewrite or leave unchanged 

num_sections = len(sections)
print(f"Total sections found: {num_sections}")

if num_sections > 6:
    print("Warning: Too many sections detected")
    print("Proposed action for extra sections:")
    print("- Merge smaller sections if possible")
    print("- Rewrite sections for clarity if needed")
    print("- Leave some sections unchanged if they are already fine")

# Rule 3 - Approval before taking action - for the corrections in sections before modifying, the system should know what needs to be modified or changed & why?
    approval = "yes"

    if approval == "yes":
        print("Proceeding with proposed changes to sections")
    else:
        print("No changes applied; sections remain unchanged")

else:
    print("Blog structure is fine; no changes needed")