import csv
import argparse

class Cookie:
    def __init__(self):
        pass

    # Main function - takes cookie_log.csv and finds the cookies that appear the most times in the specified date
    # input: day
    # output: array of most active cookies on day
    # If more than one cookie appears for the max times, prints all cookies that appear max times
    def most_cookie(file_path, day):
        # Go through csv and assign it to list cookies
        # list of cookies with timestamps
        cookies = []  
        # open csv file and read it
        # throw exception if file not found
        try:
            file = open(file_path, 'r')
        except FileNotFoundError:
            raise FileNotFoundError
        
        csvreader = csv.reader(file)
        for row in csvreader:
            if(not row[1] == "timestamp"):
                cookies.append(row)
                cookies[-1].append("")
                cookies[-1][1], cookies[-1][2] = cookies[-1][1].split("T")
        # list of cookies and timestamps on target date
        targetCookies = []  
        # dictionary that will be used to store the activeness of each cookie
        cookieActiveness = {} 
        # list that stores cookies used on target date
        targetCookieList = []  

        # Go through cookies and find the ones with the target date
        # Since cookies are given in reverse chronological order, we can end
        # the loop once we have stopped looking at cookies with the target date
        isDay = False
        for i in cookies:
            if (isDay and not i[1] == day):
                break
            elif (not isDay and i[1] == day):
                isDay = True
            if (isDay):
                targetCookies.append(i)

        # Go through cookies in the day and store in dictionary times
        # entry with key = cookie and value = number of times it occurs on the target day
        # If cookie is not encountered before, set cookieActiveness[cookie] to be 1 and add to ordered
        for i in targetCookies:
            if (i[0] in cookieActiveness.keys()):
                cookieActiveness[i[0]] += 1
            else:
                cookieActiveness[i[0]] = 1
                targetCookieList.append(i[0])

        # Get the maximum value of cookie occurences
        max = 0
        for i in targetCookieList:
            if (cookieActiveness[i] > max):
                max = cookieActiveness[i]

        mostActive = []  # list of most active cookies
        # Go through cookies on the target day and print the ones with max occurences
        for i in targetCookieList:
            if (cookieActiveness[i] == max):
                mostActive.append(i)

        return mostActive


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Finds most active cookie")

    # defining arguments for parser object
    # only argument is -d for date
    parser.add_argument("-d", "--date", type=str, nargs=1,
                        metavar="date", default=None,
                        help="takes a date to find the most active cookie")
    parser.add_argument("-p", "--path", type=str, nargs=1, default ="cookie_logs/cookie_log_1.csv", help = "path to a cookie file")
    path = "cookie_logs/cookie_log_1.csv"
    args = parser.parse_args()
    if args.date != None:
        day = args.date[0]
    else:
        raise Exception("Please provide a date with -d date")
    if args.path != None:
        path = args.path

    for i in (Cookie.most_cookie(path, day)):
        print(i)
