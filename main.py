from utilities import *

with open('jsonfile.json') as user_file:
  parsed_json = json.load(user_file)
  
plants = parsed_json["Model"]["Networks"][0]["Plants"]
n = len(plants)


folder_name = "result"
extension_JSON = "json"
extension_TXT = "txt"
json_array = plants
attribute = "PlantName"


def create(folder_name, extension, json_array, attribute):
  
  if extension in SUPPORTED_TYPES:
    
  
    folder = make_check_folder(folder_name, extension)
    
    for index in range (len(json_array)):
      file_name = create_file_name(extension, json_array, index, attribute)
      modified_data = parsed_json
      modified_data["Model"]["Networks"][0]["Plants"] = [json_array[index]]
      parsed_data = return_file_object(extension, modified_data)
      
      f = open_file("{0}/{1}".format(folder, file_name))
      f.write(parsed_data)
      f.close()
  else:
    print("---------------> TYPE NOT SUPPORTED <-----------------")
    
create(folder_name, extension_JSON, plants, attribute)
create(folder_name, extension_TXT, plants, attribute)