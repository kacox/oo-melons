"""Classes for melon orders."""

from random import randint


class AbstractMelonOrder(object):
    """ An abstract base class that other Melon Orders inherit from. """

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas melon":
            base_price = self.get_base_price() * 1.5
        else:
            base_price = self.get_base_price()
        
        total = (1 + self.tax) * self.qty * base_price

        if self.country_code != "USA" and self.qty < 10:
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_base_price(self):
        """ Determine base price based on 'Splurge Pricing' """
        return randint(5, 9)


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    country_code = "USA"
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """ A melon order by the USA government."""

    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True
