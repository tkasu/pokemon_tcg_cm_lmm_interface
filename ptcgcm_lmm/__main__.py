from dotenv import load_dotenv
from openai import OpenAI

from ptcgcm_lmm.prompts import SYSTEM_PROMPT

load_dotenv()


def main():
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": "Decsribe Sword and Shield 151 series Blastoise-Ex card for me:",
            },
        ],
    )

    #print(completion)
    print(completion.choices[0].message)


if __name__ == "__main__":
    main()
