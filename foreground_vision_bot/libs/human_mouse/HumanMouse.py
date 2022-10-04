from time import sleep
from random import uniform, randint
import win32api, win32con, win32gui

from libs.human_mouse.HumanCurve import HumanCurve


class HumanMouse:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.window_rect = win32gui.GetWindowRect(self.hwnd)

    def move(self, to_point, duration=0.5, like_robot=False):
        """
        Move mouse from current mouse position to a given point, in a human way or like a robot.
        :param to_point: tuple (x, y)
        :param duration: float. Time in seconds for the movement.
        :param like_robot: bool.
        """

        if like_robot:
            win32api.SetCursorPos(to_point)
            sleep(0.05)
            return

        from_point = win32api.GetCursorPos()
        human_curve = HumanCurve(from_point, to_point, targetPoints=25)
        for point in human_curve.points:
            win32api.SetCursorPos((int(round(point[0])), int(round(point[1]))))
            sleep(round(duration / len(human_curve.points), 3))

    def move_outside_game(self, duration=0.5, like_robot=False):
        """
        Move mouse outside the game window.
        :param duration: float. Time in seconds for the movement.
        :param like_robot: bool.
        """
        self.move(self.__get_random_outside_point(), duration, like_robot)

    def left_click(self):
        """
        Left click mouse at current mouse position. It uses a random time 
        to simulate a human click.
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(round(uniform(0.015, 0.03), 4))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        sleep(round(uniform(0.015, 0.03), 4))

    def double_left_click(self):
        self.left_click()
        self.left_click()

    def drag_left_click(self, to_point, duration=0.5, like_robot=False):
        """
        Drag mouse from current mouse position to a given point, in a human way or like a robot.
        :param to_point: tuple (x, y)
        :param duration: float. Time in seconds for the movement.
        :param like_robot: bool.
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(round(uniform(0.015, 0.03), 4))
        self.move(to_point, duration, like_robot)
        sleep(round(uniform(0.015, 0.03), 4))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        sleep(round(uniform(0.015, 0.03), 4))

    def right_click(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        sleep(round(uniform(0.015, 0.03), 4))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        sleep(round(uniform(0.015, 0.03), 4))

    def double_right_click(self):
        self.right_click()
        self.right_click()

    def drag_right_click(self, to_point, duration=0.5, like_robot=False):
        """
        Drag mouse from current mouse position to a given point, in a human way or like a robot.
        :param to_point: tuple (x, y)
        :param duration: float. Time in seconds for the movement.
        :param like_robot: bool.
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        sleep(round(uniform(0.015, 0.03), 4))
        self.move(to_point, duration, like_robot)
        sleep(round(uniform(0.015, 0.03), 4))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        sleep(round(uniform(0.015, 0.03), 4))

    def scroll(self, isUp=True, times=1):
        """
        Scroll mouse wheel. 
        :param isUp: Bool. True for up, False for down.
        """
        for _ in range(times):
            if isUp:
                win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 120)
            else:
                win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -120)
            sleep(round(uniform(0.015, 0.03), 4))

    def __get_random_outside_point(self):
        random_left = (self.window_rect[0], randint(self.window_rect[1], self.window_rect[3]))
        random_top = (randint(self.window_rect[0], self.window_rect[2]), self.window_rect[1])
        random_right = (self.window_rect[2], randint(self.window_rect[1], self.window_rect[3]))
        random_bottom = (randint(self.window_rect[0], self.window_rect[2]), self.window_rect[3])

        outside_points = (
            random_left,
            random_top,
            random_right,
            random_bottom,
        )
        return outside_points[randint(0, len(outside_points) - 1)]