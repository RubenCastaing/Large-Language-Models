import nltk
from base_text import sentance_list, sentance_list_gpt40_es, sentence_list_gt_es

weights_list = [(1,), (1/2, 1/2), (1/3, 1/3, 1/3), (0.25, 0.25, 0.25, 0.25)]

# Iterate over the weights list
for weight_number, weights in enumerate(weights_list, start=1):
    print(f"\nFor N = {weight_number}")
    for sentence_number in range(len(sentance_list)):
        BLEUscore = nltk.translate.bleu_score.sentence_bleu(
            [sentance_list_gpt40_es[sentence_number]], 
            sentence_list_gt_es[sentence_number], 
            weights=weights
        )
        print(f"Sentence {sentence_number + 1}: BLEU score = {BLEUscore:.4f}")
