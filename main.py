"""
外星人入侵游戏入口

运行此文件启动游戏。
"""

from alien_invasion import AlienInvasion


def main():
    """游戏主入口函数"""
    ai_game = AlienInvasion()
    ai_game.run_game()


if __name__ == "__main__":
    main()
