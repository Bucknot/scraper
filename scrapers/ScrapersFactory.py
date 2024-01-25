from scrapers.MaccabiScraper import MaccabiScraper

scrapers_by_name = {'maccabi': MaccabiScraper}
class ScrapersFactory:
    def create_scrapers(self, jobs):
        scrapers = {}
        for job in jobs:
            if job.scraper.lower() not in scrapers:
                scrapers[job.scraper] = []
            scrapers[job.scraper].append(job)
        return [scrapers_by_name[scraper_name](jobs) for scraper_name, jobs in scrapers.items()]


