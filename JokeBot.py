import pyjokes
import pyttsx3

engine = pyttsx3.init()
joke = pyjokes.get_joke()
engine.say(joke)
engine.runAndWait()

