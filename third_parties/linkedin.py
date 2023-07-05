import requests
import os


def scrape_linkedin_profile(linkedin_profile_url: str):
     
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
     
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

  
    # # print(response.json())

    # print(response._content)

    # gist_response = requests.get(
    #     "https://gist.githubusercontent.com/Arun-purakkatt/a7343a9811e758b18c412f9e342306a2/raw/5a8ecc4314cc32e3d6e917a3242bd398db394262/arun-purakkatt.json"
    # )
    # print(gist_response.json())
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data
