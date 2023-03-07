import json 
import os


JSON = "json"
TXT = "txt"

SUPPORTED_TYPES = [JSON, TXT]

def make_check_folder(folder_name, extension):
  try:
    os.mkdir(folder_name + "_" + extension)
  except:
    print ("{}_{} path exist".format(folder_name, extension))
  finally:
    return folder_name + "_" + extension
    
  
def create_file_name(extension, json_array, index, attribute):
  file_name = ("result_{0}_".format(extension)) + json_array [index][attribute]
  #removing spaces if there are any
  file_name = file_name.replace(" ", "_")
  return file_name


def return_file_object(extension, data):
  
  if extension == JSON:
    return json.dumps(data, indent = 4)
  elif extension == TXT:
    return str(data)
  


def open_file(file_name):
    try:
      return open(file_name, "x")
    except:
      return open(file_name, "w")
 
 
