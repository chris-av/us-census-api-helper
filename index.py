import os
from dotenv import load_dotenv
from lib.Census import Census

load_dotenv()
US_CENSUS_KEY = os.getenv("USCENSUS_KEY")
config = { "key": US_CENSUS_KEY , "survey": "acs/acs5", "year": 2021 }
census = Census(config)


zips = [90001,90002,90003,90007,90011,90015,90021,90022,90023,90033,90037,90040,90044,90058,90059,90061,90063,90089,90201,90220,90221,90222,90247,90248,90255,90262,90270,90280,90502,90723,90745,90746,90747,90805,90806,90807,90810,]

vars = census.getVariables()
zips_df = census.getPopulationByZip([ "B01001_001E" ], zips)
zips_df = zips_df[[ "zip code tabulation area", "B01001_001E" ]]
zips_df.to_csv("out/zip_pops.csv", sep=",", encoding="utf-8", index=False)
print(zips_df)

