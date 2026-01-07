from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "ai-backend-rag",
    },
)

SYSTEM_PROMPT = """
You are a helpful assistant.
Answer the question ONLY using the provided context.
If the answer cannot be found in the context, say "I don't know".
"""


async def generate_answer(question: str, context_chunks: list[str]) -> str:
    context_text = "\n\n".join(context_chunks)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"""
CONTEXT:
{context_text}

QUESTION:
{question}
""",
        },
    ]

    response = await client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=messages,
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
