from xml.dom import minidom
import os, sys
from os import path, mkdir

try:
	folder = raw_input ("Podaj Folder z Plikami (Content): ")
	filesystem = raw_input ("Podaj Plik (FileSystem.xml): ")
	plik = minidom.parse(filesystem)

	Nodes = plik.childNodes

	filenames = os.listdir(folder)

	while(True):
		for z in Nodes[0].getElementsByTagName("Volume"):

			for a in z.getElementsByTagName("Content"):

				for b in a.getElementsByTagName("Folder"):
					folder_xml = b.getAttribute("Name")
					folder_end = folder+"/"+folder_xml

					if not path.exists(folder_end):
						mkdir(folder_end)
						print "Tworze folder: "+folder_xml
						for c in b.getElementsByTagName("File"):
							print z.getAttribute("Type")+"/"+b.getAttribute("Name")+"/"+c.getAttribute("Name")
							Name =  c.getAttribute("Name")
							Content =  c.getAttribute("Content-Id")
							for filename in filenames:
								if filename == Content:

									os.rename(folder+"/"+filename, folder_end+"/"+Name)
									print filename+" na "+folder_end+"/"+Name
						else:
							break
						if b.getElementsByTagName("Folder"):
							mkdir(folder_end+"/"+b.getElementsByTagName("Folder")[0].getAttribute("Name"))
							folder_end = folder_end+"/"+b.getElementsByTagName("Folder")[0].getAttribute("Name")
							print "Tworze podfolder"
							for c in b.getElementsByTagName("Folder")[0].getElementsByTagName("File"):

								Name =  c.getAttribute("Name")
                                                                Content =  c.getAttribute("Content-Id")
                                                                for filename in filenames:
                                                                	if filename == Content:

										os.rename(folder+"/"+filename, folder_end+"/"+Name)
                                                                                print filename+" na "+folder_end+"/"+Name
								else:
									break
								if b.getElementsByTagName("Folder")[0].getElementsByTagName("Folder")[0].getElementsByTagName("File"):
									mkdir(folder_end+"/"+b.getElementsByTagName("Folder")[0].getElementsByTagName("Folder")[0].getAttribute("Name"))
									folder_end = folder_end+"/"+b.getElementsByTagName("Folder")[0].getElementsByTagName("Folder")[0].getAttribute("Name")
									print "Tworze podpodfolder"

									for c in b.getElementsByTagName("Folder")[0].getElementsByTagName("Folder")[0].getElementsByTagName("File"):

										Name =  c.getAttribute("Name")
										Content =  c.getAttribute("Content-Id")
										for filename in filenames:
											if filename == Content:
	
												os.rename(folder+"/"+filename, folder_end+"/"+Name)
												print filename+" na "+folder_end+"/"+Name
									else:
										break

					print "Jestem w Folder: "+folder_end
					#for c in tagname.getElementsByTagName("Folder")[0].getElementsByTagName("File"):

					#	Name =  c.getAttribute("Name")
					#	Content =  c.getAttribute("Content-Id")
					#	for filename in filenames:
					#		if filename == Content:
					#			os.rename(folder+"/"+filename, folder_end+"/"+Name)
					#			print folder+"/"+filename+" na "+folder_end+"/"+Name
					#		elif IndexError:
					#			continue
					#		else:
					#			continue
except KeyboardInterrupt:
	print "Koniec!"
