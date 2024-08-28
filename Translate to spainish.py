from deep_translator import GoogleTranslator

#creating a list of the sentances
sentance1 = 'A transformer architecture is a deep learning model architecture that uses self-attention mechanisms to process input data'
sentance2 = 'Tokenisation is the process of converting text into smaller units that can be processed by a large language model'
sentance3 = 'Both cats and dogs make wonderful and loyal companions for life'
sentance4 = 'Cats love to nap around the house and dogs like chasing sticks'
sentance_list = [sentance1, sentance2, sentance3, sentance4]

ChatGPT_api_key = 'sk-tlzOSseI_WfbZGKGYRzUYiexHgdWjw1XMB7SGpBfNPT3BlbkFJO58Lerb-U0_n57fGUtNf4cqex47k4yFjdBNEqmKycA'

#converting the sentances to spainish using google translate
language_dictionary = {}
for x in range(1, 5):
    language_dictionary["sentance{0}".format(x)] = GoogleTranslator(source='auto', target='es').translate(sentance_list[x-1])
print(language_dictionary)

#converting the sentances to spainish using the Gpt4 API
text = 'happy coding'
translated = ChatGptTranslator(api_key='your_key', target='german').translate(text=text)

#Comparing the answers using Bleu
#Comparing the answers using ROGUE-N
