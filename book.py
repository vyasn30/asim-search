from bs4 import BeautifulSoup

# Assuming 'html_content' contains your HTML book content
# Replace 'html_content' with the actual HTML content string

with open("stpb.html") as fp:
    soup = BeautifulSoup(fp)

# Parse the HTML content

# Find all headers (h1, h2, h3) and their related paragraphs (p)
headers = soup.find_all(['h1', 'h2'])

content = []

# Iterate through each header and its associated paragraphs
for header in headers:
    header_text = header.get_text(strip=True)
    paragraphs = []
    next_element = header.find_next_sibling()
    
    while next_element and next_element.name != header.name:
        if next_element.name == 'p':
            paragraphs.append(next_element.get_text(strip=True))
        next_element = next_element.find_next_sibling()

    # Create a dictionary for each topic with its paragraphs
    topic = {
        'title': header_text,
        'paragraphs': paragraphs
    }
    content.append(topic)

content = content[30:]


chapter_names = [topic.get("title")  for topic in content if topic.get('title')[0] == '[']
topics = list()

chapter_count = -1


try:
    # for val in content:
    #     topic = dict() 
    #     if val.get('title') != chapter_names[chapter_count]:  #val["title"] is a topic name
    #         topic["chapter_name"] = chapter_names[chapter_count]
    #         topic["topic_name"] = val.get('title')
    #         topic["paragraphs"] = val.get('paragraphs')
    #     else:
    #         # its a chapter and now we go to new chapter
    #         chapter_count+=1

    #     topics.append(topic)

    for val in content:
        topic = dict()
        
        if val.get("title") == chapter_names[chapter_count+1]:
            chapter_count+=1
            continue

        if val.get("title")[:3] !=  "ખંડ" and val.get("title") != chapter_names[chapter_count+1]:
            topic["chapter_name"] = chapter_names[chapter_count]
            topic["topic_name"] = val.get("title")
            topic["paragraphs"] = val.get("paragraphs")
            topics.append(topic)

except Exception as e:
    pass



# Display the content (array of objects - topics with paragraphs)
for topic in content:
    print(topic)
