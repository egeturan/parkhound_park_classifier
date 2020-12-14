import xml.etree.ElementTree as ET 
import os



def getReadLocationData(park_id):
    park_dict = {"0" : [1, 2, 3, 4]}
    tree = ET.parse('data/testmoment'+ str(park_id) + '.xml') 
    root = tree.getroot() 
      
    box_count = 0
    for child in root:
        if str(child.tag) == "object":
            box_count = box_count + 1
            for element in child:
                if str(element.tag) == "bndbox":
                    #print("Box ID:" + str(box_count))
                    xmin = element.find("xmin").text
                    ymin = element.find("ymin").text
                    xmax = element.find("xmax").text
                    ymax = element.find("ymax").text
                    park_dict[str(box_count)] = [xmin, ymin, xmax, ymax]
    
    print("Number of boxes are: " + str(box_count))
    return park_dict, box_count
