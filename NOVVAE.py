import pyautogui as p
from pyperclip import paste
from time import sleep
from webbrowser import open_new_tab
'''                                                            

`7MN.   `7MF'                                                  
  MMN.    M                                                    
  M YMb   M   ,pW"Wq.  `7M'   `MF'`7M'   `MF' ,6"Yb.   .gP"Ya  
  M  `MN. M  6W'   `Wb   VA   ,V    VA   ,V  8)   MM  ,M'   Yb 
  M   `MM.M  8M     M8    VA ,V      VA ,V    ,pm9MM  8M"""""" 
  M     YMM  YA.   ,A9     VVV        VVV    8M   MM  YM.    , 
.JML.    YM   `Ybmd9'       W          W     `Moo9^Yo. `Mbmmd' 

                                               
                _                ___       _.--.
                \`.|\..----...-'`   `-._.-'_.-'`             
                /  ' `         ,       _.-'          
                )/' _/     \   `-_,   /             
                `-'" `"\_  ,_.-;_.-\_ ',          
                    _.-'_./   {_.'   ; /           
                   {_.-``-'         {_/ v1.4    


'''

NOVVAE_2 = 'https://www.youtube.com/playlist?list=PLV2hNo2SKdY3FA-HMN1xFlYEpp8P5BL9O'
LIKES    = 'https://www.youtube.com/playlist?list=LL'
PERSISTENCE_DIR = "c:/Users/Esteban/Downloads/EAFIT/-CODE-/NOVVAE_PERSISTENCE.txt"

#---------------clicklist--------------------

def pos():          p.displayMousePosition()

def cerrar():       p.moveTo(1344, 15, 0.2) ; p.click()

def minimizar():    p.moveTo(1251, 13, 0.2) ; p.click()

def visual():       p.moveTo(390, 740, 0.2) ; p.click()

def chrome():       p.moveTo(330, 740, 0.2) ; p.click()

def pag_1():        p.moveTo(165, 10, 0.2)  ; p.click()

def pag_2():        p.moveTo(360, 10, 0.2)  ; p.click()

def pag_3():        p.moveTo(560, 10, 0.2)  ; p.click()

def terminal():     p.moveTo(660, 700, 0.2) ; p.click()

def refresh_link(): p.moveTo(10, 700, 0.2) ; p.click()

def like():         p.moveTo(610, 690, 0.2) ; p.click()   

def link():         p.moveTo(660, 50, 0.2)  ; p.click()

def cerrar_tab():   p.moveTo(255, 15, 0.2)  ; p.click()

#-------------------options--------------------

def pasar():
    p.keyDown('shiftleft')
    sleep(0.5)
    p.press('n')
    sleep(0.5)
    p.keyUp('shiftleft')

def anterior():
    p.keyDown('shiftleft')
    sleep(0.5)
    p.press('p')
    sleep(0.5)
    p.keyUp('shiftleft')

def nueva_pestana():
    p.keyDown('ctrl')
    p.press('t')
    p.keyUp('ctrl')

def like_list():
    open_new_tab(LIKES)

#--------------------------persistence---------------------------

def persistencia(texto):
    with open(PERSISTENCE_DIR, mode="+w") as persistence:
        persistence.write(texto)

def copiar_link():
    link()
    p.keyDown('ctrl')
    p.press('c')
    p.keyUp('ctrl')

def guardar():
    copiar_link()
    url = paste()
    persistencia( url )

#--------------------------main-------------------------------

def iniciar(novvae = False):
    sleep(5)
    if novvae: open_new_tab(NOVVAE_2)

    last_song = ''
    with open(PERSISTENCE_DIR) as persistence:
        for line in persistence: last_song = line
    print(last_song)
    open_new_tab(last_song)
    sleep(5)
    nueva_pestana()

#pos()

if __name__ == "__main__":
    chrome()
    iniciar()
    cerrar_tab()
    visual()
    terminal()

    while True:
        print('-> ',end='')
        o = input()

        if o == 'n':
            chrome()
            pag_1()
            pasar()
            pag_2()
            visual()
            terminal()
            continue

        if o == 'b':
            chrome()
            pag_1()
            anterior()
            pag_2()
            visual()
            terminal()
            continue

        if o == 'l':
            chrome()
            pag_1()
            like()
            sleep(2)
            pasar()
            pag_2()
            visual()
            terminal()
            continue

        if o == 'p':
            chrome()
            pag_1()
            p.press('space')
            pag_2()
            visual()
            terminal()
            continue

        if o == 'v':
            chrome()
            pag_1()
            continue

        if o == 'k':
            like_list()
            continue

        if o == '-':
            with open(PERSISTENCE_DIR) as persistence:
                for line in persistence: print(line)
            continue

        if o == 'g':
            chrome()
            pag_1()
            guardar()
            refresh_link()
            with open(PERSISTENCE_DIR) as persistence:
                for line in persistence: print(line)
            pag_2()
            visual()
            terminal()
            continue

        if o == '0':
            break

        print('l:like n:nope v:vide 0:quit\nb:back p:paus k:list -:numb')
    
    chrome()
    pag_1()
    guardar()
    cerrar()
    cerrar()


