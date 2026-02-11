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

# I am proposing to merge the last 2 sections instead of just printing the messages - to address concrete change to meet structual clarity requirement
    
    section1 = sections[-2]
    section2 = sections[-1]

    print("\nProposed Change:")
    print(f"I want to merge '{section1}' and '{section2}'")
    print("Reason: Blog has more than 6 sections, so merging will satisfy the rule.")

# Rule 3 - Approval before taking action - for the corrections in sections before modifying, the system should know what needs to be modified or changed & why?
    approval = input("\nDo you approve this change? (yes/no): ")

    if approval.lower() == "yes":
        print("\nChange approved. Applying merge...")

        # simple merge logic (removing last section heading)
        blog_text = blog_text.replace(section2, "")

        # Verfication part - merged section results to be displayed to ensure whether changes are reflected to adding this)
        updated_lines = blog_text.split("\n")
        updated_sections = []

        for line in updated_lines:
            if line.strip().startswith("#"):
                updated_sections.append(line.strip())
        
        print("\nUpdated Results:")
        print(f"Total sections found (After): {len(updated_sections)}")
        print("Updated Sections List:")

        print("Sections merged successfully.")
        for sec in updated_sections:
            print(sec)

    else:
        print("\nChange not approved. No changes applied.")

else:
    print("Blog structure is fine. No changes proposed.")
    