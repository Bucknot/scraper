import json

from jobs.Job import Job
from publishers.Event import Event


class Scraper:
    def __init__(self, jobs: list[Job]):
        self.jobs = jobs

    def scrape(self) -> list[Event]:
        events = []
        for job in self.jobs:
            if self._validate_job_data(job):
                events.append(self._handle_job(job))
            else:
                print(f'invalid job data - {job}')
        return events

    def _handle_job(self, job: Job) -> Event:
        raise NotImplementedError('scrape method not implemented')

    def _validate_job_data(self, job: Job) -> bool:
        try:
            job_data_dict = json.loads(job.data)
            return self._validate_job_data_dict(job_data_dict)
        except Exception as e:
            return False

    def _validate_job_data_dict(self, job_data_dict: dict) -> bool:
        raise NotImplementedError('scrape method not implemented')