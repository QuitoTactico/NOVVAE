import pyautogui as p
from pyperclip import paste
from time import sleep
from webbrowser import open_new_tab
import subprocess
from pywinauto import Desktop
from time import sleep


#     `7MN.   `7MF'
#       MMN.    M
#       M YMb   M   ,pW"Wq.  `7M'   `MF'`7M'   `MF' ,6"Yb.   .gP"Ya
#       M  `MN. M  6W'   `Wb   VA   ,V    VA   ,V  8)   MM  ,M'   Yb
#       M   `MM.M  8M     M8    VA ,V      VA ,V    ,pm9MM  8M""""""
#       M     YMM  YA.   ,A9     VVV        VVV    8M   MM  YM.    ,
#     .JML.    YM   `Ybmd9'       W          W     `Moo9^Yo. `Mbmmd'
#
#
#                     _                ___       _.--.
#                     \`.|\..----...-'`   `-._.-'_.-'`
#                     /  ' `         ,       _.-'
#                     )/' _/     \   `-_,   /
#                     `-'" `"\_  ,_.-;_.-\_ ',
#                         _.-'_./   {_.'   ; /
#                        {_.-``-'         {_/ v1.7.4


CHECK_POS = False

NOVVAE_2 = "https://www.youtube.com/playlist?list=PLV2hNo2SKdY3FA-HMN1xFlYEpp8P5BL9O"
NOVVAE_3 = "https://www.youtube.com/playlist?list=PLV2hNo2SKdY1b7zOrxEsdlCarJmUJvwdU"

ACTUAL_NOVVAE = NOVVAE_3

LIKES = "https://www.youtube.com/playlist?list=LL"
NOVVAE_REPO = "https://github.com/QuitoTactico/NOVVAE/"
PERSISTENCE_DIR = "./NOVVAE_PERSISTENCE.txt"

# ---------------clicklist--------------------


def pos():
    p.displayMousePosition()


def cerrar():
    p.moveTo(1344, 15, 0.2)
    p.click()


def minimizar():
    p.moveTo(1251, 13, 0.2)
    p.click()


def visual_old():
    p.moveTo(280, 755, 0.2)
    p.click()


def open_app(partial_title) -> bool:
    windows = Desktop(backend="uia").windows()
    for window in windows:
        if partial_title in window.window_text():
            window.set_focus()
            return True
    return False


def visual():
    if not open_app("Visual Studio Code"):
        subprocess.run(["code"])


def browser_old():
    p.moveTo(240, 755, 0.2)
    p.click()


def browser(name="Opera"):
    if not open_app(name):
        subprocess.run(["start", name.lower()], shell=True)


def pag_1():
    p.moveTo(165, 10, 0.2)
    p.click()


def pag_2():
    p.moveTo(360, 10, 0.2)
    p.click()


def pag_2_fast():
    p.moveTo(360, 10, 0.02)
    p.click()


def pag_3():
    p.moveTo(560, 10, 0.2)
    p.click()


def terminal():
    p.moveTo(660, 700, 0.2)
    p.click()


def refresh_link():
    p.moveTo(10, 700, 0.05)
    p.click()


def like_old():
    p.moveTo(620, 705, 0.2)
    p.click()


def like():
    imagen_click("like-icon")


def link():
    p.moveTo(660, 50, 0.05)
    p.click()


def cerrar_pag_1():
    p.moveTo(275, 18, 0.2)
    p.click()


def search_bar():
    p.moveTo(500, 184, 0.2)
    p.click()


# --------------image recognition---------------


def imagen_click(image, confidence=0.8, duration=0.2, region=None, minSearchTime=None):
    try:
        p.click(
            p.locateCenterOnScreen(
                f"media/{image}.png",
                confidence=confidence,
                region=region,
                minSearchTime=minSearchTime,
            ),
            duration=duration,
        )
    except:
        p.click(
            p.locateCenterOnScreen(
                f"media/{image}.png",
                confidence=0.75,
                region=region,
                minSearchTime=2,
            ),
            duration=duration,
        )


# -------------------options--------------------


def pasar():
    p.keyDown("shiftleft")
    p.press("n")
    p.keyUp("shiftleft")


def anterior():
    p.keyDown("shiftleft")
    p.press("p")
    p.keyUp("shiftleft")


def nueva_pestana():
    p.keyDown("ctrl")
    p.press("t")
    p.keyUp("ctrl")


def like_list():
    open_new_tab(LIKES)


def novvae_list():
    open_new_tab(ACTUAL_NOVVAE)


def github():
    open_new_tab(NOVVAE_REPO)


def search(texto):
    p.click()
    p.write(texto, 0.2)
    p.press("enter")


def search_yt(texto: str):
    query = "https://www.youtube.com/results?search_query="
    texto_plus = texto.replace(" ", "+")
    open_new_tab(query + texto_plus)


# --------------------------persistence---------------------------


def persistencia(texto):
    with open(PERSISTENCE_DIR, mode="+w") as persistence:
        persistence.write(texto)


def copiar_link():
    link()
    p.keyDown("ctrl")
    p.press("c")
    p.keyUp("ctrl")


def guardar() -> str:
    copiar_link()
    url = paste()
    persistencia(url)
    return url


# --------------------------main-------------------------------


def iniciar():
    # X
    browser()
    sleep(10)

    # xV
    saved_song = get_saved_song()
    print(saved_song)
    open_new_tab(saved_song)
    sleep(7)

    # Xv
    pag_1()
    sleep(2)

    # xvX
    nueva_pestana()
    pag_2()
    sleep(0.5)
    pag_3()
    sleep(2)

    # Vx
    pag_2()
    cerrar_pag_1()
    sleep(6)

    # vX
    pag_2()
    sleep(3)
    pag_1()
    sleep(0.5)
    pag_2()
    sleep(3)

    # Vx -> vX -> VSC
    pag_1()
    sleep(1)
    pag_2_fast()
    visual()
    terminal()


def get_saved_song():
    saved_song = ""
    with open(PERSISTENCE_DIR) as persistence:
        for line in persistence:
            saved_song = line
    return saved_song


if __name__ == "__main__":

    # CLICK POSITION TESTING
    if CHECK_POS:
        pos()
        exit()

    iniciar()

    auto_save_count = 0

    while True:
        print("-> ", end="")
        o = input()

        if o == "n" or o == "":
            browser()
            pag_1()
            pasar()
            pag_2_fast()
            visual()
            terminal()
            auto_save_count += 1
            if auto_save_count != 5:
                continue

        if o == "b":
            browser()
            pag_1()
            anterior()
            pag_2()
            visual()
            terminal()
            continue

        if o == "l":
            browser()
            pag_1()
            like()
            sleep(2.5)
            pasar()
            pag_2()
            visual()
            terminal()
            auto_save_count += 1
            if auto_save_count != 5:
                continue

        if o == "p":
            browser()
            pag_1()
            p.press("space")
            pag_2_fast()
            visual()
            terminal()
            continue

        if o == "v":
            browser()
            pag_1()
            continue

        if o == "k":
            like_list()
            continue

        if o == "kk" or o == "novvae" or o == "no":
            novvae_list()
            continue

        if o == "git" or o == "github" or o == "repo":
            github()
            continue

        if o == "-":
            print(get_saved_song())
            continue

        # here's the autosave
        if o == "g" or o == "s" or auto_save_count == 5:
            browser()
            pag_1()
            url = guardar()
            refresh_link()
            print(url)
            pag_2_fast()
            visual()
            terminal()
            auto_save_count = 0
            continue

        if o == "m" or o == "5":
            browser()
            pag_1()
            p.press("5")
            pag_2()
            visual()
            terminal()
            continue

        if o == "i" or o == "." or o == "00":
            browser()
            pag_1()
            p.press("0")
            pag_2()
            visual()
            terminal()
            continue

        if o == "q" or o == "," or o == "2":
            browser()
            pag_1()
            p.press("2")
            pag_2()
            visual()
            terminal()
            continue

        if o == "0v" or o == "0'":
            browser()
            pag_1()
            guardar()
            cerrar_pag_1()
            visual()
            cerrar()

        if o == "0c" or o == "09":
            browser()
            pag_1()
            url = guardar()
            print(url)
            cerrar()
            continue

        if o[0:6] == "search":
            texto = o[6:]
            browser()
            nueva_pestana()
            search_bar()
            search(texto)
            continue

        if o[0:2] == "yt":
            search_yt(o[2:])
            continue

        if o[0:7] == "youtube":
            search_yt(o[7:])
            continue

        if o == "0" or o == "exit":
            break

        print(
            "====== MAIN ======",
            "l : like",
            "n : next video",
            "b : past video",
            "p : pause",
            "v : see video",
            "====== VIDEO ======",
            "-  : current video index",
            "00 : initialice video",
            "5  : half of the video",
            "2  : quarter of the video",
            "======= APP =======",
            "g  : save actual video",
            "0  : exit app",
            "09 : close browser tab",
            "0' : close VSC tab",
            "====== LISTS ======",
            "kk : video list",
            "k  : likes list",
            "====== EXTRA ======",
            "git            : see project repo",
            "search <query> : search on browser",
            "yt <query>     : search on youtube",
            sep="\n",
        )

    browser()
    sleep(0.5)
    pag_1()
    guardar()
    cerrar()
    cerrar()
