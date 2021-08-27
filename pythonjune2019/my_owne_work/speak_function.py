# import win32com.client
# # import requests
# def speak(str):
#     speak=win32com.client.Dispatch("SAPI.spvoice")
#     speak.speak(str)
#
#
# # r=requests.get('https://python.swaroopch.com/about_python.html')
# # print(r.text)
# if __name__ == '__main__':
#     with open('file_to_speak','r') as f:
#         a=f.read()
#
#
#     speak(a)
#
# import requests
# import win32com.client
#
# string=requests.get('https://www.djangoproject.com/start/overview/').text
# speak=win32com.client.Dispatch("SAPI.spvoice")
# speak.speak(string)


import re
str='pradippandit026@gmail.com.in is the email of pradip.'
# email=re.findall(r'[a-z0-9A-Z]+@[a-z0-9A-Z]+[.][a-z0-9A-Z]+',str)
email=re.findall(r'\w+@\S+\w',str)
print(email)







