import os
import xml.etree.ElementTree as ET
path = '/Users/hafi/PycharmProjects/TextminNewsCategorization/trainset'
paragraph = []
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    tree = ET.parse(fullname)
    root = tree.getroot()
    for text in root.iter('text'):
        for p in text.iter('p'):
            paragraph.append(p.text)
