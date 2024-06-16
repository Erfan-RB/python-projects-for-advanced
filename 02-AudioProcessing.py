#Audio-Processing
import urllib.request
from pydub import AudioSegment
from pydub.playback import play

#Download audio
urllib.request.urlretrieve("")
#load
loop = AudioSegment.from_wav(".wav")
#play
play(loop)

#repeat
loop2 = loop * 2
#length
length = len(loop2)
#time
fade_time = int(length * 0.5)
faded = loop2.fade_in(fade_time).fade_out(fade_time)

# Download another 
urllib.request.urlretrieve(".wav")
# Load into PyDub
beat = AudioSegment.from_wav(".wav")
# Mix with our original loop
mixed = beat[:length].overlay(loop2)

#filter
filtered = best.low_pass_filter(3000)
loop = loop2.reverse().pan(-0.5).overlay(loop2.pan(0.5))
final = filtered.overlay(loop2 - 3, loop=True)
final.export("final.mp3", format="mp3")

# Create an empty AudioSegment
result = AudioSegment.silent(duration=0)
# Loop over 0-14
for n in range(15):
    gen = Sine(200 * n)
    sine  = gen.to_audio_segment(duration=200).apply_gain(-3)
    sine = sine.fade_in(50).fade_out(100)
    result += sine
# Play the result
play(result)
