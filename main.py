#import google.cloud.speech as speech
#import pytdm as TTS
import LoadHome as LH
import pyttsx3 as TTS

#STT = speech.SpeechClient()

#audio = speech.RecognitionAudio(uri=gcs_uri)
import speech_recognition as STT




"""
config = speech.RecognitionConfig( 
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="pl-PL",
)
"""

# Detects speech in the audio file
#response = client.recognize(config=config, audio=audio)

#for result in response.results:
#    print("Transcript: {}".format(result.alternatives[0].transcript))
shouldclose = False

def getaudioText():
    r = STT.Recognizer()
    audio =None
    said =""

    with STT.Microphone() as source:
        print("shhh, adjusting noise")
        r.adjust_for_ambient_noise(source,duration=1)
        print("prosze mowic:")

        audio = r.listen(source,timeout=1,phrase_time_limit=6)
        said = ""
    print("finished listening, on my way to calculate what you said ..")

    try:
        said = r.recognize_google(audio,language="pl_PL")
        print(said)
        TTS.speak(said)
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " +said)
    except STT.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except STT.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    """
    except STT.UnknownValueError:
        print("Sphinx could not understand audio")
        TTS.mów("Sphinx could not understand audio","en")
    except STT.RequestError as e:
        print("Sphinx error; {0}".format(e))
        TTS.mów("Sphinx error; {0}".format(e),"en")
        """

    return said
while not shouldclose:

    while True:
        print('''Napisz pytanie i naciśnij Enter
            albo naciśnij Enter i zadaj pytanie.''')
        tekst = input(">>")
        if len(tekst) > 0:
            odp = LH.asystent(tekst)
        else:
            command = getaudioText()
            if len(command) >0:
                if LH.asystent(command) == False:
                    TTS.speak("Cos nie dziala, powtorz procedure...")




