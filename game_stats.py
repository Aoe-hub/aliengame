"""
游戏统计信息模块

跟踪游戏的统计信息，如得分、等级和剩余飞船数。
"""

import json


class GameStats:
    """跟踪游戏统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏一开始处于非活动状态
        self.game_active = False

        # 最高得分不应该重置
        self.high_score = 0
        self._load_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """从文件加载最高得分"""
        try:
            with open("highscore.json", "r") as f:
                self.high_score = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            # 如果文件不存在或格式错误，尝试读取旧的 CSV 格式
            try:
                with open("highscore.csv", "r") as f:
                    self.high_score = int(f.read().strip())
            except (FileNotFoundError, ValueError):
                self.high_score = 0
