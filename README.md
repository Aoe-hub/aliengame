# 外星人入侵 (Alien Invasion)

一个经典的太空射击游戏，使用 Python 和 Pygame 开发。

## 游戏说明

控制飞船左右移动并射击外星人，防止外星人到达屏幕底部。

### 操作方式

| 按键 | 功能 |
|------|------|
| ← | 向左移动 |
| → | 向右移动 |
| 空格 | 发射子弹 |
| Q | 退出游戏 |

### 游戏规则

1. 点击 "Play" 按钮开始游戏
2. 消灭所有外星人进入下一关
3. 每关外星人速度会增加
4. 飞船被撞击或外星人到达底部会损失一艘飞船
5. 初始有 3 艘飞船

## 运行游戏

### 方法一：直接运行（需要 Python 环境）

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行游戏
python main.py
```

### 方法二：运行可执行文件（无需 Python 环境）

打包后可执行文件位于 `dist/AlienInvasion/` 目录。

## 打包游戏

### 自动打包（推荐）

```bash
# 1. 安装依赖
pip install -r requirements.txt
pip install pyinstaller

# 2. 运行打包脚本
python build.py
```

打包完成后，可执行文件位于 `dist/AlienInvasion/` 目录。

### 手动打包

```bash
# Windows
pyinstaller --onefile --windowed --name AlienInvasion --add-data "images;images" main.py

# macOS
pyinstaller --onefile --windowed --name AlienInvasion --add-data "images:images" main.py

# Linux
pyinstaller --onefile --windowed --name AlienInvasion --add-data "images:images" main.py
```

### 添加游戏图标（可选）

将图标文件放在项目根目录：
- Windows: `icon.ico`
- macOS: `icon.icns`
- Linux: `icon.png` (256x256)

然后运行：
```bash
python build.py
```

## 项目结构

```
aliengame/
├── main.py              # 游戏入口
├── alien_invasion.py    # 游戏主逻辑
├── settings.py          # 游戏设置
├── ship.py              # 飞船类
├── alien.py             # 外星人阶级
├── bullet.py            # 子弹类
├── button.py            # 按钮类
├── game_stats.py        # 游戏统计
├── scoreboard.py        # 记分牌
├── utils.py             # 工具函数（资源路径处理）
├── build.py             # 打包脚本
├── requirements.txt     # 依赖列表
├── alien_invasion.spec  # PyInstaller 配置
├── images/              # 游戏图片资源
│   ├── ship.bmp
│   └── alien.bmp
└── highscore.json       # 最高分记录
```

## 跨平台分发

打包完成后，`dist/AlienInvasion/` 目录包含所有需要的文件：

- **Windows**: 分发整个 `dist/AlienInvasion/` 文件夹
- **macOS**: 分发 `dist/AlienInvasion/AlienInvasion.app`
- **Linux**: 分发 `dist/AlienInvasion/AlienInvasion` 可执行文件

**注意**: 需要在对应平台上进行打包，才能生成该平台的可执行文件。

## 系统要求

- Python 3.8+
- pygame 2.5+
- 操作系统：Windows 7+/macOS 10.12+/Linux

## 开发信息

基于《Python 编程：从入门到实践》项目改编优化。

## 许可证

MIT License
