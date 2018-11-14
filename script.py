from config import file_name
from config import interval
from config import output
import datetime
import time
import psutil
import json


class GetStatus:
    def getTimestamp(self):
        timeInit = time.time()
        timestamp = datetime.datetime.fromtimestamp(timeInit).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        return timestamp

    def getCPU(self):
        return str(psutil.cpu_percent()) + "%"

    def getVirtMemTotal(self):
        return str(psutil.virtual_memory().total / 1024 / 1024) + "Mb"

    def getVirtMemUsed(self):
        return str(psutil.virtual_memory().used / 1024 / 1024) + "Mb"

    def getIOInf(self):
        return str(psutil.disk_io_counters())

    def getNetConn(self):
        return str(psutil.net_connections()[0])


class WriteToFile(GetStatus):
    def writeTXT(self):
        sc = 1
        while True:
            output_file = open(file_name, "a")
            output_file.write(
                 "SNAPSHOT: "
                 + str(sc)
                 + " "
                 + GetStatus.getTimestamp(self)
                 + "  CPU percent: "
                 + GetStatus.getCPU(self)
                 + "  Overall_virtual_memory_size: "
                 + GetStatus.getVirtMemTotal(self)
                 + "  Overall_virtual_memory_usage: "
                 + GetStatus.getVirtMemUsed(self)
                 + "  IO_information: "
                 + GetStatus.getIOInf(self)
                 + "  Network_information:"
                 + GetStatus.getNetConn(self)[0])
            output_file.close()
            time.sleep(int(interval))
            sc += 1

    def writeJSON(self):
        sc = 1
        while True:
            jsonf = open(file_name, "a")
            jsonf.write("\n{ \n")
            jsonf.write(
                '\n"SNAPSHOT {0}": "{1}",
                 \n'.format(sc, GetStatus.timestamp(self))
            )
            jsonf.write('\n"CPU":\n')
            json.dump({"Percent": GetStatus.getCPU(self)}, jsonf, indent=1)
            jsonf.write('\n,"Overall":\n')
            json.dump(
                {"Virt Mem Size": GetStatus.getVirtMemTotal(self)}, jsonf, indent=1
            )
            jsonf.write('\n,"Overall": \n')
            json.dump(
                {"Virt Mem Used Size": GetStatus.getVirtMemUsed(self)}, jsonf, indent=1
            )
            jsonf.write('\n,"IO":\n')
            json.dump({"Stat": GetStatus.getIOInf(self)}, jsonf, indent=1)
            jsonf.write('\n,"Network":\n')
            json.dump({"Stat": GetStatus.getNetConn(self)}, jsonf, indent=1)
            jsonf.write("\n\n")
            jsonf.write("\n} \n")
            jsonf.close()
            sc += 1
            time.sleep(int(interval))

    def typeOfLogChecker(self):
        if output == "json":
            WriteToFile.writeJSON("status_log.json")
        elif output == "text":
            WriteToFile.writeTXT("status_log.txt")
        else:
            print("check config")


t = WriteToFile()
t.typeOfLogChecker()
