import json
import pydirectinput
import keyboard
import random
import time

with open("dpconf.json") as myfile:  # файлик со всеми нужными данными
    d = json.load(myfile)
    print(d)


def starrt(key):
    if key == 1:
        pydirectinput.keyDown("d")
    elif key == 0:
        pydirectinput.keyDown("a")
    pydirectinput.keyDown("w")
    time.sleep(float(d["drift_start"]))  # время, которое держит w и d для того, чтобы войти в дрифт
    pydirectinput.keyUp("w")
    print("lesgo")
key = 1
while True:  # бесконечный цикл, останавливается условием
    if keyboard.is_pressed("ins"):# условие запуска фарма
        print("yap")
        print("HI")
        startTime = time.time()
        fail = random.randint(0, 10)
        c = 0
        # начало входа в дрифт
        starrt(key)
        # вошли в дрифт
        while True:  # основной цикл, тут происходит регулировка во время дрифта и зачисление очков
            Time = time.time() - startTime  # берём время на данный момент, чтобы знать, сколько прошло с начала фарма
            if c > 10 and 0 <= fail <= 1 or round(Time // 60) == 2:
                print("qqq")
                '''if 0 <= fail <= 3:
                    rand = random.randint(0, 9)
                    pyautogui.keyDown("d")
                    time.sleep(random.uniform(0.3, 0.45))
                    pyautogui.keyUp("d")''' #рандомизация, я её когда-нибудь доделаю)))
                if round(Time // 60, 1) == 2:
                    pydirectinput.keyDown("space")
                    time.sleep(5)  # если без перекладки
                    pydirectinput.keyUp("space")
                    #pydirectinput.keyUp("space")
                    startTime = time.time()
                    fail = random.randint(0, 10)
                    if key == 1:
                        key = 0
                    elif key == 0:
                        key = 1 # если с перекладкой, то с 95 по 99 выполнять. Если без перекладки, то нет
                    print(key)
                    starrt(key)
            print("qqall")
            if key == 1:
                pydirectinput.keyUp("d")
            elif key == 0:
                pydirectinput.keyUp("a")
            pydirectinput.keyDown("w")
            time.sleep(float(d["drift_process"]))  # держит газ, когда уже в дрифте(чтобы держать угол)
            pydirectinput.keyUp("w")
            c += 1
            if keyboard.is_pressed("del"):  # условие остановки фарма
                break
            if keyboard.is_pressed("end"):  # условие закрытия программы
                exit()
    if keyboard.is_pressed("end"):  # условие закрытия программы
        exit()

    '''def exitt(self):
        eexit = want_exit()
        eexit.setWindowFlag(Qt.WindowStaysOnTopHint)
        eexit.setWindowModality(Qt.ApplicationModal)
        eexit.exec_()'''


#менять можно
#12 13 16 34 35 38 43 строки
#удачного использования)
#если есть вопросы, а они могут появиться из-за beta версии, то пишите в вк) https://vk.com/v_khakas_v
#всем удачи! я надеюсь, что вы сможете довести это до ума и убьёте экономику дп)
#если будут успехи, сообщите мне в вк, пожалуйста