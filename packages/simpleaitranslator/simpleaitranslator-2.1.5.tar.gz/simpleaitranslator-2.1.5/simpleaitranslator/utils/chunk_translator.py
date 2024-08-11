from pydantic import BaseModel

from simpleaitranslator.exceptions import MissingAPIKeyError
from simpleaitranslator.utils.enums import ChatGPTModelForTranslator

from openai import AsyncAzureOpenAI
from openai import AsyncOpenAI
class TranslateFormat(BaseModel):
    translated_text: str


async def translate_chunk_of_text(text_chunk: str, to_language: str, chatgpt_model_name: ChatGPTModelForTranslator,
                                  client: AsyncOpenAI | AsyncAzureOpenAI) -> str:
    if not client:
        raise MissingAPIKeyError()

    messages = [
        {"role": "system",
         "content": f"You are a language translator. You should translate text provided by user to the {to_language} language. Don't write additional message like This is translated text just translate text."},
        {"role": "user", "content": text_chunk}
    ]

    response = await client.beta.chat.completions.parse(
        model=chatgpt_model_name.value,
        messages=messages,
        response_format=TranslateFormat  # auto is default, but we'll be explicit
    )

    response_message = response.choices[0].message.parsed.translated_text
    return response_message

