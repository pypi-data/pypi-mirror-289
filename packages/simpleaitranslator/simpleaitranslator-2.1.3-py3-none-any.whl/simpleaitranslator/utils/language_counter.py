from pydantic import BaseModel

from simpleaitranslator.utils.enums import ChatGPTModelForTranslator
from openai import AsyncAzureOpenAI
from openai import AsyncOpenAI


class HowManyLanguages(BaseModel):
    number_of_languages: int


async def how_many_languages_are_in_text(text: str, chatgpt_model_name: ChatGPTModelForTranslator,
                                         client: AsyncAzureOpenAI | AsyncOpenAI) -> int:
    completion = await client.beta.chat.completions.parse(
        model=chatgpt_model_name.value,
        messages=[
            {"role": "system", "content": "You are text languages counter you should count how many languaes are in provided by user text"},
            {"role": "user", "content": f"Please count how many languaes are in this text:\n{text}"},
        ],
        response_format=HowManyLanguages,
    )
    event = completion.choices[0].message.parsed.number_of_languages
    return event
