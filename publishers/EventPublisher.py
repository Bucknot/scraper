from publishers.Event import Event


class EventPublisher(object):
    def __init__(self, configs):
        self.validate_configs()
        self.configs = configs

    def validate_configs(self):
        raise NotImplementedError('scrape method not implemented')

    def publish(self, event: Event):
        raise NotImplementedError('scrape method not implemented')
