import schedule
import time
class Otonom:
    def job(self):
        print("I'm working...")
    def scheduler(self):
        schedule.every(1).minutes.do(self.job)
        schedule.every().hour.do(self.job)
        schedule.every().day.at("16:11").do(self.job)
        while 1:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    o=Otonom()
    o.scheduler()