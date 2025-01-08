from datetime import datetime

from .settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = {}
        self.total_count = 0

    def process_item(self, item, spider):
        status = item['status']
        if status not in self.counter:
            self.counter[status] = 0
        self.counter[status] += 1
        self.total_count += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_path = results_dir / datetime.now().strftime(
            'status_summary_%Y-%m-%d-%H-%M.csv'
        )
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key in self.counter:
                f.write(f'{key},{self.counter[key]}\n')
            f.write(f'Total,{self.total_count}\n')
