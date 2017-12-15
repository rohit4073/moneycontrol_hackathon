import xml.etree.ElementTree as ET
import os
import sqlite3

rootdir = '/Users/rohit/edu/moneycontrol-hackathon/data/'


def extract_xml_data(file_loc):
    parser = ET.parse(file_loc)
    root = parser.getroot()
    context_category = file_loc.split('/')[-2]
    article = root.find('article')
    heading = article.find('Heading').text
    summary = article.find('Summary').text
    body = article.find('Body').text
    url = article.find('URL').text
    image_url = article.find('Image').text
    entry_date = article.find('Entry_Date').text
    category = article.find('Category').text
    return [heading, summary, body, url, image_url, entry_date, category, context_category]


conn = sqlite3.connect('budgetData.db')
print("Opened database successfully")

try:
    conn.execute('''
        CREATE TABLE articles (
            id INT PRIMARY KEY  NOT NULL,
            heading VARCHAR(255) NOT NULL,
            summary text,
            body text,
            url text,
            image_url text,
            entry_date text,
            category varchar(255),
            context_category varchar(12)
        )
        ''')
except sqlite3.OperationalError:
    pass

print("Created table articles in budgetData")

count = 1
for subdir, dirs, files in os.walk(rootdir):
    for file_name in files:
        if file_name[-4:] == '.xml':
            file_loc = os.path.join(subdir, file_name)
            try:
                extracted_data = extract_xml_data(file_loc)
                extracted_data = [count] + extracted_data
                conn.execute("INSERT INTO articles VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", extracted_data)
                count += 1
            except Exception as e:
                print(file_name, e)
conn.commit()
print(count, "files added to Db")
