import os
import xml.etree.ElementTree as ET

# Declaring path of xml texts
path = '/Users/hafi/PycharmProjects/TextminNewsCategorization/trainset'

# Get clean text in <p> in xml file
def getText(path):
    paragraph = [] # Store all sentences inside xml's code <p> until </p>
    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        fullname = os.path.join(path, filename)
        tree = ET.parse(fullname)
        root = tree.getroot()
        for text in root.iter('text'):
            for p in text.iter('p'):
                paragraph.append(p.text)
    return paragraph
