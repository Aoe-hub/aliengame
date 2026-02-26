"""
资源路径工具模块

处理打包后的资源文件路径问题。
"""

import os
import sys


def get_resource_path(relative_path):
    """
    获取资源的绝对路径。
    
    对于开发环境，返回相对于项目根目录的路径。
    对于打包后的环境，返回相对于 _MEIPASS 的路径。
    
    Args:
        relative_path: 相对于项目根目录的资源路径
        
    Returns:
        资源的绝对路径
    """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller 创建的临时目录
        base_path = sys._MEIPASS
    else:
        # 开发环境
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)
