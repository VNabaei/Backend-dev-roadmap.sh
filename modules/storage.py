"""
Storage Module
==============

This module provides helper functions for reading and writing CSV files.

It includes functions to:
    - Read CSV files into a list of dictionaries
    - Write or overwrite CSV files
    - Append data to existing CSV files

------------------------------
Functions
------------------------------

1. read_csv(path)
   - Reads a CSV file from the given path.
   - Returns a list of dictionaries representing each row.
   - If the file does not exist, returns an empty list.

2. totalwrite_csv(path, fieldnames, rows=[])
   - Completely overwrites or creates a CSV file.
   - Parameters:
       * path : str : Path to the CSV file
       * fieldnames : list : Column headers
       * rows : list of dict : Data to write
   - Returns the written CSV file.

3. write_csv(path, fieldnames, rows)
   - Appends rows to an existing CSV file.
   - If the file does not exist, raises FileNotFoundError.
   - Writes headers if the file is empty.

------------------------------
Notes
------------------------------

- All files are handled with UTF-8 encoding.
- The module ensures CSV integrity by using DictWriter.

ماژول Storage
==============

این ماژول شامل توابع کمکی برای خواندن و نوشتن فایل‌های CSV است.

شامل توابعی برای:
    - خواندن فایل CSV به صورت لیست دیکشنری‌ها
    - نوشتن یا بازنویسی کامل فایل CSV
    - اضافه کردن داده‌ها به فایل CSV موجود

------------------------------
توابع
------------------------------

1. read_csv(path)
   - خواندن فایل CSV از مسیر مشخص شده
   - خروجی: لیستی از دیکشنری‌ها که هر ردیف را نشان می‌دهد
   - در صورت عدم وجود فایل، لیست خالی بازگردانده می‌شود

2. totalwrite_csv(path, fieldnames, rows=[])
   - بازنویسی کامل یا ایجاد یک فایل CSV
   - پارامترها:
       * path : str : مسیر فایل CSV
       * fieldnames : list : سرستون‌ها
       * rows : list of dict : داده‌های مورد نظر برای ذخیره
   - خروجی: فایل CSV نوشته شده

3. write_csv(path, fieldnames, rows)
   - اضافه کردن ردیف‌ها به فایل CSV موجود
   - اگر فایل وجود نداشته باشد، FileNotFoundError ایجاد می‌کند
   - در صورت خالی بودن فایل، سرستون‌ها نوشته می‌شوند

------------------------------
نکات
------------------------------

- همه فایل‌ها با UTF-8 ذخیره و خوانده می‌شوند
- ماژول از DictWriter برای حفظ یکپارچگی CSV استفاده می‌کند
"""

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