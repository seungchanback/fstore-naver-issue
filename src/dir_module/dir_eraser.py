import os
import shutil

def erase(erase_target_path):
    """erase_target_path 에 해당하는 폴더를 강제로 지웁니다.

    Args:
        erase_target_path (String): 지워지는 대상이 되는 폴더
    """
    
    destination_path = os.path.abspath(erase_target_path)
    shutil.rmtree(destination_path)

    return None
