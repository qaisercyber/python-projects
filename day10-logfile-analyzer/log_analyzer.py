import re


def read_log_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")
        return


def extract_ips(log_text):
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    return re.findall(ip_pattern, log_text)

def date_extract(log_text):
    date_pattern = r"\b\d{4}-\d{2}-\d{2}\b"
    return re.findall(date_pattern, log_text)

def extract_errors(log_text):
    error_pattern = r"ERROR\s+(.*)"
    return re.findall(error_pattern, log_text)


def display_results(ips, dates ,errors):
    print("-----Log Analysis Report-----")
    print("-"*40)
    print("\n Ip addresses Found are:")
    for ip in ips:
        print("-" , ip)
    print("\n Dates found are")
    for date in dates:
        print("-" , date)

    print("\n Errors found are:")

    if errors:
        for error in errors:
            print("-" , error)
    else:
        print("No errors found")


def main():
    while True:


        file_name = input("Enter file name: or q to quit: anytime ")
        if file_name == "q":
            break
        else:
            log_text = read_log_file(file_name)
            if not log_text:
                return
            else:
                ips = extract_ips(log_text)
                dates = date_extract(log_text)
                errors = extract_errors(log_text)
                display_results(ips, dates, errors)


if __name__ == "__main__":
    main()





