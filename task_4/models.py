from django.db import models


class Enterprise(models.Model):
    # CharField requires max_length parameter
    # Consider adding verbose_name for better admin interface
    name = models.CharField()

    # NIP (Polish Tax ID) should:
    # - Have validation for exactly 10 digits
    # - Probably not be nullable for a business entity
    # - Have unique=True constraint
    nip = models.CharField(max_length=10, blank=True, null=True)

    # max_length=10 is too short for real addresses
    # Consider using TextField() instead
    address = models.CharField(max_length=10, blank=True, null=True)

    # Consider adding help_text explaining the currency (PLN/EUR?)
    share_capital = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    # Consider adding help_text explaining the year format (4 digits?)
    # Add validation for the year
    established_year = models.IntegerField(blank=True)

    @property
    def short_name(self):
        """Return short name contains first letters of words from name"""
        # Missing error handling for None/empty name
        # Multiple spaces between words not handled
        # No maximum length validation
        return "".join(map(lambda x: x[0].capitalize(), self.name.split(" ")))

    def get_share_capital_in_euro(self):
        # Missing docstring
        # Hard-coded exchange rate is bad practice
        # No error handling for None values
        # Consider getting exchange rate from settings or external service
        euro_exchange_rate = 4
        return self.share_capital / euro_exchange_rate

    # Missing:
    # - __str__ method
    # - class Meta (ordering, verbose names)
    # - created_at/updated_at fields for auditing
    # - custom clean() method for model-wide validation
