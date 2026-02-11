with open("blog_input.txt", "r", encoding="utf-8") as file:
    blog_text = file.read()

print (blog_text[:500])
print ("Blog content loaded successfully")
lines = blog_text.split("\n")

# I am adding a function here to count blog sections
def count_sections(text): # here i am defining a function so i can reuse this block of code whenever to count sections
    lines = text.split("\n")
    count = 0
    for line in lines:
        if line.strip().startswith("#"):
            count += 1
    return count 

# testing section count
test_text = "# Section 1\ncontent\n# Section 2\ncontent\n# Section 3\ncontent\n# Section 4\ncontent\n# Section 5\ncontent\n# Section 6\ncontent\n# Section 7\ncontent"
assert count_sections(test_text) == 7
print("section counting test passed.")

# I am adding a function for link parsing
def classify_link(url):
    if url.startswith("https://") and ".com" in url:
        return "strong"
    elif url.startswith("http://") and ".net" in url:
        return "weak"
    else:
        return "other"

# classifying test link     
assert classify_link("https://trustedsite.com/page") == "strong"
assert classify_link("http://oldsite.net/page") == "weak"
assert classify_link("https://example.org") == "other"
print("Link classification test passed.")

# I am applying logic to collect all section title and links
sections = []
current_section = []

for line in lines:
    line = line.strip()
    if not line:
        continue

    if line.startswith("#"):  
        if current_section:  
            sections.append("\n".join(current_section))
        current_section = [line]  
    else:
        current_section.append(line)  

if current_section:
    sections.append("\n".join(current_section))


links = []

for line in lines:
    for words in line.split():
        if words.startswith("http"): #links
            url = words.strip(",.")  
            links.append(url)
    
# Rule 1 - I am creating a simple link evaluation logic here - to assess and usefulness
print("Link Evaluation Results:")
for url in links:
    result = classify_link(url)
    if result == "strong":
        print(f"Reliable link: {url}")      
    elif result == "weak":
        print(f"Weak link detected: {url}")
    else:
        print(f"Link requires manual review: {url}")


# Rule 2 - Bringing Structure clarity - refresh blog post should be <=6 sections and decide which is to keep, rewrite or leave unchanged 
num_sections = count_sections(blog_text) # earlier I was just counting a lenght of list -> len(sections) now counting using a function
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
        merged_section = sections[-2] + "\n" + "\n".join(sections[-1].splitlines()[1:])
        sections = sections[:-2] # here i am removing last 2 
        sections.append(merged_section)  
    else:
        print("\nChange not approved. No changes applied.")

# final Verfication part - After approval merged section results to be displayed to ensure whether changes are reflected so i am adding this)
    print("\nUpdated Sections After Merge:")
for sec in sections:
    print(sec)
    print()


