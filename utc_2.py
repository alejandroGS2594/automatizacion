import xml.etree.cElementTree as et
from xml.etree.ElementTree import SubElement, parse

xml_file = parse('utc.xml')

root = et.Element("UTC")

xmlRoot = xml_file.getroot()

se = et.SubElement(root, "Edificio2")
et.SubElement(se, "Matricula").text = "16078088"
et.SubElement(se, "Carrera").text = "Desarollo"
et.SubElement(se, "Nombre").text = "Sofia_Sanchez"

xmlRoot.append(se)
xml_file.write("utc.xml", xml_declaration=True)
