from deep_translator import GoogleTranslator

text = input("Enter English text: ")
translated = GoogleTranslator(source='auto', target='hi').translate(text)

print("Translated text in Hindi:", translated)
