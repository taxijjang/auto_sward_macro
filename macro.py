import pyautogui as pag
import mss, cv2, time
import PIL as ImageGrab
import numpy as np

pag.PAUSE = 0.078
# nox
# icon position 노트북
# left_icon_pos = {'left': 148, 'top': 717, 'width': 85, 'height': 85}
# right_icon_pos = {'left': 357, 'top': 717, 'width': 85, 'height': 85}
#
# # button position
# left_button = [100, 900]
# right_button = [500, 900]


# icon position 본체
left_icon_pos = {'left': 140, 'top': 708, 'width': 85, 'height': 85}
right_icon_pos = {'left': 346, 'top': 708, 'width': 85, 'height': 85}

# button position
left_button = [100, 900]
right_button = [500, 900]


def what_type_is_image(img):
    img_rgb = np.mean(img, axis=(0, 1))

    ### sward 254, 108, 254
    if img_rgb[0] > 250 and img_rgb[0] < 256 \
            and img_rgb[1] > 100 and img_rgb[1] < 130 \
            and img_rgb[2] > 250 and img_rgb[2] < 256:
        return "SWARD"

    ### boom 63, 63 ,63
    elif img_rgb[0] > 60 and img_rgb[0] < 70 \
            and img_rgb[1] > 60 and img_rgb[1] < 70 \
            and img_rgb[2] > 60 and img_rgb[2] < 70:
        return "BOOM"

    ### poison 134, 177 ,120
    elif img_rgb[0] > 130 and img_rgb[0] < 140 \
            and img_rgb[1] > 170 and img_rgb[1] < 185 \
            and img_rgb[2] > 115 and img_rgb[2] < 125:
        return "POISON"

    elif img_rgb[0] > 220 and img_rgb[0] < 230 \
            and img_rgb[1] > 220 and img_rgb[1] < 230 \
            and img_rgb[2] > 145 and img_rgb[2] < 155:
        return "BONUS"

    return None


def mean(img):
    return np.mean(img, axis=(0, 1))


def click(loc):
    pag.moveTo(x=loc[0], y=loc[1], duration=0.0)
    pag.mouseDown()
    pag.mouseUp()


if __name__ == "__main__":
    bonus_check = False

    while True:
        with mss.mss() as sct:
            left_img = np.array(sct.grab(left_icon_pos))[:, :, :3]
            right_img = np.array(sct.grab(right_icon_pos))[:, :, :3]

            left_icon = what_type_is_image(left_img)
            right_icon = what_type_is_image(right_img)

            print("left_mean = {} , right_mead = {}".format(mean(left_img), mean(right_img)))
            if left_icon is "SWARD":
                pag.click(x=left_button[0], y=left_button[1], clicks=1)
                #click(left_button)
                bonus_check = False
                print(f"left = {left_icon}, mean = {mean}")
            else:
                print(f"left = {left_icon}")

            if right_icon is "SWARD":
                pag.click(x=right_button[0], y= right_button[1], clicks=1)
                #click(right_button)
                bonus_check = False
                print(f"right = {right_icon}, mean = {mean}")
            else:
                print(f"right = {right_icon}")

            if left_icon is "BOUNS" or right_icon is "BONUS":
                bouns_start_time = time.time()

                if bonus_check is False:
                    while time.time() - bouns_start_time < 5.3:
                        print(f"{time.time()}, {bouns_start_time}")
                        pag.click(x=right_button[0], y=right_button[1], clicks=1)
                        bonus_check = True

                else:
                    pag.click(x=right_button[0], y= right_button[1], clicks=1)
