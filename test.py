"""
2025/03/30
测试并创建json文件
并在其中添加两个用户信息
"""

import json

file_path = "users.json"
data = {"Steven":
            {"username": "Steven",
             "password": 123,
             "score": 1},
        "Steven2":
            {"username": "Steven",
             "password": 123,
             "score": 1},
        }


with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)



print(f"文件 {file_path} 已创建。")
