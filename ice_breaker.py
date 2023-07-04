from langchain.prompts.prompt import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os
import sys
from langchain.llms import OpenAI

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
information = """
Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business magnate and investor. He is the founder, CEO, and chief engineer of SpaceX; angel investor, CEO, and product architect of Tesla, Inc.; owner, CTO, and chairman of Twitter; founder of the Boring Company and X Corp.; co-founder of Neuralink and OpenAI; and president of the philanthropic Musk Foundation. Musk is the wealthiest person in the world according to the Bloomberg Billionaires Index and Forbes's Real Time Billionaires list as of June 2023, primarily from his ownership stakes in Tesla and SpaceX, with an estimated net worth of around $225 billion according to Bloomberg and $230.2 billion according to Forbes.[4][5][6]

Musk was born in Pretoria, South Africa, and briefly attended the University of Pretoria before moving to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University and transferred to the University of Pennsylvania, where he received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University. After two days, he dropped out and, with his brother Kimbal, co-founded the online city guide software company Zip2. In 1999, Zip2 was acquired by Compaq for $307 million and Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal, which eBay acquired for $1.5 billion in 2002.

With $175.8 million, Musk founded SpaceX in 2002, a spaceflight services company. In 2004, he was an early investor in the electric vehicle manufacturer Tesla Motors, Inc. (now Tesla, Inc.). He became its chairman and product architect, assuming the position of CEO in 2008. In 2006, he helped create SolarCity, a solar energy company that was later acquired by Tesla and became Tesla Energy. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year, he co-founded Neuralink—a neurotechnology company developing brain–computer interfaces—and the Boring Company, a tunnel construction company. Musk has also proposed a hyperloop high-speed vactrain transportation system. In 2022, his acquisition of Twitter for $44 billion was completed.

Musk has expressed views that have made him a polarizing figure. He has been criticized for making unscientific and misleading statements, including that of spreading COVID-19 misinformation. In 2018, the U.S. Securities and Exchange Commission (SEC) sued Musk for falsely tweeting that he had secured funding for a private takeover of Tesla. Musk stepped down as chairman of Tesla and paid a $20 million fine as part of a settlement agreement with the SEC.
"""

if __name__ == "__main__":
    print("hello Lang chain")
    #print(os.environ['OPENAI_API_KEY'])

    # summary_template = """
    # given a short information{information} about a person ,I want you to create :
    # 1. a short summary
    # 2. two intersting facts about them
    # """
    # summary_prompt_template = PromptTemplate(input_variables=["information"],template=summary_template)
    # llm=ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo")
    # chain=LLMChain(llm=llm,prompt=summary_prompt_template)

    # print(chain.run(information=information))

    summary_template = """
    given a short information{information} about a person ,I want you to create :
    1. a short summary
    2. two intersting facts about them
    """
    # linkedin_data = scrape_linkedin_profile(
    #     "https://www.linkedin.com/in/arun-purakkatt-mba-mtech/"
    # )

    linkedin_url=linkedin_lookup_agent(name='Andrew Ng Landing AI')

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)
    # print(chain.run(information=linkedin_data))
    print(chain.run(information=linkedin_data))
