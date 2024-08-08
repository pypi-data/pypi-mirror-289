import json
from deepdiff import DeepDiff

def load_json_by_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_json_by_str(json_str):
    return json.loads(json_str)

def output_json_by_dict(dict_obj):
    return json.dumps(dict_obj)
    
def compare_json(file1, file2):
    '''有差异返回差异结果，没有差异返回None'''
    json1 = load_json_by_file(file1)
    json2 = load_json_by_file(file2)
    
    diff = DeepDiff(json1, json2, ignore_order=True)
    if diff:
        return format_diff(diff)
    else:
        return None

def format_diff(diff):
    formatted_diff = []
    for diff_type, changes in diff.items():
        formatted_diff.append(f"差异类型: {diff_type}")
        if isinstance(changes, dict):
            for change, detail in changes.items():
                formatted_diff.append(f"  {change}: {detail}")
        elif isinstance(changes, list):
            for change in changes:
                formatted_diff.append(f"  {change}")
        else:
            formatted_diff.append(f"  {changes}")
    return "\n".join(formatted_diff)

if __name__ == "__main__":
    file1 = r'C:\Users\luohao\Desktop\fsdownload\20240730.json'
    file2 = r'C:\Users\luohao\Desktop\fsdownload\20240807.json'
    
    differences = compare_json(file1, file2)
    
    if differences:
        print("两个JSON文件之间的差异如下：")
        print(differences)
    else:
        print("两个JSON文件没有差异。")
