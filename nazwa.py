# /usr/bin/env python
# encoding: utf-8

# Program do zmiany nazw plików po backupie sony stock
# Version: 1.0
# Autor: Adrian Skrzydło
import xml.etree.ElementTree as ET
import os

folder = raw_input("Podaj Folder z Plikami (Content): ")
filesystem = raw_input("Podaj Plik (FileSystem.xml): ")

tree = ET.parse(filesystem)

root = tree.getroot()

filenames = os.listdir(folder)

for child in root: #Volume
	if child.get("Type") == "INTERNAL":
		dir = folder+"/"+child.get("Type")
		if not os.path.exists(folder+"/"+child.get("Type")):
			os.makedirs(dir)
		for child2 in child:

			for child3 in child2: #Nazwa folderu
				if not child3.get("Name") == None:
					print "Folder: %s" % child3.get("Name")
					folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")
					print "Folder_end: ", folder_end
					if not os.path.exists(folder_end):
						os.makedirs(folder_end)
	
					for child4 in child3: #Nazwa Pliku
						zmienna = child3
						if child4.get("Content-Id") == None: #Jezeli jest to Folder
							print child4.tag, child4.get("Name")
							folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")
							if not os.path.exists(folder_end):
								os.makedirs(folder_end)
	
							for child5 in child4: #Nazwa Folder/Plik
								if child5.get("Content-Id") == None: #Jezeli jest to Folder
									print child5.tag, child5.get("Name")
									folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")
									if not os.path.exists(folder_end):
										os.makedirs(folder_end)
									for child6 in child5:
										if child6.get("Content-Id") == None: #Jezeli jest to Folder
											print child6.tag, child6.get("Name")
											folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")
											if not os.path.exists(folder_end):
												os.makedirs(folder_end)
											for child7 in child6:
	
												if child7.get("Content-Id") == None:
													Name = child7.get("Name")
													Content = child7.get("Content-Id")
													folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")
                       		                         						if not os.path.exists(folder_end):
                       		                                 						os.makedirs(folder_end)
													for child8 in child7:
														if child8.get("Content-Id") == None:
															Name = child8.get("Name")
															Content = child8.get("Content-Id")
															folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")+"/"+child8.get("Name")
															if not os.path.exists(folder_end):
																os.makedirs(folder_end)
															for child9 in child8:
																if child9.get("Content-Id") == None:
																	Name = child9.get("Name")
                                                                                                                        		Content = child9.get("Content-Id")
                                                                                                                        		folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")+"/"+child8.get("Name")+"/"+child9.get("Name")
                                                                                                                        		if not os.path.exists(folder_end):
                                                                                                                        		        os.makedirs(folder_end)
																	for chile10 in child9:
																		if child10.get("Content-Id") == None:
																			Name = child10.get("Name")
                                                                                                                                        		Content = child10.get("Content-Id")
                                                                                                                                        		folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")+"/"+child8.get("Name")+"/"+child9.get("Name")+"/"+child10.get("Name")
                                                                                                                                        		if not os.path.exists(folder_end):
                                                                                                                                        		        os.makedirs(folder_end)
																		else:
																			Name = chile10.get("Name").encode('utf-8')
																			Content = child10.get("Content-Id")
																			folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")+"/"+child8.get("Name")+"/"+child9.get("Name")+"/"
																			for filename in filenames:
																				os.rename(folder+"/"+filename, folder_end+Name)
																				print filename+" --> "+folder_end+Name
																else:
																	Name = child9.get("Name").encode('utf-8')
                                                                                                                        		Content = child9.get("Content-Id")
                                                                                                                        		folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")+"/"+child8.get("Name")+"/"
                                                                                                                        		for filename in filenames:
                                                                                                                        			if filename == Content:
																		        os.rename(folder+"/"+filename, folder_end+Name)
                                                                                                                        		        	print filename+" --> "+folder_end+Name
														else:
															Name = child8.get("Name").encode('utf-8')
															Content = child8.get("Content-Id")
															folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")+"/"
															for filename in filenames:
																if filename == Content:
																	os.rename(folder+"/"+filename, folder_end+Name)
																	print filename+" --> "+folder_end+Name
	
												else:
													Name = child7.get("Name").encode('utf-8')
                       		                         						Content = child7.get("Content-Id")
                       		                         						folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"
                       		                         						for filename in filenames:
                       		                         						        if filename == Content:
                       		                         						                os.rename(folder+"/"+filename, folder_end+Name)
                       		                         						                print filename+" --> "+folder_end+Name
										else:
											Name = child6.get("Name").encode('utf-8')
											Content = child6.get("Content-Id")
											folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"
		
											for filename in filenames:
												if filename == Content:
													os.rename(folder+"/"+filename, folder_end+Name)
											        	print filename+" --> "+folder_end+Name
								else:
	
									Name = child5.get("Name").encode('utf-8')
									Content = child5.get("Content-Id")
									folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"
		
									for filename in filenames:
										if filename == Content:
											os.rename(folder+"/"+filename, folder_end+Name)
					                                        	print filename+" --> "+folder_end+Name
	
						else:					#Jezeli jest to Plik
							Name = child4.get("Name").encode('utf-8')
							Content = child4.get("Content-Id")
							folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"

							for filename in filenames:
								if filename == Content:
									os.rename(folder+"/"+filename, folder_end+Name)
									print filename+" --> "+folder_end+Name
	elif child.get("Type") == "EXTENDED":
		dir = folder+"/"+child.get("Type")
		if not os.path.exists(folder+"/"+child.get("Type")):
			os.makedirs(dir)
		for child2 in child:
			for child3 in child2: #Nazwa folderu
				if not child3.get("Name") == None:
					print "Folder: %s" % child3.get("Name")
					folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")
					print "Folder_end: ", folder_end
					if not os.path.exists(folder_end):
						os.makedirs(folder_end)
					for child4 in child3: #Nazwa Pliku
						if child4.get("Content-Id") == None: #Jezeli jest to Folder
							print child4.tag, child4.get("Name")
							folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")
							if not os.path.exists(folder_end):
								os.makedirs(folder_end)
								for child5 in child4: #Nazwa Folder/Plik
									if child5.get("Content-Id") == None: #Jezeli jest to Folder
										print child5.tag, child5.get("Name")
										folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")
										if not os.path.exists(folder_end):
											os.makedirs(folder_end)
										for child6 in child5:
											if child6.get("Content-Id") == None: #Jezeli jest to Folder
												print child6.tag, child6.get("Name")
												folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")
												if not os.path.exists(folder_end):
													os.makedirs(folder_end)
												for child7 in child6:
													if child7.get("Content-Id") == None:
														Name = child7.get("Name")
														Content = child7.get("Content-Id")
														folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")
                	        	                       							if not os.path.exists(folder_end):
                	        	                        	       						os.makedirs(folder_end)
														for child8 in child7:
															if child8.get("Content-Id") == None:
																Name = child8.get("Name")
																Content = child8.get("Content-Id")
																folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")+"/"+child8.get("Name")
																if not os.path.exists(folder_end):
																	os.makedirs(folder_end)
																for child9 in child8:
																	if child9.get("Content-Id") == None:
																		Name = child9.get("Name")
																		Content = child9.get("Content-Id")
																		folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")+"/"+child8.get("Name")+"/"+child9.get("Name")
																		if not os.path.exists(folder_end):
																			os.makedirs(folder_end)
																		for child10 in child9:
																			if child10.get("Content-Id") == None:
																				folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")+"/"+child8.get("Name")+"/"+child9.get("Name")+"/"+child10.get("Name")
																				if not os.path.exists(folder_end):
																					os.makedirs(folder_end)
																			else:
																				Name = child10.get("Name")
																				Content = child10.get("Content-Id")
																				folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")+"/"+child8.get("Name")+"/"+child9.get("Name")+"/"
																				for filename in filenames:
																					os.rename(folder+"/"+filename, folder_end+Name)
																					print filename+" --> "+folder_end+Name
																	else:
																		Name = child9.get("Name")
																		Content = child9.get("Content-Id")
																		folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")+"/"+child8.get("Name")+"/"
																		for filename in filenames:
																			os.rename(folder+"/"+filename, folder_end+Name)
																			print filename+" --> "+folder_end+Name
															else:
																Name = child8.get("Name").encode('utf-8')
																Content = child8.get("Content-Id")
																folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"+child7.get("Name")+"/"
																for filename in filenames:
																	os.rename(folder+"/"+filename, folder_end+Name)
																	print filename+" --> "+folder_end+Name
													else:
														Name = child7.get("Name").encode('utf-8')
                	        	                       							Content = child7.get("Content-Id")
                	        	                       							folder_end = folder+"/"+chiled.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"+child6.get("Name")+"/"
                	        	                       							for filename in filenames:
                	        	                       							        if filename == Content:
                	        	                       							                os.rename(folder+"/"+filename, folder_end+Name)
                	        	                       							                print filename+" --> "+folder_end+Name
											else:
												Name = child6.get("Name").encode('utf-8')
												Content = child6.get("Content-Id")
												folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"+child5.get("Name")+"/"
												for filename in filenames:
													if filename == Content:
														os.rename(folder+"/"+filename, folder_end+Name)
												        	print filename+" --> "+folder_end+Name
									else:
										Name = child5.get("Name").encode('utf-8')
										Content = child5.get("Content-Id")
										folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"+child4.get("Name")+"/"
										for filename in filenames:
											if filename == Content:
												os.rename(folder+"/"+filename, folder_end+Name)
							                                       	print filename+" --> "+folder_end+Name
						else:					#Jezeli jest to Plik
							Name = child4.get("Name").encode('utf-8')
							Content = child4.get("Content-Id")
							folder_end = folder+"/"+child.get("Type")+"/"+child3.get("Name")+"/"
							for filename in filenames:
								if filename == Content:
									os.rename(folder+"/"+filename, folder_end+Name)
									print filename+" --> "+folder_end+Name
