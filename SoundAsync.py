import pydub as pd
import multiprocessing as mp
from time import sleep
import simpleaudio as siau
from pydub.playback import play
from datetime import datetime
import asyncio
import gpiozero 

class SoundAsync:
    button = Button(17)
    loop =asyncio.get_event_loop()
    playback = 
    
    async def timerFunc():
        await asyncio.wait(sleep(5))
        print("done")
    async def interrupt():
        
     
    async def audioPlayback():
        button.when_pressed=loop.call_soon_threadsafe(interrupt)
        mp3=pd.AudioSegment.from_file("test.mp3",format="mp3")-20
        playback=siau.play_buffer(mp3.raw_data,num_channels=mp3.channels,bytes_per_sample=mp3.sample_width,sample_rate=mp3.frame_rate)
        print("playback Started")
        tim=asyncio.create_task(timerFunc())
        inter=asyncio.create_task(interrupt())
        start = datetime.now()
        await asyncio.wait([tim,inter],return_when=asyncio.FIRST_COMPLETED)
        print("await ended")
        
        elapsed = (datetime.now()-start).total_seconds()
        mp32=mp3[elapsed*1000:]+mp3[0:elapsed*1000]
        mp32=mp32.reverse()
        playback.stop()
        playback=siau.play_buffer(mp32.raw_data,num_channels=mp3.channels,bytes_per_sample=mp3.sample_width,sample_rate=mp3.frame_rate)
        tim.cancel()
        tim2=asyncio.create_task(timerFunc())
        inter.cancel()
        inter2=asyncio.create_task(interrupt())
        await asyncio.wait([tim2,inter2],return_when=asyncio.FIRST_COMPLETED)
        print("await ended")
        playback.stop()
        mp32.export("mp32.mp3",format="mp3")



asyncio.run(audioPlayback())
print("done")
