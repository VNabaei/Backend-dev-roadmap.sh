import json

def WriteFileJSON(input_data) :
    with open ("---------------","w",enconding="utf-8") as f:
        json.dump(input_data , f, ensure_ascii=False,indent=4)  
                         
def ReadFileJSON(file_path):
    with open (file_path,"r") as f : 
        data =json.load(f)
        return data
    
# CRUD operations
    
def get_next_id(file_path):
    data = ReadFileJSON(file_path)
    if not data:
        return 1
    max_id = max(item["ID"] for item in data)
    return max_id + 1

def save_data(file_path, task):
    data = ReadFileJSON(file_path)
    data.append(task)
    WriteFileJSON(file_path, data)
    
    # این برسی شود
# def update_data(file_path, updated_task):
#     data = ReadFileJSON(file_path)
#     for index, item in enumerate(data):
#         if item["ID"] == updated_task["ID"]:
#             data[index] = updated_task
#             break
#     WriteFileJSON(file_path, data)
    
def delete_data(file_path, task_id):
    data = ReadFileJSON(file_path)
    data = [item for item in data if item["ID"] != task_id] 
    WriteFileJSON(file_path, data)              
    
    