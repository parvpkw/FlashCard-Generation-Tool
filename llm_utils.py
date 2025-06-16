import openai

openai.api_key = "your-api-key-here"

def generate_flashcards(text, subject):
    prompt = f"""
You are a helpful assistant. Given the educational content below, generate 10 flashcards with clear Q&A.

Subject: {subject}
Text: {text[:2000]}  # truncate if too long

Return format:
Q: ...
A: ...
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response['choices'][0]['message']['content']
    cards = []
    for qa in output.strip().split("Q:")[1:]:
        parts = qa.strip().split("A:")
        if len(parts) == 2:
            q = parts[0].strip()
            a = parts[1].strip()
            cards.append({"question": q, "answer": a})
    return cards
