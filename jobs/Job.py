import json


class Job:
    def __init__(self, json: dict):
        try:
            self.scraper = json['scraper']
            self.end_date = json['end_date']
            self.url_to_scrape = json['url_to_scrape']
            self.data = json['data']
        except Exception as e:
            raise Exception(f'invalid job json - {e}')

    @classmethod
    def from_str(self, json_str: str):
        return Job(json.loads(json_str))

    def __str__(self):
        return json.dumps(self.__dict__)
