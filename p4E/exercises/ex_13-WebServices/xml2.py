import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')#findall method retrieves Python list of subtrees taht rep user structures in xml tree.
print('User count:', len(lst))

#for loop that looks at each of the user nodes and prints the name and ide text elements as well as the x attr from user node
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Atrribute', item.get('x'))