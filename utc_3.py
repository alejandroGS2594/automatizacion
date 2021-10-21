from xml.etree.ElementTree import parse, Element

file_name = "utc2.xml"
doc_xml = parse(file_name)
root = doc_xml.getroot()

root.remove(root.find('Edificio2'))

new_file = 'utc3.xml'
doc_xml.write(new_file, xml_declaration = True)
