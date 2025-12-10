import pandas as pd

# 读取你之前生成的 2009 数据
df = pd.read_csv('nyc_noise_extracted_2009.csv')

# 定义噪音列和它们好看的名字
noise_sources = {
    'noiseneighbors': 'Neighbors (邻居)',
    'noisetraffic': 'Traffic (交通)',
    'noiseconstruction': 'Construction (施工)',
    'noisesirens': 'Sirens (警笛)',
    'noisestreet': 'Street People (街头行人)',
    'noisesubway': 'Subway (地铁)',
    'noiserestaurant': 'Restaurants/Bars (餐馆酒吧)',
    'noiseanimals': 'Animals (动物)'
}

results = []

print("正在统计噪音来源...\n")

for col, name in noise_sources.items():
    if col in df.columns:
        # 统计 Yes (1.0) 的数量
        # 注意：有些数据可能是空值，不算在分母里
        valid_responses = df[col].dropna()
        total = len(valid_responses)
        yes_count = (valid_responses == 1.0).sum()
        
        # 计算百分比
        percentage = (yes_count / total) * 100 if total > 0 else 0
        
        results.append({
            'Noise Source': name,
            'Yes Count': int(yes_count),
            'Total Responses': int(total),
            'Percentage (%)': round(percentage, 1)
        })

# 转成 DataFrame 并按百分比降序排列
final_df = pd.DataFrame(results).sort_values('Percentage (%)', ascending=False)

# 打印预览
print(final_df.to_string(index=False))

# 保存为 CSV
final_df.to_csv('noise_ranking.csv', index=False)
print("\n✅ 已保存为 noise_ranking.csv，去桌面看看吧！")