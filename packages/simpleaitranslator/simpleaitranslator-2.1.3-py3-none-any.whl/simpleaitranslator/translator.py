import asyncio
from openai import AsyncAzureOpenAI
from openai import AsyncOpenAI
from simpleaitranslator.exceptions import MissingAPIKeyError, NoneAPIKeyProvidedError, InvalidModelName
from simpleaitranslator.utils.chunk_translator import translate_chunk_of_text
from simpleaitranslator.utils.enums import ChatGPTModelForTranslator
from pydantic import BaseModel

from simpleaitranslator.utils.language_counter import how_many_languages_are_in_text
from simpleaitranslator.utils.text_splitter import split_text_to_chunks, get_first_n_words
from typing import Optional
CHATGPT_MODEL_NAME = ChatGPTModelForTranslator.BEST_BIG_MODEL
global_client = None
MAX_LENGTH = 1000
MAX_LENGTH_MINI_TEXT_CHUNK = 128

def set_openai_api_key(api_key):
    """
    Sets the API key for the OpenAI client.

    Parameters:
    api_key (str): The API key for authenticating with the OpenAI API.

    Raises:
    NoneAPIKeyProvidedError: If the api_key is empty or None.
    """
    if not api_key:
        raise NoneAPIKeyProvidedError()
    global global_client
    global_client = AsyncOpenAI(api_key=api_key)

def set_azure_openai_api_key(azure_endpoint, api_key, api_version, azure_deployment):
    """
    Sets the API key and related parameters for the Azure OpenAI client.

    Parameters:
    azure_endpoint (str): The endpoint URL for the Azure OpenAI service.
    api_key (str): The API key for authenticating with the Azure OpenAI API.
    api_version (str): The version of the Azure OpenAI API to use.
    azure_deployment (str): The specific deployment of the Azure OpenAI service.

    Raises:
    NoneAPIKeyProvidedError: If the api_key is empty or None.
    ValueError: If azure_endpoint, api_version, or azure_deployment are empty or None.
    """
    if not api_key:
        raise NoneAPIKeyProvidedError()
    if not azure_deployment:
        raise ValueError('azure_deployment is required - current value is None')
    if not api_version:
        raise ValueError('api_version is required - current value is None')
    if not azure_endpoint:
        raise ValueError('azure_endpoint is required - current value is None')
    global global_client
    global_client = AsyncAzureOpenAI(
        azure_endpoint=azure_endpoint,
        api_key=api_key,
        api_version=api_version,
        azure_deployment=azure_deployment
    )


def set_chatgpt_model(chatgpt_model_name: ChatGPTModelForTranslator):
    """
    Sets the default ChatGPT model.

    This function allows you to change the default ChatGPT model used in the application.

    Line to import enums:
    from simpleaitranslator.utils.enums import ChatGPTModel

    Parameters:
    chatgpt_model_name (str or ChatGPTModel): The name of the ChatGPT model to set.
    Recommended enums are:
        - ChatGPTModelForTranslator.BEST_BIG_MODEL
        - ChatGPTModelForTranslator.BEST_SMALL_MODEL

    Raises:
    InvalidModelName: If the provided model name is not valid.
    ValueError: If the chatgpt_model_name is None or in an incorrect format.
    """
    global CHATGPT_MODEL_NAME

    if type(chatgpt_model_name) == ChatGPTModelForTranslator:
        CHATGPT_MODEL_NAME = chatgpt_model_name
    else:
        raise ValueError('chatgpt_model name is required - current value is None or have wrong format')



def _get_setup_for_one_request(chatgpt_model_name, open_ai_api_key_for_this_translation)->(ChatGPTModelForTranslator, AsyncAzureOpenAI | AsyncOpenAI):
    global global_client
    global CHATGPT_MODEL_NAME
    # Setup configuration for translation
    if not global_client and not open_ai_api_key_for_this_translation:
        raise MissingAPIKeyError()
    if chatgpt_model_name is None:
        chatgpt_model_name = CHATGPT_MODEL_NAME

    if open_ai_api_key_for_this_translation is None:
        client = AsyncOpenAI(api_key=open_ai_api_key_for_this_translation)
    else:
        client = global_client

    return chatgpt_model_name, client


class TextLanguageFormat(BaseModel):
    language_ISO_639_3_code: str


async def async_get_text_language(text, chatgpt_model_name: Optional[ChatGPTModelForTranslator] = None,
                                  open_ai_api_key_for_this_translation: Optional[str] = None) -> str:

    global MAX_LENGTH
    chatgpt_model_name, client = _get_setup_for_one_request(chatgpt_model_name, open_ai_api_key_for_this_translation)

    text = get_first_n_words(text, MAX_LENGTH)
    messages = [
        {"role": "system", "content": "You are a language detector. You should return only the ISO 639-3 code of the text provided by user"},
        {"role": "user", "content": text}
    ]

    response = await client.beta.chat.completions.parse(
        model=chatgpt_model_name.value,
        messages=messages,
        response_format=TextLanguageFormat  # auto is default, but we'll be explicit
    )

    response_message = response.choices[0].message.parsed.language_ISO_639_3_code
    return response_message


def get_text_language(text: str, chatgpt_model_name: Optional[ChatGPTModelForTranslator] = None,
                      open_ai_api_key_for_this_translation: Optional[str] = None) -> str:
    """
    Detects the language of a given text using a specified ChatGPT model (ISO 639-3 code).

    Parameters:
    -----------
    Required:
    - text : str
        The text to detect the language of.

    Optional:
    - chatgpt_model_name : Optional[ChatGPTModelForTranslator], optional
        ChatGPT model for language detection. Default is None.
    - open_ai_api_key_for_this_translation : Optional[str], optional
        OpenAI API key for the translation. Default is None.

    Returns:
    --------
    str
        ISO 639-3 code of the detected language.

    """
    result = asyncio.run(async_get_text_language(text, chatgpt_model_name, open_ai_api_key_for_this_translation))
    return result


async def async_translate_text(text: str, to_language ="eng",
                               chatgpt_model_name: Optional[ChatGPTModelForTranslator] = None,
                               open_ai_api_key_for_this_translation: Optional[str] = None) -> str:
    global MAX_LENGTH
    global MAX_LENGTH_MINI_TEXT_CHUNK

    chatgpt_model_name, client = _get_setup_for_one_request(chatgpt_model_name, open_ai_api_key_for_this_translation)
    text_chunks = split_text_to_chunks(text, MAX_LENGTH)

    # Run how_many_languages_are_in_text concurrently
    # Chunks that contain more than one language will be split (this will simplify translation for the LLM)
    counted_number_of_languages = await asyncio.gather(*[how_many_languages_are_in_text(text_chunk, chatgpt_model_name,client) for text_chunk in text_chunks])

    tasks = []
    for index, text_chunk in enumerate(text_chunks):
        if counted_number_of_languages[index] > 1:
            mini_text_chunks = split_text_to_chunks(text_chunk, MAX_LENGTH_MINI_TEXT_CHUNK)
            for mini_text_chunk in mini_text_chunks:
                tasks.append(translate_chunk_of_text(mini_text_chunk, to_language, chatgpt_model_name, client))
        else:
            tasks.append(translate_chunk_of_text(text_chunk, to_language, chatgpt_model_name, client))

    translated_list = await asyncio.gather(*tasks)
    return " ".join(translated_list)


def translate(text, to_language ="eng",
              chatgpt_model_name: Optional[ChatGPTModelForTranslator] = None,
              open_ai_api_key_for_this_translation: Optional[str] = None) -> str: #ISO 639-3
    """
    Translates the given text to the specified language.

    Required Parameters:
    --------------------
    text (str):
        The text to be translated.

    to_language (str):
        The target language code (ISO 639-3). Default is "eng" (English).

    Optional Parameters:
    --------------------
    chatgpt_model_name (Optional[ChatGPTModelForTranslator]):
        The specific ChatGPT model to be used for this translation request.
        If not provided, the global/default model will be used.
        
        Line to import enums:
        from simpleaitranslator.utils.enums import ChatGPTModel
        
        Recommended enums are:
        - ChatGPTModelForTranslator.BEST_BIG_MODEL
        - ChatGPTModelForTranslator.BEST_SMALL_MODEL

    open_ai_api_key_for_this_translation (Optional[str]):
        An optional API key for OpenAI to be used specifically for this translation request.
        This is useful if you want to override the global API key for this particular request.
        Note that this will only work with the OpenAI client, not with the AzureOpenAI client.

    Returns:
    --------
    str:
        The translated text.
    """
    translated_text = asyncio.run(async_translate_text(text, to_language, chatgpt_model_name, open_ai_api_key_for_this_translation))
    return translated_text







