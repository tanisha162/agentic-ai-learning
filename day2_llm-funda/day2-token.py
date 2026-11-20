
import tiktoken

text = "I am learning Agentic AI with Python."

encoding = tiktoken.get_encoding("cl100k_base")

tokens = encoding.encode(text)

print("Original text:", text)
print("Token IDs:", tokens)
print("Number of tokens:", len(tokens))

decoded_text = encoding.decode(tokens)

print("Decoded text:", decoded_text)
