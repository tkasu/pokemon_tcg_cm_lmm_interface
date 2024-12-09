from dotenv import load_dotenv
from pprint import pprint

from langchain_openai import ChatOpenAI
from ptcgcm_lmm.models import Card
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
    structured_card_llm = llm.with_structured_output(Card)

    messages = [
        ("system", SYSTEM_PROMPT),
        (
            "user",
            "Decsribe Sword and Shield 151 series Blastoise-Ex card for me:",
        ),
    ]

    ai_message: Card = structured_card_llm.invoke(messages)
    pprint(ai_message.model_dump())


if __name__ == "__main__":
    main()
