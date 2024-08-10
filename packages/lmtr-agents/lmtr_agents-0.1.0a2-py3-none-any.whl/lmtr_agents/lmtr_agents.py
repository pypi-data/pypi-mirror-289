"""
Define lmtr_agents.

https://www.kaggle.com/code/marcinrutecki/langchain-multiple-chains-simply-explained
synopsis = synopsis_chain.invoke({"title": title})
review = review_chain.invoke({"synopsis": synopsis})
summary = summary_chain.invoke({"review": review})

chain = (
    {"synopsis": synopsis_chain}
    | RunnablePassthrough.assign(review=review_chain)
    | RunnablePassthrough.assign(summary=summary_chain)
)
# Invoking the combined chain with the initial input
result = chain.invoke({"title": title})

chain = (
    {"text": RunnablePassthrough(), "trtext": agent_tr}   # <- text, to_lang
    | RunnablePassthrough.assign(refelection=agent_ref)  # <- text trtext
    | RunnablePassthrough.assign(ftext=agent_imp) # <- trtext, refelection
)

result = chain.invoke({"text": text, "to_lang": to_lang})

"""

import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI

from ycecream import y

from loguru import logger
from lmtr_agents.templates import template_tr, template_ref, template_imp, template_comb, template_comb_imp, template_comb_imp1

# from lmtr_agents.__init__ import agent_base_url, agent_api_key

agent_model = os.getenv("AGENT_MODEL")
agent_base_url = os.getenv("AGENT_BASE_URL")
agent_api_key = os.getenv("AGENT_API_KEY")

def lmtr_agents():
    """Define lmtr_agents."""
    logger.debug(" entry ")

# model_tr = ChatOpenAI(model=model, base_url=base_url, api_key=api_key,temperature=temperature, verbose=verbose)
# model_tr1 = ChatOpenAI(base_url="https://duck2api.dattw.eu.org/v1", api_key='any', temperature=temperature, verbose=verbose)
# model_tr2 = ChatOpenAI(base_url="https://duck2api.dattw.eu.org/v1", temperature=temperature, verbose=verbose)

load_dotenv()

# envs: OR_ NEWAPI
model, base_url, api_key = [*map(os.getenv, [f"OR_{elm}" for elm in ["MODEL", "BASE_URL", "API_KEY"]])]
if not all([model, base_url, api_key]):
    model, base_url, api_key = "gpt-4o-mini", "https://litellm.dattw.eu.org/v1", "any"
MODEL_4OM = ChatOpenAI(model=model, base_url=base_url, api_key=api_key,temperature=.3, verbose=0)

MODEL_DUCK = ChatOpenAI(base_url="https://duck2api.dattw.eu.org/v1", api_key="NA", temperature=.3, verbose=0)

model, base_url, api_key = [*map(os.getenv, [f"NEWAPI_{elm}" for elm in ["MODEL", "BASE_URL", "API_KEY"]])]

# LLM_ in .env
model, base_url, api_key = [*map(os.getenv, [f"LLM_{elm}" for elm in ["MODEL", "BASE_URL", "API_KEY"]])]

# if .env not present or LLM_ model, base_url, api_key no defined
if not all([model, base_url, api_key]):
    model, base_url, api_key = "gpt-3.5-turbo", "https://litellm.dattw.eu.org/v1", "any"

MODEL_GPT3 = ChatOpenAI(model=model, base_url=base_url, api_key=api_key,temperature=.3, verbose=0, name='llm')


def agent_tr(
    text: str,
    model=MODEL_GPT3,
    to_lang: str = "Chinese",
) -> str:
    """Translate."""
    prompt_tr = ChatPromptTemplate.from_template(template_tr)

    chat_template = ChatPromptTemplate.from_messages(
      [
        ("system", '''You are an expert {to_lang} translator. Your task is to translate TEXT into {to_lang}. You translate text into smooth and natural {to_lang} while maintaining the meaning in the original text.
        You only provide translated text and nothing else.'''),
        ("user", "{text}"),
       ]
    )
    del chat_template

    # messages = chat_template.format_messages(name="Alice", user_input="Can you tell me a joke?")
    # messages = chat_template.invoke({"text": text, "to_lang": to_lang})

    # model_tr = ChatOpenAI(model=model, base_url=base_url, api_key=api_key,temperature=temperature, verbose=verbose)

    # chain_tr = prompt_tr | model_tr | StrOutputParser()
    # chain_tr = chat_template | model_tr | StrOutputParser()
    chain_tr = prompt_tr | model | StrOutputParser()

    trtext = chain_tr.invoke({"to_lang": to_lang, "text": text})

    return trtext

def agent_ref(
    text: str,
    trtext: str,
    to_lang: str = "Chinese",
    model=MODEL_GPT3,
    # base_url: str = agent_base_url,
    # api_key: str = agent_api_key,
    # temperature: float = 0.3,
) -> str:
    """Reflect initial translation."""
    prompt_ref = ChatPromptTemplate.from_template(template_ref)
    # model_ref = ChatOpenAI(model=model, base_url=base_url, api_key=api_key,temperature=temperature, verbose=verbose)
    chain_ref= prompt_ref | model | StrOutputParser()
    edtext = chain_ref.invoke({"text": text, "to_lang": to_lang, "trtext": trtext})

    return edtext

def agent_imp(
    text: str,
    trtext: str,
    reflection: str,
    to_lang: str = "Chinese",
    model=MODEL_GPT3,
    # model: str = agent_model,
    # base_url: str = agent_base_url,
    # api_key: str = agent_api_key,
    # temperature: float = 0.3,
) -> str:
    # improve
    prompt_imp = ChatPromptTemplate.from_template(template_imp)
    # model_imp = ChatOpenAI(model=model, base_url=base_url, api_key=api_key,temperature=temperature, verbose=verbose)
    chain_imp = prompt_imp | model | StrOutputParser()
    ftext = chain_imp.invoke({"text": text, "to_lang": to_lang, "trtext": trtext, "reflection": reflection})

    return ftext

def agent_comb(
    text: str,
    translation1,
    translation2,
    # to_lang: str = "Chinese",
    model=MODEL_GPT3,
) -> str:
    # combine
    prompt_comb = ChatPromptTemplate.from_template(template_comb)
    chain_comb = prompt_comb | model | StrOutputParser()

    ctrtext = chain_comb.invoke({
        "text": text,
        "translation1": translation1,
        "translation2": translation2,
    })

    return ctrtext


def agent_comb_imp(
    # text: str,
    translation1,
    translation2,
    reflection: str,
    # to_lang: str = "Chinese",
    model=MODEL_GPT3,
) -> str:
    # combine and improve
    # template_comb_imp = translation1 translation2 reflection

    prompt_comb_imp = ChatPromptTemplate.from_template(template_comb_imp)
    chain_comb_imp = prompt_comb_imp | model | StrOutputParser()

    c_i_trtext = chain_comb_imp.invoke({
        # "text": text,
        "translation1": translation1,
        "translation2": translation2,
        "reflection": reflection,
    })

    # agent_ref:
    # text, trext -> reflection

    return c_i_trtext

def agent_comb_imp1(
    text: str,
    translation1,
    translation2,
    reflection: str,
    # to_lang: str = "Chinese",
    model=MODEL_GPT3,
) -> str:
    # combine and improve
    # template_comb_imp = text translation1 translation2 reflection

    prompt_comb_imp = ChatPromptTemplate.from_template(template_comb_imp1)
    chain_comb_imp = prompt_comb_imp | model | StrOutputParser()

    c_i_trtext1 = chain_comb_imp.invoke({
        "text": text,
        "translation1": translation1,
        "translation2": translation2,
        "reflection": reflection,
    })

    # agent_ref:
    # text, trext -> reflection

    return c_i_trtext1
