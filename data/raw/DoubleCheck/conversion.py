import pandas as pd
import os
import json

# 读取CSV文件
csv_file = 'LTCR.csv'
data = pd.read_csv(csv_file)

# 创建文件夹
os.makedirs('fake', exist_ok=True)
os.makedirs('real', exist_ok=True)

# 遍历每一行
for index, row in data.iterrows():
    # 只处理label为0或1的行
    if row['label'] in [0, 1]:
        json_data = {
            "kids": [],
            "uid": str(row['id']),
            "parent": "",
            "text": row['text'],  # 这里可以根据需要调整
            "mid": str(row['id']),  # 假设mid与id相同
            "date": row['time']
        }

        # 根据label值决定存放的文件夹
        if row['label'] == 0:
            file_path = f'fake/{row["id"]}.json'
        else:
            file_path = f'real/{row["id"]}.json'

            # 写入JSON文件
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print("JSON文件生成完毕！")