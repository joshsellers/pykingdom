import xml.etree.ElementTree as et
root = et.parse("assets/levels/fields.oel").getroot()

print(root.get('backdropFarImg'))
