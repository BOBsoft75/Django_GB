from django.shortcuts import render
import logging
from django.http import HttpResponse


logger = logging.getLogger(__name__)

headers = {'Cache-Control': 'no-cache, must-revalidate',
           'Pragma': 'no-cache'}


def main(request):  
    body = """
    <h1>Главная страница</h1>
    <p>Содержимое главной страницы</p>
    """
    logger.info(f'Страница открыта')
    return HttpResponse(body, charset="utf-8", headers=headers)


def about_me(request):  
    body = """
        <h1>О себе</h1>
        <p>Содержимое страницы о себе</p>
        """
    logger.info(f'Страница открыта')
    return HttpResponse(body, charset="utf-8", headers=headers)
