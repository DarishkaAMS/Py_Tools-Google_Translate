from googletrans import Translator

translator = Translator()

text = "Слава Україні"

traslation = translator.translate(text, scr="ua", dest="en")

print(traslation.text)
