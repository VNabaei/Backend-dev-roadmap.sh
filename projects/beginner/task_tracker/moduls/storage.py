import json

def WriteFileJSON(input_data) :
    with open ("---------------","w",enconding="utf-8") as f:
        json.dump(input_data , f, ensure_ascii=False,indent=4)  
                         
def ReadFileJSON(file_path):
    with open (file_path,"r") as f : 
        json.load(f)
        
    