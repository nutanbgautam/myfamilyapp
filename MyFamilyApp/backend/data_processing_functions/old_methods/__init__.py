from .csv_processing import load_data_from_csv
from .write_to_database import write_to_database

csvLoadedData=load_data_from_csv()
write_to_database(csvLoadedData)
