import pandas as pd

# 读取数据
df = pd.read_csv('nyc_noise_extracted_2011.csv')

# 统计 noise9 (地铁/公交) 的每天人数
noise9_counts = df['noise9'].value_counts().sort_index()

# 统计 noise11 (耳机) 的每天人数
noise11_counts = df['noise11'].value_counts().sort_index()

# 统计 trafficnoisedays (街道交通) 的每天人数
# 注意：如果这个变量是分类代码(1,2,3)，统计结果将显示代码而非天数
traffic_counts = df['trafficnoisedays'].value_counts().sort_index()

print("--- 地铁/公交噪音 (noise9) ---")
print(noise9_counts)
print("\n--- 耳机使用 (noise11) ---")
print(noise11_counts)
print("\n--- 街道交通噪音 (trafficnoisedays) ---")
print(traffic_counts)