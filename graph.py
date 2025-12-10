import pandas as pd

# 读取 2011 年数据
df = pd.read_csv('nyc_noise_extracted_2011.csv')

print("正在计算贫富差距数据...\n")

# 1. 筛选有效数据
# 去掉 povertygroup 是空值或者 5,6 (通常是Refused/Don't Know) 的行
# 去掉 trafficnoisedays 是空值的行
# 假设 povertygroup 1-4 是有效范围
valid_data = df[
    (df['povertygroup'].isin([1.0, 2.0, 3.0, 4.0])) & 
    (df['trafficnoisedays'].notna())
]

# 2. 按贫困组分组，计算平均天数
result = valid_data.groupby('povertygroup')['trafficnoisedays'].mean().reset_index()

# 3. 把数字 1-4 翻译成好听的英文标签
income_labels = {
    1.0: 'Lowest Income (<200% Poverty Line)',
    2.0: 'Low-Middle Income',
    3.0: 'Middle-High Income',
    4.0: 'Highest Income (>600% Poverty Line)'
}
result['Income Group'] = result['povertygroup'].map(income_labels)

# 4. 整理列顺序，只留有用的
final_df = result[['Income Group', 'trafficnoisedays']]
final_df.columns = ['Income Group', 'Avg Days with Traffic Noise (per week)']

# 打印结果
print(final_df.to_string(index=False))

# 保存为 CSV
final_df.to_csv('chart_inequality.csv', index=False)
print("\n✅ 已保存为 chart_inequality.csv")