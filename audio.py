from ibm_watson import SpeechToTextV1
from ibm_watson import LanguageTranslatorV3
url_s2t = "F9hBd11j9O6ARqToQ8RL9xOns-XqK24OfB7TRQdPljqk"
key = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/e7844af6-2d51-42a7-8712-685f94799a20"
s2t = SpeechToTextV1(authenticator=key)
filename = 'hello_this_is_python.wav'
with open(filename, mode='rb') as wav:
    response = s2t.recognize(audio=wav, content_type='audio/wav') #send the audio to watsonSpeech

text = response.result['transcript']
url_lt = "https://geteway.watsonplatform.net/language-translator/api"
version_lt = '2020-06-20'
language_tr = LanguageTranslatorV3(iam_apikey=key, url=url_lt, version=version_lt)
traslate_response = language_tr.translate(text=text, model_id='en-es')
reslt = traslate_response.get_result()
print(reslt['translation'])