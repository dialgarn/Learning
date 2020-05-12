from xml.dom import minidom
import os

os.getcwd()
print(os.path.exists('XML Files'))
os.chdir('XML Files')
print(os.path.exists('Library.xml'))

mydoc = minidom.parse('Library.xml')
items = mydoc.getElementsByTagName('item')
