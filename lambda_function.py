import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))

import json
from concurrent.futures import ThreadPoolExecutor

from publishers.PushOverPublisher import PushOverPublisher
from publishers.TrelloPublisher import TrelloPublisher
from jobs.Job import Job
from scrapers.ScrapersFactory import ScrapersFactory

def scrape_and_publish(scraper, events, publisher):
    try:
        for event in events:
            publisher.publish(event)
    except Exception as e:
        print(f'Error processing {scraper} and {publisher}: {e}')

def lambda_handler(event, context):
    try:
        jobs_dicts = json.loads(os.environ.get("JOBS"))
    except Exception as e:
        raise Exception(f'invalid jobs json - {e}')

    jobs = [Job(job_dict) for job_dict in jobs_dicts]
    scrapers_factory = ScrapersFactory()
    scrapers = scrapers_factory.create_scrapers(jobs)
    event_publishers = [PushOverPublisher, TrelloPublisher]

    with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers as needed
        for scraper in scrapers:
            events = scraper.scrape()
            for event_publisher in event_publishers:
                publisher = event_publisher(os.environ)
                executor.submit(scrape_and_publish, scraper, events, publisher)

