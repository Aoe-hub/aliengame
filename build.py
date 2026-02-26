"""
游戏打包脚本

使用 PyInstaller 将游戏打包成可执行文件。
支持 Windows、macOS 和 Linux。

使用方法:
    python build.py
"""

import os
import shutil
import subprocess
import sys


def check_dependencies():
    """检查是否安装了必要的依赖"""
    try:
        import pygame
        print(f"[OK] pygame {pygame.__version__} 已安装")
    except ImportError:
        print("[ERROR] pygame 未安装，正在安装...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    try:
        import PyInstaller
        print(f"[OK] PyInstaller {PyInstaller.__version__} 已安装")
    except ImportError:
        print("[ERROR] PyInstaller 未安装，正在安装...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])


def clean_build():
    """清理之前的构建文件"""
    build_dirs = ['build', 'dist']
    for directory in build_dirs:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"[OK] 已清理 {directory} 目录")


def build():
    """执行打包"""
    print("\n" + "=" * 50)
    print("开始打包 Alien Invasion 游戏...")
    print("=" * 50 + "\n")

    # 检查依赖
    check_dependencies()

    # 清理旧构建
    clean_build()

    # 检查图标文件
    icon_file = None
    for icon in ['icon.ico', 'icon.icns', 'icon.png']:
        if os.path.exists(icon):
            icon_file = icon
            print(f"[OK] 使用图标文件：{icon}")
            break

    # 执行 PyInstaller
    spec_file = "alien_invasion.spec"
    cmd = [sys.executable, "-m", "PyInstaller", "--clean", "-y", spec_file]

    # 如果有图标文件，添加图标参数
    if icon_file:
        cmd.insert(-1, f"--icon={icon_file}")

    print(f"\n执行命令：{' '.join(cmd)}\n")

    try:
        subprocess.check_call(cmd)
        print("\n" + "=" * 50)
        print("[OK] 打包完成!")
        print("=" * 50)
        print("\n可执行文件位置：dist/AlienInvasion/")

        if sys.platform == 'win32':
            print(f"Windows 可执行文件：dist/AlienInvasion/AlienInvasion.exe")
        elif sys.platform == 'darwin':
            print(f"macOS 应用：dist/AlienInvasion/AlienInvasion.app")
        else:
            print(f"Linux 可执行文件：dist/AlienInvasion/AlienInvasion")

        print("\n提示：dist/AlienInvasion 目录包含所有需要的文件，可以整体分发给用户。")

    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] 打包失败：{e}")
        sys.exit(1)


if __name__ == "__main__":
    build()
