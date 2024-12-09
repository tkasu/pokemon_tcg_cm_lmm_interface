from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from ptcgcm_lmm.prompts import SYSTEM_PROMPT

load_dotenv()


def main():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    messages = [
        ("system", SYSTEM_PROMPT),
        (
            "user",
            "Decsribe Sword and Shield 151 series Blastoise-Ex card for me:",
        ),
    ]

    ai_message = llm.invoke(messages)

    print(ai_message)


if __name__ == "__main__":
    main()
