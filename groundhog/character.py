import time

import pyautogui as gui

class Character:

    # TODO: can be a display specific value
    PIXELS_DRUG_TO_FULL_TURN = 1600

    def __init__(self) -> None:
        self._screen_width, self._screen_height = gui.size()

    # TODO: consider turning using /script FlipCameraYaw(180) instead
    def turn(self, degree: int) -> None:
        degree = degree % 360
        if degree < 0:
            degree = 360 - degree

        pixels_to_turn = degree / 360 * self.PIXELS_DRUG_TO_FULL_TURN

        # Move mous to most left center
        self._move_mouse_to_center(x=0)
        self._drag(x_offset=pixels_to_turn, y_offset=0, button=gui.RIGHT)

    # TODO: async?
    # Holding 2 mouse buttons move your character towards current direction
    def move(self, seconds: int) -> None:
        self._move_mouse_to_center(x=0)
        gui.mouseDown(button=gui.LEFT)
        gui.mouseDown(button=gui.RIGHT)
        time.sleep(seconds)
        gui.mouseUp(button=gui.LEFT)
        gui.mouseUp(button=gui.RIGHT)

    def cast(self, keybind: str):
        gui.press(keybind)
        # TODO: detect cast bar using CV and don't use hardcoded value
        time.sleep(2)

    # TODO: detect target selected using CV and return bool to identify it
    def target(self):
        gui.press('tab')

    def _drag(self, x_offset: int, y_offset: int, button: str) -> None:
        gui.mouseDown(button=button)
        gui.moveRel(xOffset=x_offset, yOffset=y_offset)
        gui.mouseUp(button=button)

    def _move_mouse_to_center(self, x=None, y=None) -> None:
        final_x = x if x is not None else self._screen_width / 2
        final_y = y if y is not None else self._screen_height / 2
        gui.moveTo(x=final_x, y=final_y)
