import xml.etree.cElementTree as et

root = et.Element("UTC")

se = et.SubElement(root, "Edificio2")
et.SubElement(se, "Matricula").text = "16040086"
et.SubElement(se, "Carrera").text = "Redes"
et.SubElement(se, "Nombre").text = "David_Guevara"

se = et.SubElement(root, "Edificio2")
et.SubElement(se, "Matricula").text = "16824863"
et.SubElement(se, "Carrera").text = "Desarrollo"
et.SubElement(se, "Nombre").text = "Christian_Murra"

se = et.SubElement(root, "Edificio2")
et.SubElement(se, "Matricula").text = "16036785"
et.SubElement(se, "Carrera").text = "Redes"
et.SubElement(se, "Nombre").text = "Stephanie_Olivares"

se = et.SubElement(root, "Edificio2")
et.SubElement(se, "Matricula").text = "16042577"
et.SubElement(se, "Carrera").text = "Multimedia"
et.SubElement(se, "Nombre").text = "Roberto_Lopez"

tree = et.ElementTree(root)
tree.write("utc.xml", xml_declaration=True)
