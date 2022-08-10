from django import forms


class PreditctForm(forms.Form):
    loan_amount = forms.IntegerField()
    term = forms.IntegerField()
    int_rate = forms.FloatField()
    installment = forms.FloatField()
    emp_title = forms.CharField()
    home_ownership = forms.CharField()
    annual_inc = forms.FloatField()
    verification_status = forms.BooleanField()
    purpose = forms.CharField()
    dti = forms.FloatField()
    # drop
    pub_rec = forms.IntegerField()
    revol_bal = forms.FloatField()
    # drop
    total_acc = forms.FloatField()
    initial_list_status = forms.IntegerField()
    application_type = forms.CharField()
    pub_rec_bankruptcies = forms.IntegerField()
    address = forms.CharField()
    issue_d_month = forms.CharField()
    issue_d_year = forms.CharField()
    earliest_cr_line_month = forms.CharField()
    earliest_cr_line_year = forms.CharField()
