import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, ClassVar


@dataclass
class Document(ABC):

    NAME: ClassVar[str]

    title: str = ""
    ensua_id: str = ""
    url: str = ""
    year: int = 0

    label: str = field(init=False)

    def __post_init__(self):
        self.label = self._label()

    @abstractmethod
    def _label(self) -> str:
        pass


@dataclass
class BaseTax:
    tax_year: int = 0


@dataclass
class IncomeTax(BaseTax):
    pass


@dataclass
class WealthTax(BaseTax):
    pass


@dataclass
class RealEstateWealthTax(BaseTax):
    pass


@dataclass
class LocalTax(BaseTax):
    pass


@dataclass
class HousingTax(LocalTax):
    pass


@dataclass
class PropertyTax(LocalTax):
    pass


@dataclass
class PublicBroadcastingContribution(BaseTax):
    pass


@dataclass
class TaxReturn(Document, ABC):
    date: Optional[datetime.date] = datetime.date(year=1900, month=1, day=1)
    time: Optional[datetime.time] = datetime.time(hour=0, minute=0)


@dataclass
class TaxNotice(Document, ABC):
    pass


@dataclass
class TaxRebateNotice(TaxNotice, ABC):
    pass


@dataclass
class ReceiptConfirmation(Document, ABC):
    pass


@dataclass
class PaymentSchedule(Document, ABC):
    pass


@dataclass
class UnknownDocument(Document):

    NAME = "Document inconnu"

    def _label(self) -> str:
        return f"Document inconnu de l’année {self.year}"


@dataclass
class IncomeTaxReturn(IncomeTax, TaxReturn):
    form: str = ""

    NAME = "Déclaration de revenus"

    def _label(self) -> str:
        return f"Déclaration des revenus {self.tax_year} - Imprimé {self.form}"


@dataclass
class RealEstateWealthTaxReturn(RealEstateWealthTax, TaxReturn):

    NAME = "Déclaration d’impôt sur la fortune immobilière"

    def _label(self) -> str:
        return f"Déclaration d’impôt sur la fortune immobilière {self.tax_year}"


@dataclass
class IncomeTaxReturnReceiptConfirmation(IncomeTax, ReceiptConfirmation):
    identifier: str = ""

    NAME = "Accusé de réception de la déclaration de revenus"

    def _label(self) -> str:
        return f"Accusé de réception de la déclaration des revenus {self.tax_year}"


@dataclass
class AdvanceInformation(IncomeTax, Document):

    NAME = "Information sur l’avance reçue"

    def _label(self) -> str:
        return f"Information sur l’avance reçue au titre des revenus {self.tax_year}"


@dataclass
class AutomaticInformation(IncomeTax, Document):

    NAME = "Déclaration automatique des revenus"

    def _label(self) -> str:
        return f"Déclaration automatique des revenus {self.tax_year}"


@dataclass
class InstantIncomeTaxNotice(IncomeTax, TaxNotice):
    date: Optional[datetime.date] = datetime.date(year=1900, month=1, day=1)
    time: Optional[datetime.time] = datetime.time(hour=0, minute=0)

    NAME = "Avis de situation déclarative"

    def _label(self) -> str:
        return f"Avis de situation déclarative {self.year} au titre des revenus {self.tax_year}"


@dataclass
class IncomeTaxNotice(IncomeTax, TaxNotice):

    NAME = "Avis d’impôt sur le revenu"

    def _label(self) -> str:
        return f"Avis d’impôt {self.year} sur les revenus {self.tax_year}"


@dataclass
class SupplementaryIncomeTaxNotice(IncomeTax, TaxNotice):

    NAME = "Avis supplémentaire d’impôt sur le revenu"

    def _label(self) -> str:
        return f"Avis supplémentaire d’impôt {self.year} sur les revenus {self.tax_year}"


@dataclass
class WealthTaxNotice(WealthTax, TaxNotice):

    NAME = "Avis d’impôt de solidarité sur la fortune"

    def _label(self) -> str:
        return f"Avis d’impôt de solidarité sur la fortune {self.tax_year}"


@dataclass
class RealEstateWealthTaxNotice(RealEstateWealthTax, TaxNotice):

    NAME = "Avis d’impôt sur la fortune immobilière"

    def _label(self) -> str:
        return f"Avis d’impôt sur la fortune immobilière {self.tax_year}"


@dataclass
class SupplementaryRealEstateWealthTaxNotice(RealEstateWealthTax, TaxNotice):

    NAME = "Avis supplémentaire d’impôt sur la fortune immobilière"

    def _label(self) -> str:
        return f"Avis supplémentaire d’impôt sur la fortune immobilière {self.tax_year}"


@dataclass
class HousingTaxNotice(HousingTax, TaxNotice):
    address: str = ""

    NAME = "Avis de taxe d’habitation"

    def _label(self) -> str:
        return f"Avis de taxe d’habitation {self.tax_year}"


@dataclass
class PropertyTaxNotice(PropertyTax, TaxNotice):
    address: str = ""

    NAME = "Avis de taxe foncière"

    def _label(self) -> str:
        return f"Avis de taxe foncière {self.tax_year}"

@dataclass
class HousingTaxPaymentSchedule(HousingTax, PaymentSchedule):

    NAME = "Échéancier de paiement de la taxe d’habitation"

    def _label(self) -> str:
        return f"Échéancier {self.year} de paiement de la taxe d’habitation"


@dataclass
class PropertyTaxPaymentSchedule(PropertyTax, PaymentSchedule):

    NAME = "Échéancier de paiement de la taxe foncière"

    def _label(self) -> str:
        return f"Échéancier {self.year} de paiement de la taxe foncière"


@dataclass
class PublicBroadcastingContributionRebateNotice(PublicBroadcastingContribution, TaxRebateNotice):

    NAME = "Avis de dégrèvement sur la contribution à l’audiovisuel public"

    def _label(self) -> str:
        return f"Avis de dégrèvement sur la contribution à l’audiovisuel public {self.tax_year}"
