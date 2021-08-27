import time
from pygame import mixer
def musiconloop(file,string):

    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==string:
            mixer.music.stop()
            break
def masglog(msg):
    with open("Healthy programmer.txt",'a') as a:
        a.write(str(time.asctime())+f'{msg}')
if __name__ == '__main__':
     print("Healthy Programmer program started:...........")
     # musiconloop('F:\youtube audio\Airline.mp3','stop')
     initwater=time.time()
     initphycial=time.time()
     watertime=10
     phycialtime=30

     while True:
         if time.time()-initwater > watertime:
             print("Water Drinking time, Enter stop if you complete the task")
             musiconloop('F:\youtube audio\Airline.mp3','stop')
             initwater=time.time()
             masglog("In this time I drank water\n")


         if time.time()-initphycial >phycialtime:
             print("Physical Exercise time, Enter stop if you complete the task")
             musiconloop('F:\youtube audio\I_m_Happy_For_This_Guitar.mp3','stop')
             initphycial=time.time()
             masglog("In this time I Do phycial Exercise\n")


