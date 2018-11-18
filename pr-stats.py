import datetime
import getpass
import requests

user = input("Input Github Login: ")
password = getpass.getpass()


def exitCommand():
    quit()


def help_usage():
    """HELP"""
    print("""Usage:
           pr-stats [options] [user]
           pr-stats --version
           pr-stats (-h | --help)
           Options:
           -h --help                  Show help.
           --version                  Print version
           --dayCreated               Show day of the week
           --hourCreated              Show hour opened file
           --userCreated              Show user who opened
           --quit                     Quit
           --attachedLabels           Analyze attached labels.
           --basic                    Basic stats about merged/closed rate""")


# help_usage()

url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls?state=all'
req = requests.get(url, auth=(user, password))
out = []
out += req.json()

while 'next' in req.links.keys():
    next_url = req.links['next']['url']
    req = requests.get(next_url,
                       auth=(user, password))
    out += req.json()


def version():
    print("Version 1.01")


def dayCreated(myjson, value):
    date = myjson[value][:10].split('-')
    print('Day of the week ' + value + ': ')
    print(str(datetime.datetime(int(date[0]),
          int(date[1]), int(date[2])).strftime("%a")))


def hourCreated(myjson, value):
    print("Pull request " + str(myjson["number"]) + ": hour of the day ")
    print(str(value) + ' ' + myjson[value][11:13])


def userCreated(myjson):
    print("Pull request " + str(myjson["number"]) + ": user who opened is: ")
    print(myjson["user"]["login"])


def attachedLabels(myjson):
    print("Pull request " + str(myjson["number"]) + ": attached labels: ")
    print(myjson["head"]["label"] + ', ' + myjson["base"]["label"])


def basic(myjson):
    print("Pull request " + str(myjson["number"]) + " is: " + myjson["state"])
    if myjson["merged_at"] is not None:
        print("Pull request " + str(myjson["number"]) + " is: merged")


def callingRequest(option, input, myjson):
    for i in myjson:
        if i["user"]["login"] == input[2]:
            if option == '--dayCreated':
                dayCreated(i, "created_at")
                break
            elif option == '--hourCreated':
                hourCreated(i, "created_at")
                break
            elif option == '--userCreated':
                userCreated(i)
                break
            elif option == '--attachedLabels':
                attachedLabels(i)
                break
            elif option == '--basic':
                basic(i)
                break
            else:
                print("Error,please input again (use pr-stats (-h ))")
            break


while True:
    try:
        humanInput = input().split(' ')
        if humanInput[0] != 'pr-stats':
            raise Exception("Error please input again (use pr-stats (-h))")
        options = humanInput[1]
        if options == '--version':
            version()
        elif options == '-h' or options == '--help':
            help_usage()
        elif options == '-q' or options == '--quit':
            break
        elif len(humanInput) == 3:
            callingRequest(options, humanInput, out)
    except Exception as error:
        print(error)
