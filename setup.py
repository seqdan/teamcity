# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

# TODO list
"""
Code
- Рефакторинг моделей - чтобы был единый Шаблон для моделей
- Рефакторинг API - аналогично, должен быть единый общий родитель
- Продумать как сделать так, чтобы можно было получать teamcity.agents.get() - и обращение сразу шло к API
- Наполнение информации про agent.pool.agents
- Добавление билд-степов напрямую к конфигурации? teamcity.build_types.get(ID).steps.add()?

- Retry как 502 ошибку - как сейчас в teamcity

Docs
- Ревью автогенерируемой документации
- Документация по тому что где находится, как сгенерировать документацию

"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "dohq-teamcity"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="TeamCity REST API",
    author_email="",
    url="https://github.com/devopshq/teamcity",
    keywords=["Swagger", "TeamCity REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501
    """
)
