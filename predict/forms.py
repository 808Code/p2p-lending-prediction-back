from django import forms

MONTHS_CHOICES = [
    ('Jan', 'Jan'),
    ('Feb', 'Feb'),
    ('Mar', 'Mar'),
    ('Apr', 'Apr'),
    ('May', 'May'),
    ('Jun', 'Jun'),
    ('Jul', 'Jul'),
    ('Aug', 'Aug'),
    ('Sep', 'Sep'),
    ('Oct', 'Oct'),
    ('Nov', 'Nov'),
    ('Dec', 'Dec'),
]

TERM_CHOICES = [
    (' 36 months', ' 36 Months'),
    (' 60 months', ' 60 Months')
]

EMP_LENGTH_CHOICES = [
    ('< 1 year', '< 1 year'),
    ('1 year', '1 year'),
    ('2 years', '2 years'),
    ('3 years', '3 years'),
    ('4 years', '4 years'),
    ('5 years', '5 years'),
    ('6 years', '6 years'),
    ('7 years', '7 years'),
    ('8 years', '8 years'),
    ('9 years', '9 years'),
    ('10+ years', '10+ years'),
]

HOME_OWNERSHIP_CHOICES = [
    ('RENT', 'RENT'),
    ('MORTGAGE', 'MORTGAGE'),
    ('OWN', 'OWN'),
    ('OTHER', 'OTHER'),
    ('ANY', 'ANY'),
    ('NONE', 'NONE'),
]

VERIFICATION_CHOICES = [
    ('Not Verified', 'Not Verified'),
    ('Source Verified', 'Source Verified'),
    ('Verified', 'Verified'),
]
LOAN_STATUS_CHOICES = [
    ('Fully Paid', 'Fully Paid'),
    ('Charged Off', 'Charged Off'),
]
INITIAL_LIST_CHOICES = [('w', 'w'), ('f', 'f'), ]
EMP_LENGTH_MISSING_CHOICES = [(0, 'Not Missing'), (1, 'Missing'), ]
MORT_ACC_MISSING_CHOICES = [(0, 'Not Missing'), (1, 'Missing'), ]
APPLICATION_TYPE_CHOICES = [
    ('INDIVIDUAL', 'Individual'),
    ('JOINT', 'Joint'),
    ('DIRECT_PAY', 'Direct Pay'),
]

PURPOSE_CHOICES = [
    ('vacation', 'vacation'),
    ('debt_consolidation', 'debt_consolidation'),
    ('credit_card', 'credit_card'),
    ('home_improvement', 'home_improvement'),
    ('small_business', 'small_business'),
    ('major_purchase', 'major_purchase'),
    ('other', 'other'),
    ('medical', 'medical'),
    ('wedding', 'wedding'),
    ('car', 'car'),
    ('moving', 'moving'),
    ('house', 'house'),
    ('educational', 'educational'),
    ('renewable_energy', 'renewable_energy'),
]

STATE_CHOICES = [
    ('OK', 'OK'),
    ('SD', 'SD'),
    ('WV', 'WV'),
    ('MA', 'MA'),
    ('VA', 'VA'),
    ('DE', 'DE'),
    ('TX', 'TX'),
    ('AE', 'AE'),
    ('AP', 'AP'),
    ('NM', 'NM'),
    ('MS', 'MS'),
    ('OR', 'OR'),
    ('NH', 'NH'),
    ('HI', 'HI'),
    ('PA', 'PA'),
    ('CO', 'CO'),
    ('AL', 'AL'),
    ('FL', 'FL'),
    ('AZ', 'AZ'),
    ('WI', 'WI'),
    ('NC', 'NC'),
    ('IN', 'IN'),
    ('MO', 'MO'),
    ('AA', 'AA'),
    ('TN', 'TN'),
    ('KS', 'KS'),
    ('ND', 'ND'),
    ('CT', 'CT'),
    ('WY', 'WY'),
    ('NE', 'NE'),
    ('RI', 'RI'),
    ('AR', 'AR'),
    ('MI', 'MI'),
    ('IL', 'IL'),
    ('LA', 'LA'),
    ('NY', 'NY'),
    ('IA', 'IA'),
    ('AK', 'AK'),
    ('UT', 'UT'),
    ('MD', 'MD'),
    ('WA', 'WA'),
    ('MN', 'MN'),
    ('OH', 'OH'),
    ('MT', 'MT'),
    ('NJ', 'NJ'),
    ('DC', 'DC'),
    ('NV', 'NV'),
    ('VT', 'VT'),
    ('CA', 'CA'),
    ('ME', 'ME'),
    ('ID', 'ID'),
    ('GA', 'GA'),
    ('KY', 'KY'),
    ('SC', 'SC'),
]
POSTAL_CHOICES = [
    ('22690', '22690'),
    ('05113', '05113'),
    ('00813', '00813'),
    ('11650', '11650'),
    ('30723', '30723'),
    ('70466', '70466'),
    ('29597', '29597'),
    ('48052', '48052'),
    ('86630', '86630'),
    ('93700', '93700'),
]


class PreditctForm(forms.Form):
    loan_amnt = forms.IntegerField(min_value=0)
    term = forms.ChoiceField(choices=TERM_CHOICES)
    int_rate = forms.FloatField(min_value=0)
    installment = forms.FloatField(min_value=0)
    emp_length = forms.ChoiceField(choices=EMP_LENGTH_CHOICES)
    home_ownership = forms.ChoiceField(choices=HOME_OWNERSHIP_CHOICES)
    annual_inc = forms.FloatField(min_value=0)
    verification_status = forms.ChoiceField(choices=VERIFICATION_CHOICES)
    loan_status = forms.ChoiceField(choices=LOAN_STATUS_CHOICES)
    purpose = forms.ChoiceField(choices=PURPOSE_CHOICES)
    dti = forms.FloatField(min_value=0)
    open_acc = forms.FloatField(label='Total Loans Recieved not yet utilized', min_value=0)
    pub_rec = forms.IntegerField(min_value=0)
    revol_bal = forms.FloatField(min_value=0)
    revol_util = forms.FloatField(min_value=0)
    mort_acc = forms.FloatField(label='Total Mortages Recieved', min_value=0)
    total_acc = forms.FloatField(label='Total Loans/Mortages/Credit Recieved', min_value=0)
    initial_list_status = forms.ChoiceField(choices=INITIAL_LIST_CHOICES)
    application_type = forms.ChoiceField(choices=APPLICATION_TYPE_CHOICES)
    pub_rec_bankruptcies = forms.IntegerField(min_value=0)
    state = forms.ChoiceField(choices=STATE_CHOICES)
    postal_code = forms.ChoiceField(choices=POSTAL_CHOICES)
    mort_acc_missing = forms.ChoiceField(choices=MORT_ACC_MISSING_CHOICES)
    emp_length_missing = forms.ChoiceField(choices=EMP_LENGTH_MISSING_CHOICES)
    issue_d_month = forms.ChoiceField(choices=MONTHS_CHOICES)
    issue_d_year = forms.IntegerField(min_value=1900, max_value=2022)
    earliest_cr_line_month = forms.ChoiceField(choices=MONTHS_CHOICES)
    #Throw last
    #earliest_cr_line_year = forms.IntegerField(min_value=1900, max_value=2022)
