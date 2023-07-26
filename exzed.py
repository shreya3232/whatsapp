import openpyxl
import pywhatkit as pwk
from phonenumbers.phonenumberutil import NumberParseException
import time
workbook = openpyxl.load_workbook('fgsdhj.xlsx')
sheet = workbook.active

# Define a dictionary to map cities to WhatsApp groups
city_groups = {
    'bangalore': 'FlUU8g5Zng0DOsH1ONQDey',
    'mangalore': 'H8fGrC7ICVT8qmroSsGXAE',
   
}
processed_groups = set()

for row in sheet.iter_rows(min_row=3, values_only=True):
    slno = row[0]
    name = row[1]
    city = row[2]
    location = row[3]
    squarefeet = row[4]
    
    message = f"Sl No: {slno}\nName: {name}\nCity: {city}\nLocation: {location}\nSquare Feet: {squarefeet}"
    
    # Check if the city has a corresponding WhatsApp group
    if city in city_groups:
        group_number = city_groups[city]
        print(group_number)
        if group_number in processed_groups:
            print(f"Skipping duplicate message for WhatsApp group number: {group_number}")
            continue
        
        try:
            
            current_time = time.localtime()
            time_hour = current_time.tm_hour
            time_min = current_time.tm_min + 1
           
            wait_time = 10  # Set the wait_time as desired
             
            pwk.sendwhatmsg_to_group(group_number,message, time_hour, time_min, wait_time)
            processed_groups.add(group_number)
        except NumberParseException:
            print(f"Country code missing for WhatsApp group: {group_number}")
    else:
        print(f"No WhatsApp group found for city: {city}")
