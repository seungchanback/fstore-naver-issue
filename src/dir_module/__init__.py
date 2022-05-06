import os
import csv
import glob

from src.dir_module import dir_checker

def check_dir(target_path):
    
    destination_path = os.path.abspath(target_path)
    
    for filepath in glob.iglob(destination_path + '/**/*.csv', recursive=True):

        basename = os.path.basename(filepath)
        filename = os.path.splitext(basename)[0]

        csv_file = open(filepath, 'r', encoding='utf-8')
        csv_dict = csv.DictReader(csv_file)
        
        first_row = None

        dir_checker.check_rank(csv_dict,filepath)
        
        #generator copy 가 안되기 때문에 두번 호출
        csv_file = open(filepath, 'r', encoding='utf-8')
        csv_dict = csv.DictReader(csv_file)        

        for index, row in enumerate(csv_dict):
            
            if index == 0:
                first_row = row
                
            dir_checker.check_column(row,filepath,first_row.keys())
            dir_checker.check_null_keyword(row,filepath)
            dir_checker.check_keyword_filename(row,filename,filepath)
            
            #dir_checker.check_int_float(first_row,row,filepath)
            
