from rouge_score import rouge_scorer
from base_text import gpt4o_summary, llama3_405B_summary, gemini_flash_summary

#I will use gpt4o as the base text
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rouge3', 'rouge4'], use_stemmer=True)
gpt4o_llama3_scores = scorer.score(gpt4o_summary, llama3_405B_summary)
gpt4o_gemini_scores = scorer.score(gpt4o_summary, gemini_flash_summary)

#calculate the geometric mean


print(gpt4o_llama3_scores)