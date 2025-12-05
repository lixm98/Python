import pandas as pd
import math
data = pd.Series([84, 80, 71, 65, 64, 62, 84, 73, 71, 72])
print(sorted(data, reverse=True))
print(data.median())
print(data.mode()[0])
print(round(math.sqrt(122.2), 2))
