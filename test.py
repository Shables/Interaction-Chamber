import simpleaudio
import time

sim_complete_sound = simpleaudio.WaveObject.from_wave_file('audio/trill_complete.wav')
person_leaving_sound = simpleaudio.WaveObject.from_wave_file('audio/grumble.wav')

def play_sound(sound):
    play_obj = sound.play()
    play_obj.wait_done()

play_sound(person_leaving_sound)
print("FIRST AUDIO PLAYED")
time.sleep(2)
play_sound(sim_complete_sound)