import nltk
from Translate_to_spainish import sentance_list, sentance_list_gpt40_es, sentence_list_gt_es

weights_list = [(1,),(1/2, 1/2),(1/3, 1/3, 1/3),(0.25, 0.25, 0.25, 0.25)]

for weight_number in range(len(weights_list)):
    print("The N gram is ", weight_number + 1)
    for sentance_number in range (0,4):
        BLEUscore = nltk.translate.bleu_score.sentence_bleu([sentance_list_gpt40_es[sentance_number]], sentence_list_gt_es[sentance_number], weights=weights_list[weight_number])
        print(BLEUscore)