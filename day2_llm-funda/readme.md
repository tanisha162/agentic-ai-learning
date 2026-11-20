# Day 2: Large Language Models (LLMs) Fundamentals

## Overview
Today, I learned the fundamentals of Large Language Models (LLMs) and how they generate human-like responses. I also explored tokenization, context windows, training, inference, and sampling parameters.

## Topics Covered

### 1. What is an LLM?
A Large Language Model is an AI model trained on large amounts of text data to understand and generate human language.

Examples:
- ChatGPT
- Gemini
- Claude
- Llama

### 2. Next-Token Prediction
LLMs generate responses by predicting the next token based on the previous context. They repeat this process until the response is complete.

### 3. Tokenization
Tokenization is the process of splitting text into smaller units called tokens. A token can be a word, part of a word, or punctuation.

**Practical implementation:** Used Python's `tiktoken` library to encode text into token IDs and decode it back.

### 4. Context Window
The context window is the maximum amount of tokens a model can process in a single request. It can include prompts, conversation history, tool results, and generated output.

### 5. Training vs Inference
- **Training:** The model learns patterns from data by updating its parameters.
- **Inference:** The trained model uses its learned parameters to generate responses.

### 6. Temperature and Top-P
- **Temperature:** Controls the randomness of generated responses.
- **Top-P:** Limits token selection to a group of likely candidates based on cumulative probability.

## Practical Exercise

Created `day2_tokens.py` using the `tiktoken` library to:
- Encode text into token IDs.
- Count the number of tokens.
- Decode token IDs back into text.

## Technologies Used
- Python
- tiktoken

## Key Takeaways
- LLMs generate responses through next-token prediction.
- Tokens are the basic units processed by language models.
- Context windows limit how much information a model can process at once.
- Training and inference are two different stages.
- Temperature and Top-P influence text generation.

## Next Steps
- Explore LLM APIs.
- Understand prompts and structured outputs.
- Learn how LLMs interact with external tools.
- Gradually upgrade the rule-based calculator into an LLM-powered agent.