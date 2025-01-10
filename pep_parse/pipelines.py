import csv
from datetime import datetime

from .settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = {}
        self.total_count = 0

    def process_item(self, item, spider):
        status = item['status']
        self.counter[status] = self.counter.get(status, 0) + 1
        self.total_count += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_path = results_dir / datetime.now().strftime(
            'status_summary_%Y-%m-%d-%H-%M.csv'
        )
        results_list = [['Статус,Количество']] + [
            [f'{key},{self.counter[key]}'] for key in self.counter
        ] + [[f'Total,{self.total_count}']]
        with open(file_path, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(results_list)
