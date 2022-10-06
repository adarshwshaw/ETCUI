from settings import Engine

def util_row_to_dict(list):
    result=[]
    for row in list:
        result.append(dict(row))
    return result

