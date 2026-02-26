"""
游戏图标生成脚本

生成用于打包的游戏图标文件。
"""

import os

# 检查 images 目录是否存在
images_dir = os.path.join(os.path.dirname(__file__), 'images')
if not os.path.exists(images_dir):
    os.makedirs(images_dir)
    print(f"已创建 images 目录：{images_dir}")

# 提示用户添加图标文件
icon_instructions = """
========================================
图标文件说明
========================================

请准备以下图标文件之一：

1. Windows: 将 icon.ico 放在项目根目录
2. macOS: 将 icon.icns 放在项目根目录  
3. Linux: 将 icon.png (256x256) 放在项目根目录

如果没有图标文件，游戏将使用默认图标。

可以使用在线工具生成图标：
- https://www.icoconverter.com/
- https://convertio.co/zh/png-ico/

========================================
"""

print(icon_instructions)

# 检查现有图标
icon_files = ['icon.ico', 'icon.icns', 'icon.png']
for icon in icon_files:
    icon_path = os.path.join(os.path.dirname(__file__), icon)
    if os.path.exists(icon_path):
        print(f"✓ 找到图标文件：{icon}")
    else:
        print(f"✗ 未找到图标文件：{icon}")
