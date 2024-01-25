from scrapers.Scraper import Scraper
from publishers.Event import Event


class MaccabiScraper(Scraper):
    def __init__(self, jobs):
        super().__init__(jobs)

    def _handle_job(self, job):
        return Event(job.scraper, f"handled job {job}", True)

    def _validate_job_data_dict(self, job_data_dict: dict) -> bool:
        return bool(job_data_dict.get('appointment_from') and job_data_dict.get('appointment_to'))

