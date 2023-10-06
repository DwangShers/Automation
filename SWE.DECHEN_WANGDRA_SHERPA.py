import time
import pygame

# path to the music file
music_file = '/home/wangdra/Desktop/Mediatation Music/mediatation.mp3'

def play_music():
    pygame.mixer.init() #Initialize the Pygame mixer
    pygame.mixer.music.load(music_file) #Load the MP3 file
    pygame.mixer.music.play() #Play the music
    time.sleep(600) #Pause execution(program) for a specified duration
    pygame.mixer.music.stop() #Stop the music

# Defining sleep and wake times
sleep_time = time.strptime("10:00:00 PM", "%I:%M:%S %p")
wake_time = time.strptime("07:00:00 AM", "%I:%M:%S %p")

# Formating the sleeping and waking time to show only hours, minute, second, and AM or PM
formatted_time1 = time.strftime("%I:%M:%S %p", sleep_time)
formatted_time2 = time.strftime("%I:%M:%S %p", wake_time)

while True:
    # get current time and formating it simultanously
    localtime = time.localtime()
    result_time = time.strftime("%I:%M:%S %p",localtime)
    # to check if the localtime matches the formatted time
    if result_time == formatted_time2 or result_time == formatted_time1:
        play_music()
        time.sleep(60)