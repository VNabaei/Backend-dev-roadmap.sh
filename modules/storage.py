import csv
import os

#region : function

def read_csv(path) :
    if not os.path.exists(path):
        return []
    with open(path,"r",encoding = "utf-8") as f :
        return list(csv.DictReader(f))
    
def totalwrite_csv(path,fieldnames,rows = []) -> csv:
    #NOTE : this function write a csv file, if file is exist, then it is rewrite.
    '''
    This function writes the file completely from the beginning.
    
    Parametr(s) :
    -------------
    path : str,
        the path of file that will writen
    fieldnames : list,
        the fiels of file
    rows : dictionary
        the data that ypu want to save in csv file
        
    Return(s):
    ---------
    csv :  file
    
    '''
    # if not os.path.exists(path):
    #     raise FileNotFoundError(f"{path} does not exist.")

   
    with open(path,"w",newline="",encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
def write_csv(path,fieldnames,rows):
    '''
    '''
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist.")

    else :
        with open (path,"a",newline="",encoding="utf-8") as f:
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            if f.tell() == 0:  
                writer.writeheader()
        
            writer.writerows(rows)