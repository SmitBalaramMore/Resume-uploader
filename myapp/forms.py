from .models import resumedata
from django import forms

GENDER_CHOICE=[
    ("MALE","MALE"),
    ("FEMALE","FEMALE")
]
PREFERRED_CITY=[
    ('PUNE','PUNE'),
    ('MUMBAI','MUMBAI'),
    ('BANGLORE','BANGLORE'),
    ('THANE','THANE'),
    ('VASHI','VASHI'),
    ('NAVI MUMBAI','NAVI MUMBAI')
    ,('KALYAN','KALYAN')
]

class formsdata(forms.ModelForm):
    genders = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    date = forms.DateField(
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )

   
    job_city = forms.MultipleChoiceField(choices=PREFERRED_CITY, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = resumedata
        fields = ['name','skills', 'date', 'genders', 'locality', 'city', 'pin', 'state', 'mobile', 'email',
                  'job_city', 'profile', 'my_file']
        labels = {'name': 'FULL NAME', 'date': 'DATE OF BIRTH', 'locality': 'LOCALITY', 'city': 'CITY', 'pin': 'PINCODE',
                  'state': 'STATE', 'mobile': 'PHONE NO', 'email': 'EMIAL ID', 'job_city': 'PREFERRED CITY',
                  'genders': 'GENDER', 'profile': 'PROFILE IMG', 'my_file': 'DOCUMENT'}
