from dotenv import load_dotenv
from pprint import pprint

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from ptcgcm_lmm.models import Card
from ptcgcm_lmm.prompts import SYSTEM_PROMPT

load_dotenv()

# From https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/series/sv3pt5/9/
IMAGE_URL = "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV3PT5/SV3PT5_EN_9.png"


def main():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    structured_card_llm = llm.with_structured_output(Card)

    message = HumanMessage(
        content=[
            {"type": "text", "text": SYSTEM_PROMPT},
            {
                "type": "image_url",
                "image_url": {
                    "url": IMAGE_URL,
                },
            },
        ]
    )

    ai_message: Card = structured_card_llm.invoke([message])
    pprint(ai_message.model_dump())


if __name__ == "__main__":
    main()
