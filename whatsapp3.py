import openpyxl
import pywhatkit as pwk
from phonenumbers.phonenumberutil import NumberParseException
import time

group_number = 'KZkdX4l7XJX5qAoxoN6RCU'
last_processed_row =8
# wait_time = 10 
def process_excel_file():
    global last_processed_row
    
    workbook = openpyxl.load_workbook('exceltowhatsapp.xlsx')
    sheet = workbook.active
    max_row = sheet.max_row

    for row_number in range(last_processed_row, max_row + 1):
        row = [cell.value for cell in sheet[row_number]]

        slno = row[0]
        EnquiryDate = row[1]
        ContactPerson = row[2]
        State = row[3]
        City = row[4]
        PhNo=row[5]
        SqftRequired=row[6]
        e=row[7]
        TypeofCustomer=row[8]
        Enquirydetails=row[9]
        Reference=row[10]
        LeadPassedto=row[11]
        LeadPassDate= row[12]
        LeadSentby=row[13]
        
        message = f"ContactPerson: {ContactPerson}\nState: {State}\nCity: {City}\nPhNo:{PhNo}\nSqftRequired:{SqftRequired}\nReference:{Reference}"

        try:
            current_time = time.localtime()
            time_hour = current_time.tm_hour
            time_min = current_time.tm_min +1

            wait_time = 10  # Set the wait_time as desired

            pwk.sendwhatmsg_to_group(group_number, message, time_hour, time_min, wait_time)
            last_processed_row = row_number + 1
        except NumberParseException:
            print(f"Country code missing for WhatsApp group: {group_number}")

def run_code_continuously():
    while True:
        process_excel_file()
        time.sleep(20)  # Delay between iterations (e.g., 1 minute)

if __name__ == '__main__':
    process_excel_file()  # Initial processing
    run_code_continuously()
