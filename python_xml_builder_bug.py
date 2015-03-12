from xml.etree import ElementTree
from StringIO import StringIO

builder = ElementTree.TreeBuilder()
builder.start("top", {})
builder.start("line", {})
builder.data("2015-03-12 09:44:54.560 [1;32mscript runner plugin [1;34mHello, world[0m")
builder.end("line")
builder.end("top")
tree = ElementTree.ElementTree()
element = builder.close()
tree._setroot(element)
io = StringIO()
tree.write(io, encoding='utf-8', xml_declaration=True)
print io.getvalue()

ElementTree.fromstring(io.getvalue())
