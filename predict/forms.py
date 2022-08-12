from django import forms

VERIFICATION_CHOICES= [
    (0, 'Not Verified'),
    (1,'Verified'),
    (2,'Source Verified'),
    ]

MONTHS_MAPPING = {1: 'Jan',
 2: 'Feb',
 3: 'Mar',
 4: 'Apr',
 5: 'May',
 6: 'Jun',
 7: 'Jul',
 8: 'Aug',
 9: 'Sep',
 10: 'Oct',
 11: 'Nov',
 12: 'Dec'}

INTIAL_LIST_STATUS = [(1,'Whole'),(0,'Fractional')]
HOME_OWNERSHIP = [(0,'RENT') , (1,'OWN') ,(3,'MORTGAGE')]
APPLICATION_TYPE = [(0,'JOINT') , (1,'INDIVIDUAL')]

class PreditctForm(forms.Form):
    loan_amnt = forms.IntegerField(min_value=0)
    term = forms.IntegerField(min_value=0)
    int_rate = forms.FloatField(min_value=0)
    installment = forms.FloatField(min_value=0)
    emp_title = forms.IntegerField()
    emp_length = forms.IntegerField()
    home_ownership = forms.IntegerField(widget=forms.Select(choices=HOME_OWNERSHIP))
    annual_inc = forms.FloatField(min_value=0)
    verification_status = forms.IntegerField(widget=forms.Select(choices=VERIFICATION_CHOICES))
    loan_status=forms.IntegerField()
    purpose = forms.IntegerField()
    dti = forms.FloatField(min_value=0)
    # drop
    pub_rec = forms.IntegerField(min_value=0)
    revol_bal = forms.FloatField(min_value=0)
    # drop
    total_acc = forms.FloatField(label='Total Loans Recieved',min_value=0)
    initial_list_status = forms.IntegerField(widget=forms.Select(choices=INTIAL_LIST_STATUS))
    application_type = forms.IntegerField(widget=forms.Select(choices=APPLICATION_TYPE))
    pub_rec_bankruptcies = forms.IntegerField(min_value=0)
    address = forms.IntegerField(min_value=0)
    issue_d_month = forms.CharField(widget=forms.Select(choices=MONTHS_MAPPING.items()))
    issue_d_year = forms.IntegerField(min_value=1900,max_value=2022)
    earliest_cr_line_month = forms.IntegerField(widget=forms.Select(choices=MONTHS_MAPPING.items()))
    earliest_cr_line_year = forms.IntegerField(min_value=1900,max_value=2022)
