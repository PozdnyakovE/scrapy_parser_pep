from pathlib import Path

PEP_PARSER_NAME = 'pep'
PEP_ALLOWED_DOMAINS = ['peps.python.org']
PEP_START_URLS = ['https://peps.python.org/']

BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
BASE_DIR = Path(__file__).parent.parent
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
