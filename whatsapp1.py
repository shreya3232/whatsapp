


# group_number = 'DgQh4trIoZo0RC3h19JKnC'
import openpyxl
import pywhatkit as pwk
from phonenumbers.phonenumberutil import NumberParseException
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

group_number = 'KZkdX4l7XJX5qAoxoN6RCU'
processed_rows = set()

class ExcelFileHandler(FileSystemEventHandler):
    def __init__(self, filename):
        self.filename = filename

    def on_modified(self, event):
        if not event.is_directory and event.src_path == self.filename:
            process_excel_file(self.filename)

def process_excel_file(filename):
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=3, values_only=True):
        slno = row[0]
        name = row[1]
        city = row[2]
        location = row[3]
        squarefeet = row[4]

        message = f"Sl No: {slno}\nName: {name}\nCity: {city}\nLocation: {location}\nSquare Feet: {squarefeet}"

        if row in processed_rows:
            print(f"Skipping duplicate row: {row}")
            continue

        try:
            current_time = time.localtime()
            time_hour = current_time.tm_hour
            time_min = current_time.tm_min + 1

            wait_time = 10 # Set the wait_time as desired

            pwk.sendwhatmsg_to_group(group_number, message, time_hour, time_min, wait_time)
            processed_rows.add(row)
        except NumberParseException:
            print(f"Country code missing for WhatsApp group: {group_number}")

def watch_excel_file_changes(filename):
    event_handler = ExcelFileHandler(filename)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    print(f"Watching for changes in {filename}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    excel_filename = 'fgsdhj.xlsx'
    process_excel_file(excel_filename)  # Initial processing before watching for changes
    watch_excel_file_changes(excel_filename)
