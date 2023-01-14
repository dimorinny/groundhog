import pyautogui as gui

class Character:

    # TODO: can be a display specific value
    PIXELS_DRUG_TO_FULL_TURN = 1600

    def __init__(self) -> None:
        self._screen_width, self._screen_height = gui.size()

    def turn(self, degree: int) -> None:
        degree = degree % 360
        if degree < 0:
            degree = 360 - degree

        pixels_to_turn = degree / 360 * self.PIXELS_DRUG_TO_FULL_TURN

        # Move mous to most left center
        self._move_mouse_to_center(x=0)
        self._drag(x_offset=pixels_to_turn, y_offset=0, button=gui.RIGHT)

    def _drag(self, x_offset: int, y_offset: int, button: str) -> None:
        gui.mouseDown(button=button, logScreenshot=None)
        gui.moveRel(xOffset=x_offset, yOffset=y_offset)
        gui.mouseUp(button=button, logScreenshot=None)

    def _move_mouse_to_center(self, x=None, y=None) -> None:
        final_x = x if x is not None else self._screen_width / 2
        final_y = y if y is not None else self._screen_height / 2
        gui.moveTo(x=final_x, y=final_y)
