import os
from re import S
from src import s3
from src.s3 import s3_resource

def s3_download(year, month, day, downloaded_path):
    """downloaded_path 에 년,월,일 객체 받아오는 함수

    Args:
        year (String) 
        month (String)
        day (String)
    """
    
    bucket = s3_resource.Bucket(s3.config['AWS']['TARGET_BUCKET'])
    prefix = f'cData_day2/{year}/{month}/{day}/'
    
    for object in bucket.objects.filter(Prefix = prefix):
        
        destination_path = os.path.abspath(downloaded_path+'/'+object.key)
    
        if not os.path.exists(os.path.dirname(destination_path)):
            os.makedirs(os.path.dirname(destination_path))

        if object.key == prefix:
            os.makedirs(os.path.dirname(object.key), exist_ok=True)
            continue;

        bucket.download_file(object.key, destination_path)
    
    return None