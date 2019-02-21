with open("links.txt","r") as linkfile:
    links = linkfile.readlines()

i = 0
for each in links:
    i += 1
    name = each.replace("https://schema.org/","").replace("\n","")
    link = each.replace("\n","")
    line = str(i)
    with open("links_sorted.txt","a") as sortlinks:
        sortlinks.writelines(line+"#"+name + "\n")