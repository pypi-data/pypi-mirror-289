import re
from openai import OpenAI
from openai import AzureOpenAI
import json
from simpleaitranslator.exceptions import MissingAPIKeyError, NoneAPIKeyProvidedError, InvalidModelName
from simpleaitranslator.utils.enums import ChatGPTModel
from simpleaitranslator.utils.function_tools import tools_get_text_language, tools_translate
from pydantic import BaseModel

CHATGPT_MODEL_NAME = ChatGPTModel.BEST_BIG_MODEL.value
client = None
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
    global client
    client = OpenAI(api_key=api_key)

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
    global client
    client = AzureOpenAI(
        azure_endpoint=azure_endpoint,
        api_key=api_key,
        api_version=api_version,
        azure_deployment=azure_deployment
    )

def set_chatgpt_model(chatgpt_model_name: ChatGPTModel | str):
    """
    Sets the default ChatGPT model.

    This function allows you to change the default ChatGPT model used in the application.
    You can assign either a string representing the name of the GPT model or
    ENUMS (recommended approach) to the chatgpt_model_name variable

    Line to import enums:
    from simpleaitranslator.utils.enums import ChatGPTModel

    Parameters:
    chatgpt_model_name (str or ChatGPTModel): The name of the ChatGPT model to set. Recommended values are:
    For enums:
        - ChatGPTModel.BEST_BIG_MODEL
        - ChatGPTModel.BEST_SMALL_MODEL
    For strings:
        - "gpt-4o-2024-08-06"
        - "gpt-4o-mini"

    Raises:
    InvalidModelName: If the provided model name is not valid.
    ValueError: If the chatgpt_model_name is None or in an incorrect format.
    """
    def validate_model(model_to_check: str) -> None:
        if model_to_check not in {model.value for model in ChatGPTModel}:
            raise InvalidModelName(invalid_model_name=model_to_check)

    global CHATGPT_MODEL_NAME
    if type(chatgpt_model_name) ==ChatGPTModel:
        CHATGPT_MODEL_NAME = chatgpt_model_name.value
    elif type(chatgpt_model_name) == str and validate_model(chatgpt_model_name):
        CHATGPT_MODEL_NAME = chatgpt_model_name
    else:
        raise ValueError('chatgpt_model name is required - current value is None or have wrong format')


def get_first_thousand_words(text: str) -> str:
    words = re.split(r'\s+', text)
    words = words[0:MAX_LENGTH]
    return ' '.join(words)



def get_text_language(text):
    global client
    if not client:
        raise MissingAPIKeyError()

    text = get_first_thousand_words(text)
    messages = [
        {"role": "system", "content": "You are a language detector. You should return the ISO 639-3 code to the get_from_language function of user text."},
        {"role": "user", "content": text}
    ]

    response = client.chat.completions.create(
        model=CHATGPT_MODEL_NAME,
        messages=messages,
        tools=tools_get_text_language,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    if tool_calls:
        #print(tool_calls)
        tool_call = tool_calls[0]
        function_args = json.loads(tool_call.function.arguments)
        return function_args.get("iso639_3")

    return None


def translate_chunk_of_text(text_chunk: str, to_language: str) -> str:
    global client
    if not client:
        raise MissingAPIKeyError()

    number_of_languages_in_text_chunk = how_many_languages_are_in_text(text_chunk)

    messages = [
        {"role": "system",
         "content": f"You are a language translator. You should translate the text to the {to_language} language and then put the result of the translation into the display_translated_text function"},
        {"role": "user", "content": text_chunk}
    ]

    response = client.chat.completions.create(
        model=CHATGPT_MODEL_NAME,
        messages=messages,
        tools=tools_translate,
        tool_choice="auto",
    )

    response_message = response.choices[0].message
    messages.append(response_message)  # extend conversation with assistant's reply

    tool_calls = response_message.tool_calls
    if tool_calls:
        tool_call = tool_calls[0]
        function_args = tool_call.function.arguments

        # Attempt to parse the function arguments
        try:
            function_args_dict = json.loads(function_args)
            return function_args_dict.get("translated_text")
        except json.JSONDecodeError:
            # Inform the chatbot to correct the format
            print("Error")
            print(function_args)
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": "translated_text",
                    "content": "Error Please ensure the translated text is returned as a JSON object with the key 'translated_text'.",
                }
            )
            response = client.chat.completions.create(
                model=CHATGPT_MODEL_NAME,
                messages=messages,
                tools=tools_translate,
                tool_choice="auto",
            )
            response_message = response.choices[0].message
            messages.append(response_message)

            tool_calls = response_message.tool_calls
            if tool_calls:
                tool_call = tool_calls[0]
                function_args = tool_call.function.arguments
                function_args_dict = json.loads(function_args)
                return function_args_dict.get("translated_text")

    return None



def split_text_to_chunks(text, max_lenght):
    global WORD_TOKEN_MULTIPLY
    splited_text = re.split(r'\s+', text)
    last_comma_index = -1
    last_dot_index = -1
    last_index = 0
    chunks_of_text = []


    for index, word in enumerate(splited_text):
        if "," in word:
            last_comma_index = index
        if "." in word or "?" in word or "!" in word:
            last_dot_index = index

        if (index - last_index + 1) > max_lenght:
            if last_dot_index >= last_index:
                chunks_of_text.append(splited_text[last_index:last_dot_index + 1])
                last_index = last_dot_index + 1
            elif last_comma_index >= last_index:
                chunks_of_text.append(splited_text[last_index:last_comma_index + 1])
                last_index = last_comma_index + 1
            else:
                chunks_of_text.append(splited_text[last_index:index+1])
                last_index = index + 1

    # Add the last chunk
    if last_index < len(splited_text):
        chunks_of_text.append(splited_text[last_index:])

    # Verify the chunks
    check_sentence = [word for chunk in chunks_of_text for word in chunk]

    for index, word in enumerate(check_sentence):
        if word != splited_text[index]:
            print("Error Error")

    return [" ".join(chunk) for chunk in chunks_of_text]


def translate(text, to_language ="eng") -> str: #ISO 639-3
    """
    Translates the given text to the specified language.

    Parameters:
    text (str): The text to be translated.
    to_language (str): The target language code (ISO 639-3). Default is "eng" (English).

    Returns:
    str: The translated text.
    """
    global MAX_LENGTH
    global MAX_LENGTH_MINI_TEXT_CHUNK
    text_chunks = split_text_to_chunks(text, MAX_LENGTH)
    #print(text_chunks)
    translated_list = []
    for index, text_chunk in enumerate(text_chunks):
        if how_many_languages_are_in_text(text_chunk) > 1:
            mini_text_chunks = split_text_to_chunks(text_chunk, MAX_LENGTH_MINI_TEXT_CHUNK)
            for mini_text_chunk in mini_text_chunks:
                translated_list.append(translate_chunk_of_text(mini_text_chunk, to_language))
        else:
            translated_tex = translate_chunk_of_text(text_chunk, to_language)
            translated_list.append(translated_tex)

    #print(translated_list)
    #print(len(translated_list))
    return " ".join(translated_list)


class HowManyLanguages(BaseModel):
    number_of_languages: int

def how_many_languages_are_in_text(text):
    global CHATGPT_MODEL_NAME
    global client
    completion = client.beta.chat.completions.parse(
        model=CHATGPT_MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are text languages counter you should count how many languaes are in provided by user text"},
            {"role": "user", "content": f"Please count how many languaes are in this text:\n{text}"},
        ],
        response_format=HowManyLanguages,
    )
    event = completion.choices[0].message.parsed.number_of_languages
    return event

