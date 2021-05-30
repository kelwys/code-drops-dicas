# dependency >>> pip install translate
from translate import Translator

# Set the translation language
translator = Translator(from_lang='english', to_lang='pt-br')

text = 'never stop learning'
result = translator.translate(text)

print(result)
# output: nunca pare de aprender