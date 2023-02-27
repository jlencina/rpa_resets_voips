import easygui
import os

msg = "Load application..."
title="Juan's Hardware Application Starter"
choices = ["Antares","Abrir Chrome"]
reply = easygui.buttonbox(msg, title , choices=choices)
if reply == "Antares":
    os.startfile("C:\\Users\\Usuario\\Documents\\test_py\\antares.py")
elif reply == "Abrir Chrome":
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")