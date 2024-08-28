from deep_translator import GoogleTranslator
from deep_translator import ChatGptTranslator

#The assignement's list of the sentances
sentance1 = 'A transformer architecture is a deep learning model architecture that uses self-attention mechanisms to process input data'
sentance2 = 'Tokenisation is the process of converting text into smaller units that can be processed by a large language model'
sentance3 = 'Both cats and dogs make wonderful and loyal companions for life'
sentance4 = 'Cats love to nap around the house and dogs like chasing sticks'
sentance_list = [sentance1, sentance2, sentance3, sentance4]

#These sentances have been translated to spainish in GPT4o.
sentance1_gpt40_es = "Una arquitectura de transformador es una arquitectura de modelo de aprendizaje profundo que utiliza mecanismos de autoatención para procesar datos de entrada."
sentance2_gpt40_es = "La tokenización es el proceso de convertir texto en unidades más pequeñas que pueden ser procesadas por un modelo de lenguaje grande."
sentance3_gpt40_es = "Tanto los gatos como los perros son compañeros maravillosos y leales de por vida."
sentance4_gpt40_es = "A los gatos les encanta dormir la siesta en la casa y a los perros les gusta perseguir palos."
sentance_list_gpt40_es = [sentance1_gpt40_es, sentance2_gpt40_es, sentance3_gpt40_es, sentance4_gpt40_es]

#converting the sentances to spainish using google translate
sentence_list_gt_es = []
for sentance in sentance_list:
    sentence_list_gt_es.append(GoogleTranslator(source='auto', target='es').translate(sentance))