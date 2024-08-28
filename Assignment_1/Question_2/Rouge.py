from rouge_score import rouge_scorer
from base_text import gpt4o_summary, llama3_405B_summary, gemini_flash_summary
import pandas as pd
from scipy.stats import gmean

# Initialize the Rouge scorer
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rouge3', 'rouge4'], use_stemmer=True)

# Compute scores for gpt4o_summary against llama3_405B_summary and gemini_flash_summary
gpt4o_llama3_scores = scorer.score(gpt4o_summary, llama3_405B_summary)
gpt4o_gemini_scores = scorer.score(gpt4o_summary, gemini_flash_summary)

# Converting Rouge scores dictionary to a DataFrame
def scores_to_dataframe(scores_dict):
    return pd.DataFrame({
        key: {
            'precision': score.precision,
            'recall': score.recall,
            'fmeasure': score.fmeasure
        }
        for key, score in scores_dict.items()
    }).T

# Convert the scores to DataFrames
df_llama3 = scores_to_dataframe(gpt4o_llama3_scores)
df_gemini = scores_to_dataframe(gpt4o_gemini_scores)

# Calculate geometric mean for each metric
geometric_mean_llama3 = df_llama3.apply(gmean)
geometric_mean_gemini = df_gemini.apply(gmean)

# Print the results
print("Geometric Mean for GPT-4o vs LLaMA 3:")
print(geometric_mean_llama3)
print("\nGeometric Mean for GPT-4o vs Gemini Flash:")
print(geometric_mean_gemini)


# Print Rouge-1 to Rouge-4 scores for GPT-4o vs LLaMA 3
print("GPT-4o vs LLaMA 3 Scores:")
print(df_llama3)

# Print Rouge-1 to Rouge-4 scores for GPT-4o vs Gemini Flash
print("\nGPT-4o vs Gemini Flash Scores:")
print(df_gemini)