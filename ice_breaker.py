from langchain.prompts.prompt import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os
import sys
from langchain.llms import OpenAI

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.twitter import scrape_user_tweets
from output_parsers import person_intel_parser, PersonIntel

name="Harrison Chase"

def ice_break(name: str) -> Tuple[PersonIntel, str]:
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
    given the linkedin information{linkedin_information} and {twitter_information}about a person ,I want you to create :
    1. a short summary
    2. two intersting facts about them
    3. A topic that may interest them
    4. 2 creative Ice breakers to open a conversation with them
        \n{format_instructions}
    """
    # linkedin_data = scrape_linkedin_profile(
    #     "https://www.linkedin.com/in/arun-purakkatt-mba-mtech/"
    # )

    linkedin_url=linkedin_lookup_agent(name=name)
    linkedin_data=scrape_linkedin_profile(linkedin_profile_url=linkedin_url)
    twitter_username=twitter_lookup_agent(name=name)
    tweets=scrape_user_tweets(username=twitter_username,num_tweets=5)

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information","twitter_information"], template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    
    result=chain.run(linkedin_information=linkedin_data,twitter_information=tweets)
    print(result)
    return person_intel_parser.parse(result), linkedin_data.get("profile_pic_url")

if __name__ == "__main__":
    print("Hello LangChain!")
    result = ice_break(name="Harrison Chase")
    print(result)