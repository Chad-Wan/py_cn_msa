import pandas as pd
from datetime import datetime

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [25, 30, 28, 35],
    "城市": ["北京", "上海", "广州", "深圳"]
}, index=["a", "b", "c", "d"])

# print(df)
print(df.loc[df['姓名'] == "张三", "年龄"].values[0])
print(type(df.loc[df['姓名'] == "张三", "年龄"]))

date_time_str = "2026 09 23 04 46 51"
date_time = datetime(2026,9, 23, 4, 46, 51)

print(date_time)