from django import forms

class PreditctForm(forms.Form):
    loan_amount = forms.IntegerField(max_length=100)
    term = forms.IntegerField(max_length = 100)
    int_rate = forms.FloatField(max_length = 200)
    installment = forms.FloatField(max_length = 200)
    emp_title = forms.CharField()
    home_ownership = forms.CharField()
    annual_inc = forms.FloatField(max_length = 200)
    verification_status = forms.BooleanField()
    purpose = forms.CharField()
    dti =forms.FloatField(max_length=200)
    #drop
    pub_rec = forms.IntegerField(max_length = 100)
    revol_bal = forms.FloatField(max_length = 200)
    #drop
    total_acc = forms.FloatField(max_length = 200)
    initial_list_status	= forms.IntegerField(max_length = 100)
    application_type = forms.CharField()
    pub_rec_bankruptcies = forms.IntegerField(max_length = 100)
    address = forms.CharField()
    issue_d_month = forms.CharField()
    issue_d_year = forms.CharField()
    earliest_cr_line_month = forms.CharField()
    earliest_cr_line_year = forms.CharField()

