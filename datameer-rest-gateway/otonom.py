import schedule
import time
import requests

url = 'http://localhost:5000/test'


class Otonom:

    def job(self):
        print "I'm working..."
        response = requests.get(url)
        print response.content

    def scheduler(self):
        schedule.every(1).minutes.do(self.job)
        schedule.every().hour.do(self.job)
        schedule.every().day.at("20:20").do(self.job)
        while 1:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    o = Otonom()
    o.scheduler()
