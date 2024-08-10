import datetime as dt
import time
import re
from enum import Enum
from typing import Optional

import bs4
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from .models import (IncomeTaxReturn, HousingTaxNotice,
                     PropertyTaxNotice, IncomeTaxNotice, AdvanceInformation,
                     AutomaticInformation, InstantIncomeTaxNotice, HousingTaxPaymentSchedule,
                     PropertyTaxPaymentSchedule, IncomeTaxReturnReceiptConfirmation, SupplementaryIncomeTaxNotice,
                     WealthTaxNotice, RealEstateWealthTaxNotice, SupplementaryRealEstateWealthTaxNotice,
                     PublicBroadcastingContributionRebateNotice, RealEstateWealthTaxReturn, UnknownDocument)


def login_required(function):
    def wrapper(self, *args, **kwargs):
        if not self.is_connected:
            self.login()
        return function(self, *args, **kwargs)

    return wrapper


class ImpotsGouvConnexionError(Enum):
    UNKNOWN_ERROR = 0
    UNKNOWN_LOGIN_ERROR = 1
    UNKNOWN_FISCAL_NUMBER = 2
    WRONG_PASSWORD = 3


class ImpotsGouvData:
    REQUEST_DELAY = 1

    URLS = {
        'home': 'https://cfspart.impots.gouv.fr/',
        'root_documents': 'https://cfspart.impots.gouv.fr/enp/',
        'root_documents_display': 'https://cfspart.impots.gouv.fr/enp/Affichage_Document_PDF?idEnsua='
    }

    USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
    HEADERS = {"User-Agent": USER_AGENT}

    def __init__(self, fiscal_number, password):
        self.fiscal_number = fiscal_number
        self.password = password

        self._session = self._init_session()
        self._last_request: Optional[dt.datetime] = None
        self.page = None

        self._last_name: Optional[str] = None
        self._first_name: Optional[str] = None
        self._birth_date: Optional[dt.date] = None

    @staticmethod
    def _init_session():

        session = requests.Session()

        retry_strategy = Retry(
            total=5,
            redirect=5,
            backoff_factor=0.5,
        )

        session.mount("https://", HTTPAdapter(max_retries=retry_strategy))

        return session

    @property
    def is_connected(self):

        connected = False

        if self.page is not None:

            home = self.get(self.URLS['home'])
            bs = BeautifulSoup(home.text, 'lxml')

            if bs.select_one('#numfiscal') is not None:
                regex = re.search(r'[0-9]{13}', bs.select_one('#numfiscal').text)

                if regex is not None and regex[0] == str(self.fiscal_number):
                    connected = True

        return connected

    def _sleep(self, request_delay=None):
        delay = 0
        request_delay = self.REQUEST_DELAY if request_delay is None else request_delay

        if self._last_request is not None:
            time_limit = self._last_request + dt.timedelta(seconds=request_delay)
            delay = max((0, (time_limit - dt.datetime.now()).total_seconds()))

        time.sleep(delay)

        self._last_request = dt.datetime.now()

    def get(self, url, request_delay=None, **kwargs):
        self._sleep(request_delay=request_delay)
        self.page = self._session.get(url=url, headers=self.HEADERS, **kwargs)
        return self.page

    def post(self, url, data, request_delay=None, *args, **kwargs):
        self._sleep(request_delay=request_delay)
        self.page = self._session.post(url=url, data=data, headers=self.HEADERS, *args, **kwargs)
        return self.page

    @staticmethod
    def inspect(html_element):
        return bs4.BeautifulSoup(html_element, 'lxml')

    @staticmethod
    def date_from_text(text):
        day, month, year = re.search(r"(\d{1,2}) (.*) (\d{4})", text).groups()
        day = int(day)
        month = {"janvier": 1, "février": 2, "mars": 3, "avril": 4,
                 "mai": 5, "juin": 6, "juillet": 7, "août": 8,
                 "septembre": 9, "octobre": 10, "novembre": 11, "décembre": 12,
                 }.get(month)
        year = int(year)
        return dt.date(year=year, month=month, day=day)

    def login(self):

        if not self.is_connected:
            self.get('https://cfspart.impots.gouv.fr')

            # Override default sleep
            r = self.post(url='https://cfspart-idp.impots.gouv.fr/GetContexte',
                          data={
                              'url': '',
                              'lmAuth': '',
                              'spi': self.fiscal_number,
                          },
                          )

            value = re.search(r"parent.postMessage\('ctx,(.*)'.*\)", r.text)

            if value.group(1) == 'EXISTEPAS':
                raise ConnectionError(ImpotsGouvConnexionError.UNKNOWN_FISCAL_NUMBER)

            elif value.group(1) != 'LMDP':
                raise ConnectionError(ImpotsGouvConnexionError.UNKNOWN_LOGIN_ERROR)

            r = self.post(url='https://cfspart-idp.impots.gouv.fr/',
                          data={
                              'url': '',
                              'lmAuth': 'LDAP',
                              'authType': '',
                              'spi': self.fiscal_number,
                              'pwd': self.password,
                              'fg': '',
                          },
                          )

            value = re.search(r"parent.postMessage\('(.*)',", r.text)

            status = value.group(1)

            if regex := re.search(r"lmdp,4005:(\d)", status):
                raise ConnectionError(ImpotsGouvConnexionError.WRONG_PASSWORD, int(regex.group(1)))

            elif not re.search(r"ok,(.*)", status):
                raise ConnectionError(ImpotsGouvConnexionError.UNKNOWN_ERROR, status)

            else:
                url = status.removeprefix("ok,")
                self.get(url=url)

    def logout(self):
        self.get("https://cfspart.impots.gouv.fr/enp/j_spring_security_logout.ex")
        self._session = self._init_session()

    @login_required
    def fetch_civil_data(self):
        page = self.get('https://cfspart.impots.gouv.fr/enp/chargementprofil.do')
        soup = self.inspect(page.text)

        self._last_name = soup.select_one('#nom').text.title()
        self._first_name = soup.select_one('#prenom').text.title()
        self._birth_date = self.date_from_text(soup.select_one('#datenaissance').text)

    @property
    def last_name(self):
        if self._last_name is None:
            self.fetch_civil_data()
        return self._last_name

    @property
    def first_name(self):
        if self._first_name is None:
            self.fetch_civil_data()
        return self._first_name

    @property
    def birth_date(self):
        if self._birth_date is None:
            self.fetch_civil_data()
        return self._birth_date

    @property
    @login_required
    def tax_data(self):
        return self.get('https://cfspart.impots.gouv.fr/enp/dpr.do')

    @login_required
    def iter_documents(self):

        r = self.get(url=f"{self.URLS['root_documents']}documents.do?n=0")

        soup = self.inspect(r.text)

        for href in (a['href'] for a in soup.select('.blocAnnee a')):
            r = self.get(url=(self.URLS['root_documents'] + href))
            doc_soup = self.inspect(r.text)

            year = int(re.search(r"(\d{4})", href).group(1))

            for document in doc_soup.select('.document, .document [id^="plierdocuments"] .document_lie'):
                title_elt = document.select_one('[id^="doc-item"]')
                title = title_elt.text
                ensua_id = document.select_one('form input[name="idEnsua"]').get('value')

                if not ensua_id:
                    continue

                url = f"{self.URLS['root_documents_display']}{ensua_id}"

                if m := re.search(r"Déclaration automatique : "
                                  r"vos informations connues de l'administration \(revenus (\d{4})\)", title):
                    tax_year = int(m.group(1))

                    doc = AutomaticInformation(title=title, ensua_id=ensua_id, url=url, year=year, tax_year=tax_year)

                elif m := re.search(r"^Accusé de réception n° (\d+) .*revenus (\d{4})", title):
                    tax_year = int(m.group(2))
                    identifier = m.group(1)

                    doc = IncomeTaxReturnReceiptConfirmation(title=title, ensua_id=ensua_id, url=url,
                                                             year=year, tax_year=tax_year, identifier=identifier)

                elif m := re.search(r"Déclaration.*(\d{4}).*fortune immobilière"
                                    r".*(\d{2}/\d{2}/\d{4})*.*(\d{2}:\d{2})*", title):
                    tax_year = int(m.group(1))

                    date = None
                    if m_date := re.search(r"(\d{2}/\d{2}/\d{4})", title):
                        day, month, year = m_date.group().split('/')
                        date = dt.date(year=int(year), month=int(month), day=int(day))

                    _time = None
                    if m_time := re.search(r"(\d{2}:\d{2})", title):
                        hour, minute = m_time.group().split(':')
                        _time = dt.time(hour=int(hour), minute=int(minute))

                    doc = RealEstateWealthTaxReturn(title=title, ensua_id=ensua_id, url=url, year=year,
                                                    tax_year=tax_year, date=date, time=_time)

                elif re.search(r"^Déclaration.*(\d{2}/\d{2}/\d{4})*.*(\d{2}:\d{2})*", title):

                    date = None
                    if m_date := re.search(r"(\d{2}/\d{2}/\d{4})", title):
                        day, month, year = m_date.group().split('/')
                        date = dt.date(year=int(year), month=int(month), day=int(day))

                    _time = None
                    if m_time := re.search(r"(\d{2}:\d{2})", title):
                        hour, minute = m_time.group().split(':')
                        _time = dt.time(hour=int(hour), minute=int(minute))

                    tax_year = None
                    form = None

                    if m := re.search(r"complémentaire.*des revenus (\d{4})", title):
                        tax_year = int(m.group(1))
                        form = "2042-C"

                    elif m := re.search(r"revenus (\d{4}).*encaissés.*étranger", title):
                        tax_year = int(m.group(1))
                        form = "2047"

                    elif m := re.search(r"revenus (\d{4}) : réductions et crédits", title):
                        tax_year = int(m.group(1))
                        form = "2042-RICI"

                    elif m := re.search(r"Déclaration.*des revenus (\d{4})", title):
                        tax_year = int(m.group(1))
                        form = "2042"

                    elif m := re.search(r"revenus fonciers (\d{4})", title):
                        tax_year = int(m.group(1))
                        form = "2044"

                    elif m := re.search(r"Déclaration.*(\d{4}).*plus ou moins-values", title):
                        tax_year = int(m.group(1)) - 1
                        form = "2074"

                    elif m := re.search(r"Déclaration.*(\d{4}).*plus-values en report", title):
                        tax_year = int(m.group(1)) - 1
                        form = "2074-I"

                    elif m := re.search(r"(\d{4}).*compensation.*moins-values.*suivi", title):
                        tax_year = int(m.group(1)) - 1
                        form = "2041-SP"

                    elif m := re.search(r"(\d{4}).*résident.*compte bancaire.*étranger", title):
                        tax_year = int(m.group(1)) - 1
                        form = "3916"

                    doc = IncomeTaxReturn(title=title, ensua_id=ensua_id, url=url, year=year,
                                          tax_year=tax_year, date=date, time=_time, form=form,
                                          )

                elif m := re.search(r"Impôt sur les revenus (\d{4})"
                                    r" – Montant de l’avance de réductions et crédits d’impôt", title):
                    tax_year = int(m.group(1))

                    doc = AdvanceInformation(title=title, ensua_id=ensua_id, url=url, year=year, tax_year=tax_year)

                elif m := re.search(r"Avis d'impôt (\d{4}) sur les revenus .*(\d{4})", title):
                    tax_year = int(m.group(2))

                    doc = IncomeTaxNotice(title=title, ensua_id=ensua_id, url=url, year=year, tax_year=tax_year)

                elif m := re.search(r"Avis supplémentaire d'impôt (\d{4}) sur les revenus .*(\d{4})", title):
                    tax_year = int(m.group(2))

                    doc = SupplementaryIncomeTaxNotice(title=title, ensua_id=ensua_id, url=url,
                                                       year=year, tax_year=tax_year)

                elif m := re.search(r"Avis de situation déclarative à l'impôt (\d{4}) sur les revenus (\d{4}) "
                                    r"\(.*(\d{2}/\d{2}/\d{4}).*(\d{2}:\d{2}).*\)", title):
                    tax_year = int(m.group(2))

                    date = None
                    if m_date := re.search(r"(\d{2}/\d{2}/\d{4})", title):
                        day, month, year = m_date.group().split('/')
                        date = dt.date(year=int(year), month=int(month), day=int(day))

                    _time = None
                    if m_time := re.search(r"(\d{2}:\d{2})", title):
                        hour, minute = m_time.group().split(':')
                        _time = dt.time(hour=int(hour), minute=int(minute))

                    doc = InstantIncomeTaxNotice(title=title, ensua_id=ensua_id, url=url, year=year,
                                                 tax_year=tax_year, date=date, time=_time)

                elif m := re.search(r"Avis impôt sur la fortune (\d{4})", title):
                    tax_year = int(m.group(1))

                    doc = WealthTaxNotice(title=title, ensua_id=ensua_id, url=url, year=year, tax_year=tax_year)

                elif m := re.search(r"Avis impôt sur la fortune immobilière (\d{4})", title):
                    tax_year = int(m.group(1))

                    doc = RealEstateWealthTaxNotice(title=title, ensua_id=ensua_id, url=url,
                                                    year=year, tax_year=tax_year)

                elif m := re.search(r"Avis supplémentaire impôt sur la fortune immobilière (\d{4})", title):
                    tax_year = int(m.group(1))

                    doc = SupplementaryRealEstateWealthTaxNotice(title=title, ensua_id=ensua_id, url=url,
                                                                 year=year, tax_year=tax_year)

                elif m := re.search(r"taxe.*habitation.*(\d{4}).*<br/>(.*)", title_elt.decode_contents()):
                    tax_year = int(m.group(1))
                    address = m.group(2)

                    doc = HousingTaxNotice(title=title, ensua_id=ensua_id, url=url, year=year,
                                           tax_year=tax_year, address=address)

                elif m := re.search(r"Avis de taxes foncières (\d{4}).*<br/>(.*)", title_elt.decode_contents()):
                    tax_year = int(m.group(1))
                    address = m.group(2)

                    doc = PropertyTaxNotice(title=title, ensua_id=ensua_id, url=url, year=year,
                                            tax_year=tax_year, address=address)

                elif m := re.search(r"Avis dégrèvement contribution audiovisuelle (\d{4})", title):
                    tax_year = int(m.group(1))

                    doc = PublicBroadcastingContributionRebateNotice(title=title, ensua_id=ensua_id,
                                                                     url=url, year=year,
                                                                     tax_year=tax_year,
                                                                     )

                elif re.search(r"Echéancier.*(\d{4}).*habitation", title):
                    doc = HousingTaxPaymentSchedule(title=title, ensua_id=ensua_id, url=url, year=year, tax_year=year)

                elif re.search(r"Echéancier.*(\d{4}).*foncière", title):
                    doc = PropertyTaxPaymentSchedule(title=title, ensua_id=ensua_id, url=url, year=year, tax_year=year)

                else:
                    doc = UnknownDocument(title=title, ensua_id=ensua_id, url=url, year=year)

                yield doc
