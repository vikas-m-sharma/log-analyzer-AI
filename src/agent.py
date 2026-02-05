from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama


def load_llm():
    return Ollama(
        model="mistral",
        temperature=0.2
    )


def generate_answer(error_text: str) -> str:
    prompt = PromptTemplate(
        input_variables=["error_text"],
        template="""
You are an expert Python developer and AI engineer.

Analyze the following log errors and explain:
1. What the error means
2. Why it happened
3. How to fix it

Errors:
{error_text}
"""
    )

    llm = load_llm()
    chain = prompt | llm
    response = chain.invoke({"error_text": error_text})

    return response.strip()
