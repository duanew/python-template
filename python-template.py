import logging
import sys
from settings.settings import Settings

logger = logging.getLogger(__name__)


class PythonTemplate:

    def __init__(self):
        self.settings = Settings()
        self.config = self.settings.load_config()
        self.settings.init_logging('python-template', prefix_date=True, stdout=True)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def main(self):
        logger.info("Starting a new run")


if __name__ == "__main__":
    python_template = PythonTemplate()
    python_template.main()
    sys.exit(0)
