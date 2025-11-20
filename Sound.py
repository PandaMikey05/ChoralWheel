import pydub as pd
import multiprocessing as mp
from time import sleep
import simpleaudio as siau
from pydub.playback import play
from datetime import datetime
mp3=pd.AudioSegment.from_file("test.mp3",format="mp3")-10
playback=siau.play_buffer(mp3.raw_data,num_channels=mp3.channels,bytes_per_sample=mp3.sample_width,sample_rate=mp3.frame_rate)
print("playback Started")
start = datetime.now()
sleep(5)
elapsed = (datetime.now()-start).total_seconds()
mp32=mp3[elapsed*1000:]+mp3[0:elapsed*1000]
mp32=mp32.reverse()
playback.stop()
playback=siau.play_buffer(mp32.raw_data,num_channels=mp3.channels,bytes_per_sample=mp3.sample_width,sample_rate=mp3.frame_rate)
sleep(5)
playback.stop()
mp32.export("mp32.mp3",format="mp3")
