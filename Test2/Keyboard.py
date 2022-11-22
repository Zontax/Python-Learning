import keyboard as kb
import os

kb.add_abbreviation('gg', 'God game!')  
# kb.add_hotkey('ctrl+ h', lambda: kb.write('God game man!', delay=0)) #скорочення тексту + space
# kb.wait('shift')

# povtor = kb.record('alt') #запис
# kb.play(povtor) # повтор

# kb.press('ctrl') #зажим
# kb.release('ctrl') #віджим
key1 = 'ctrl + h'
file1 = r'C:\Windows\System32\cmd.exe'
kb.add_hotkey(key1, lambda: os.system('start ' + file1))
print(key1 + " cmd")
kb.wait()
