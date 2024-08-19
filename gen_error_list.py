from utility import *

my_dict = get_error_dict_from_txt()
for key, value in my_dict.items():
    print(f"{key}: '{value}',")

print(get_raw_size_from_txt())