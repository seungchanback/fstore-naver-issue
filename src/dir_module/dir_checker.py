"""csv 의 row를 돌면서 검사하는 모듈
"""

def is_number(check_string):

    try:
        float(check_string)
        return True
    except:
        return False

def is_integer(number_string) :

    if number_string.isdigit() or number_string[1:].isdigit():
        return True
    else:
        return False


def check_keyword_filename(row, filename, filepath):
    """row 의 keyword 와 filename 이 일치하는지 확인

    Args:
        row (Dict)
        filename (String): 파일이름
        filepath (String): 파일위치
    """

    try:
        row['keyword']
    except KeyError:
        print(f"[CHECK_NULL_KEYWORD] PATH : {filepath} ")
        return None

    if row['keyword'] != filename:
        print(f"[CHECK_KEYWORD_FILENAME] PATH : {filepath} ")
        print(f"[CHECK_KEYWORD_FILENAME] filename : {filename} ")
        print(f"[CHECK_KEYWORD_FILENAME] row_keyword : {row['keyword']} ")
    
    return None
        

def check_column(row,filepath, first_row_keys):
    """csv 로 읽은 파일의 내용은 모두 string 입니다. csv 타입과 동일하지 않은 row 를 탐색합니다.


    Args:
        row (Dict)
    """

    for key in first_row_keys:
        try:
            if row[key] == None:
                print(f"[CHECK_COLUMN] PATH : {filepath} ")
                print(f"[CHECK_COLUMN] row : {row['keyword']} ")
                print(f"[CHECK_COLUMN] key : {key} ")
                break
        except KeyError:
            print(f"[CHECK_COLUMN] PATH : {filepath} ")
            print(f"[CHECK_COLUMN] row : {row} ")
            print(f"[CHECK_COLUMN] key : {key} ")
            break
            
    return None

# def check_int_float(first_row, current_row, filepath):
#     """첫번째 row와 현재 row 의 숫자 타입을 비교합니다.
#     - 데이터의 형태가 너무 달라서 해당 함수는 시행하지 않습니다

#     Args:
#         previous_row (Dict)
#         current_row (Dict)
#         first_row_keys (List)
#     """
#     first_row_keys = first_row.keys()

#     for key in first_row_keys:
        
#         current_row_key_value = current_row[key]
#         first_row_key_value = first_row[key]
        
#         #특정 키의 값이있으면 PASS
#         if current_row_key_value == None or (len(current_row_key_value) ==0):
#             continue

#         # 첫번째 줄은 숫자였는데, 다음 줄은 문자인 경우 혹은 그반대
#         if is_number(first_row_key_value) != is_number(current_row_key_value):
#             print(f"[CHECK_INT_FLOAT] PATH : {filepath} ")
#             print(f"[CHECK_INT_FLOAT] key : {key} ")
#             print(f"[CHECK_INT_FLOAT] first_row_key : {first_row_key_value} ")
#             print(f"[CHECK_INT_FLOAT] current_row : {current_row} ")
#             continue

#         # 첫번째 줄은 int였는데, 다음 줄은 float 인 경우 혹은 그반대
#         if is_integer(first_row_key_value) != is_integer(current_row_key_value):
#             print(f"[CHECK_INT_FLOAT] PATH : {filepath} ")
#             print(f"[CHECK_INT_FLOAT] key : {key} ")
#             print(f"[CHECK_INT_FLOAT] first_row_value : {first_row_key_value} ")
#             print(f"[CHECK_INT_FLOAT] current_row : {current_row} ")

#     return None

def check_rank(csv_dict, filepath): 
    """rank 가 200 이상인 row 를 확인합니다.
    rank 는 출력의 수가 많아 csv 파일을 대상으로합니다.

    Args:
        csv_dict (CSVDict)

    """
    
    
        

    for row in csv_dict:

        try:
            int(row['rank'])
        except ValueError:
            print(f"[CHECK_RANK] PATH : {filepath} Keyword NULL ")
            break

        if int(row['rank']) > 200:
            print(f"[CHECK_RANK] PATH : {filepath} ")
            print(f"[CHECK_RANK] rank : {row['rank'] } ")
            break
    
    return None

def check_null_keyword(row,filepath):
    """keyword 값이 null 이거나 비어있는 row 를 확인합니다.

    Args:
        row (Dict): 
        filepath (String): 
    """
    try:
        row['keyword']
    except KeyError:
        print(f"[CHECK_NULL_KEYWORD] PATH : {filepath} ")
        return None
        
    if row['keyword'] == None or (len(row['keyword'])==0):
        print(f"[CHECK_NULL_KEYWORD] PATH : {filepath} ")
    
    return None            
