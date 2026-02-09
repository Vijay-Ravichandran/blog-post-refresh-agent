with open("blog_input.txt", "r", encoding="utf-8") as file:
    blog_text = file.read()
print (blog_text[:500])
print ("Blog content loaded successfully")