import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

x = np.linspace(-3, 3, 100)
y = stats.norm.pdf(x, 0, 1)

fig, ax = plt.subplots(figsize=(3, 3), dpi=300)
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)

ax.plot(x, y, color='#1A365D', linewidth=5)

ax.text(0, 0.02, 'Z.K', fontsize=40, fontweight='bold', 
        color= '#1A365D', ha='center', fontfamily='sans-serif')

ax.axis('off')

plt.savefig('logo.png', transparent=True, bbox_inches='tight', pad_inches=0)
print("恭喜！高清 favicon.png 已经生成在当前文件夹中。")

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 1. 生成正态分布数据
x = np.linspace(-3, 3, 100)
y = stats.norm.pdf(x, 0, 1)

# 2. 设置更紧凑的画布 (背景透明)
fig, ax = plt.subplots(figsize=(2, 2), dpi=300)
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)

# 3. 画出正态分布曲线 (线条极度加粗，保证缩小后可见)
ax.plot(x, y, color='#1A365D', linewidth=15)

# 4. 在下方添加名字缩写 (字体变得极大，去掉标点符号更清晰)
ax.text(0, 0.05, 'ZK', fontsize=65, fontweight='bold', 
        color='#1A365D', ha='center', fontfamily='sans-serif')

# 5. 隐藏坐标轴
ax.axis('off')

# 6. 保存为 favicon.png
plt.savefig('favicon.png', transparent=True, bbox_inches='tight', pad_inches=0.1)
print("恭喜！高清 favicon.png 已经生成在当前文件夹中。")