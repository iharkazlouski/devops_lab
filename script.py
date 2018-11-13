from config import file_name
from config import interval
from config import output
from datetime import datetime
import json
import psutil
from time import sleep


def status():
    get_info = {"Overall_CPU_load": str(psutil.cpu_percent()) + "%",
                "Overall_memory_size": str(psutil.virtual_memory().total),
                "Overall_memory_usage": str(psutil.virtual_memory().used),
                "IO_information": str(psutil.disk_io_counters()),
                "Network_information": str(psutil.net_connections()[0]),
                "Network_information1": str(psutil.net_connections()[1]),
                "Network_information2": str(psutil.net_connections()[2])
                }
    return get_info


counter = 0
if output == "text":
    while True:
        get_status = status()
        output_file = open(file_name, "a")
        output_file.write("SNAPSHOT" + str(counter) + " : ")
        output_file.write(str(datetime.today()) + " : ")
        for _ in get_status:
            output_file.write(_ + " : " + get_status[_] + "\n")
        output_file.write("\n")
        output_file.close()
        get_status.clear()
        counter += 1
        sleep(interval)

if output == "json":
    get_status = {}
    while True:
        get_status["SNAPSHOT"] = str(counter)
        get_status["timestamp"] = str(datetime.today())
        get_status["status"] = status()
        output_file = open(file_name, "a")
        output_file.write(json.dumps(get_status) + "\n\n")
        output_file.close()
        get_status.clear()
        counter += 1
        sleep(interval)
