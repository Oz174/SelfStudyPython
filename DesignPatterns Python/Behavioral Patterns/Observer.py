class Subject:
    def __init__(self):
        self.__observers = []

    def register_observer(self, observer):
        self.__observers.append(observer)

    def notify_observers(self, message):
        for observer in self.__observers:
            observer.notify(message)


class Observer:
    def notify(self, message):
        pass


class EmailAlerts(Observer):
    def notify(self, message):
        print(f"Email Alert: {message}")


class SMSAlerts(Observer):
    def notify(self, message):
        print(f"SMS Alert: {message}")


if __name__ == "__main__":
    print("Welcome to Observer Pattern")
    print("This class aims to notify all the observers when a change occurs in the subject")
    subject = Subject()  # => to be observed
    email_alerts = EmailAlerts()  # => observer
    sms_alerts = SMSAlerts()  # => observer
    print("Registering Observers ...")
    subject.register_observer(email_alerts)
    subject.register_observer(sms_alerts)
    print("Registered Observers Successfully")
    print("Notifying Observers ...")
    subject.notify_observers("Alert: System is down")
    subject.notify_observers("Alert: Server is down")
    subject.notify_observers("Alert: Network is down")
