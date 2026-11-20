
from google import genai

client = genai.Client()

system_prompt = """
You are a helpful AI tutor.
Explain technical concepts in simple language.
Give practical examples.
"""

user_prompt =  "how to reduce dark circles under eyes? Explain with an example."

prompt = f"""
{system_prompt}

User request:
{user_prompt}
"""

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

print("AI Response:")
print(response.text)
