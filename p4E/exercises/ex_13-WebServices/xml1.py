import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="int1">
    +1 734 303 4456
    </phone>
    <email hide="yes" />
</person>'''

tree = ET.fromstring(data)#converts string rep of xml into a "tree" of xml elements. 
print('Name:', tree.find('name').text)#find functioun searches through xml tree and retrieves element that match specific tag
print('Attr:', tree.find('email').get('hide'))