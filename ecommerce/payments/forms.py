from django import forms


class AddressForm(forms.Form):
    address1 = forms.CharField(max_length=255)
    address2 = forms.CharField(max_length=255)
    town_city = forms.CharField(max_length=255)
    postcode = forms.CharField(max_length=20)
    post_office_name = forms.CharField(label='Enter post office number and it`s name', max_length=40)

    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
