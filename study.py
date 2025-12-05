import pandas as pd
import math
# 测试改动
data = pd.Series([84, 80, 71, 65, 64, 62, 84, 73, 71, 72])
print(sorted(data, reverse=True))
# 测试Sourcetree
print(data.median())
print(data.mode()[0])
print(round(math.sqrt(122.2), 2))
