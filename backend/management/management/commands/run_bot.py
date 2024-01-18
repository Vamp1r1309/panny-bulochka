import asyncio
import logging
import sys

from django.core.management.base import BaseCommand
from django.conf import settings
from bot.main_bot import start


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Запуск бота"

    def handle(self, *args, **option):
        try:
            logging.basicConfig(level=settings.LOG_LEVEL, stream=sys.stdout)
            asyncio.run(start())
        except Exception as err:
            logger.error(f'Ошибка: {err}')

