import os

message =  "期限ですよ〜"

def main():
    os.system("osascript -e 'display notification \"{}\"'".format(message))
if __name__ == '__main__':
    main()