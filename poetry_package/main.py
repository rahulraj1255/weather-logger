#Takes in an optional boolean argument (do_logging)

from weather_logger.get_weather_info import log_weather
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--do_logging', action='store_true')
arg=parser.parse_args()
print(arg)
url="https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
params={'dataType':'rhrread', 'lang':'en'}
temp_loc="King's Park"
rain_loc="Wan Chaia"
a=log_weather(temp_loc, rain_loc, url,params,arg.do_logging)
a.log_data()
