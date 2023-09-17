from backend_functions.collect_data import *
from backend_functions.create_table import *
from backend_functions.get_data import *
from backend_functions.create_SQL_database import *

url = "https://moskva.mts.ru/personal/mobilnaya-svyaz/tarifi/vse-tarifi/mobile-tv-inet"
#get_data(url=url)
#data = collect_data()
#create_table(data)
create_SQL_database()