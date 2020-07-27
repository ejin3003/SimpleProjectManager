import doctest


class TicketQueue(object):
    def __init__(self):
        self.lst = []

    def add_person(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added to the queue
        """
        self.lst.append(name)
        print(f"{name} has been added to the queue")

    def service_person(self):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added to the queue
        >>> queue.service_person()
        Jack has been serviced
        """
        name = self.lst.pop(0)
        print(f"{name} has been serviced")

    def bypass_queue(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added to the queue
        >>> queue.bypass_queue("Jill")
        Jill has bypassed the queue
        """
        self.lst.insert(0, name)
        print(f"{name} has bypassed the queue")


doctest.testmod(name="TicketQueue", verbose=True)
