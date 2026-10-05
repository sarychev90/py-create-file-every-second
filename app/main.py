from datetime import datetime
from time import sleep


def main():
    while True:
        c_time = datetime.now()
        try:
            file_name = f"app-{c_time.hour}_{c_time.minute}_{c_time.second}.log"
            with open(file_name, "w") as file:
                c_time_str = c_time.strftime("%Y-%m-%d %H:%M:%S")
                file.write(c_time_str)
                print(f"{c_time_str} {file_name}")
            sleep(1)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
