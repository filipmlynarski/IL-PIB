from django.forms import ModelForm

from .models import Enterprise


class EnterpriseForm(ModelForm):
    # Missing docstring explaining form's purpose
    # Missing fields declaration - should explicitly declare which fields to include

    class Meta:
        model = Enterprise
        # Missing 'fields' attribute - required for ModelForm
        # Should specify which fields to include/exclude

    def clean_nip(self):
        # Missing docstring explaining validation logic
        nip_str = self.cleaned_data.get("nip")
        try:
            nip_str = nip_str.replace("-", "")
            if len(nip_str) != 10 or not nip_str.isdigit():
                return False  # Should raise ValidationError instead of returning False
            digits = [int(i) for i in nip_str]
            weights = (6, 5, 7, 2, 3, 4, 5, 6, 7)
            check_sum = sum(d * w for d, w in zip(digits, weights)) % 11
        except KeyError:  # Wrong exception - should be catching ValueError or TypeError
            return False  # Should raise ValidationError instead of returning False
        return check_sum == digits[9]  # Should return cleaned value, not boolean
