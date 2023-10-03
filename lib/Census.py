import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote, urlencode
import requests
import re



class Census:
    def __init__(self, config):
        self.key = config["key"]
        self.survey = config["survey"]
        self.year = config["year"]
        self.base_link = "https://api.census.gov/data/{}/{}".format(self.year, self.survey)

    def setSurvey(self, survey):
        self.survey = survey
        print("now using survey : {}".format(survey))
        pass

    def displaySurvey(self):
        print("currently using survey : {}".format(self.survey))
        pass

    def getPopulationByZip(self, vars, zips):
        zips = map(str, zips)
        zips = ",".join(zips)
        query_params = urlencode({ 
                                  "key": self.key, 
                                  "get": ",".join(vars), 
                                  "for": "zip code tabulation area:{}".format(zips), 
                                  }, quote_via=quote)
        req_str = self.base_link + "?" + query_params
        print("making request to : {}\n".format(req_str))

        response = requests.get(req_str)
        if (response.status_code != 200):
            print(response.status_code)
            print(response.content)
            return "something went wrong ... "
        
        response_data = response.json()
        columns = response_data[0]
        data = response_data[1:]
        df = pd.DataFrame(data, columns=columns)

        return df

    # TODO: request takes too long, cache it locally
    def getVariables(self):
        req_str = "{}/variables.html".format(self.base_link)
        print("making request to : {}\n".format(req_str))
        response = requests.get(req_str)
        if (response.status_code != 200):
            print(response.status_code)
            print(response.content)
            return "something went wrong ... "
        soup = BeautifulSoup(response.content, features='html.parser')
        headers = []
        thead = soup.find('thead')
        for th in thead.find_all('th'):
            headers.append(th.text)
        rows = []
        tbody = soup.find('tbody')
        for tr in tbody.find_all('tr'):
            row = []
            for td in tr.find_all('td'):
                clean_txt = re.sub("\\n", "", td.text)
                clean_txt = re.sub("\\t", "", clean_txt)
                row.append(clean_txt)
            rows.append(row)
        vars_df = pd.DataFrame(rows, columns=headers)
        filepath = "out/{}--{}.csv".format(self.survey.replace("/", "-"), self.year)
        vars_df.to_csv(filepath, index=False)
        print(vars_df)
        return vars_df


    # TODO: global error handler
    def handleError(self, err):
        pass


