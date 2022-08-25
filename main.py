#importar bibliotecas de pip y python.
import pyautogui as pg, webbrowser as web , time as tn

#vincular con whatssap web y dandole limitacion de tiempo.
web.open("https://web.whatsapp.com/send?phone=numerotelefono")
tn.sleep(8)

for i in range(10):#Ciclo for para enviar mensajes.
    pg.write("Bombardeo de whatssap")
    pg.press('enter')
    print("Bombardeo"+str(i+1))
    pass

#cierre de ciclo for.


