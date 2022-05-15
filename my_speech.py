import time

import pyttsx3

engine = pyttsx3.init()
engine.say("Say something.")
engine.say("中文")
engine.say(time.strftime('%H点%M分%S秒'))
engine.runAndWait()
