from django.shortcuts import render
from .forms import PreditctForm
import pickle
from .service import getRandomRecord

filename = 'Final_LOANSTATUS_XGBOOST_NN_withStatewith_withZipCode.pkl'
ML_MODEL = pickle.load(open(filename, 'rb'))

scaler = pickle.load(open('Final_Scaler.pkl', 'rb'))


def check(request):
    context = {}
    if request.method == 'POST':
        import pandas as pd
        d = request.POST.dict()
        del d['csrfmiddlewaretoken']
        df = pd.DataFrame(d, index=[0])
        original_loan_status = df['loan_status'][0]
        if original_loan_status == 'Fully Paid':
            original_value = 0
        else:
            original_value = 1
        df.drop('loan_status', axis=1, inplace=True)
        df['term'] = df['term'].replace({' 36 months': 0, ' 60 months': 1})
        df['initial_list_status'] = df['initial_list_status'].replace({'w': 0, 'f': 1})
        emp_length_map = {'< 1 year': 0,
                          '1 year': 1,
                          '2 years': 2,
                          '3 years': 3,
                          '4 years': 4,
                          '5 years': 5,
                          '6 years': 6,
                          '7 years': 7,
                          '8 years': 8,
                          '9 years': 9,
                          '10+ years': 10}
        df['emp_length'] = df['emp_length'].map(emp_length_map)
        month_map = {'Jan': 0,
                     'Feb': 1,
                     'Mar': 2,
                     'Apr': 3,
                     'May': 4,
                     'Jun': 5,
                     'Jul': 6,
                     'Aug': 7,
                     'Sep': 8,
                     'Oct': 9,
                     'Nov': 10,
                     'Dec': 11}
        df['issue_d_month'] = df['issue_d_month'].map(month_map)
        df['earliest_cr_line_month'] = df['earliest_cr_line_month'].map(month_map)
        df.drop('home_ownership', axis=1, inplace=True)
        # One hot columns
        df.loc[0, 'MORTGAGE'] = 0
        df.loc[0, 'NONE'] = 0
        df.loc[0, 'OTHER'] = 0
        df.loc[0, 'RENT'] = 0
        if d['home_ownership'] == 'MORTGAGE':
            df.loc[0, 'MORTGAGE'] = 1
        if d['home_ownership'] == 'NONE':
            df.loc[0, 'NONE'] = 1
        if d['home_ownership'] == 'OTHER':
            df.loc[0, 'OTHER'] = 1
        if d['home_ownership'] == 'RENT':
            df.loc[0, 'RENT'] = 1

        df.drop('verification_status', axis=1, inplace=True)
        df.loc[0, 'Source Verified'] = 0
        df.loc[0, 'Not Verified'] = 0
        if d['verification_status'] == 'Source Verified':
            df.loc[0, 'Source Verified'] = 1
        if d['verification_status'] == 'Not Verified':
            df.loc[0, 'Not Verified'] = 1

        df.drop('application_type', axis=1, inplace=True)
        df.loc[0, 'DIRECT_PAY'] = 0
        df.loc[0, 'JOINT'] = 0
        if d['application_type'] == 'DIRECT_PAY':
            df.loc[0, 'DIRECT_PAY'] = 1
        if d['application_type'] == 'JOINT':
            df.loc[0, 'JOINT'] = 1

            # Assuming you have a DataFrame named df and a dictionary named d
        state = 'state'
        state_values = ['AP', 'AR', 'AZ', 'CA', 'CO', 'DC', 'DE', 'FL', 'GA', 'IN', 'MD', 'MN', 'MO', 'MS', 'MT',
                        'NC', 'NJ', 'NY', 'OK', 'OR', 'PA', 'TN', 'TX', 'UT', 'VT', 'WI', 'WV', 'WY']

        # Drop 'application_type' column from DataFrame
        df.drop(state, axis=1, inplace=True)

        # Create new columns for each state and set initial values to 0
        for state_value in state_values:
            df.loc[0, state_value] = 0
        if d[state] in state_values:
            df.loc[0, d[state]] = 1

        postal_values = ['00813', '05113', '11650', '22690', '29597', '48052', '86630', '93700']
        # Drop 'application_type' column from DataFrame
        df.drop('postal_code', axis=1, inplace=True)
        for postal_value in postal_values:
            df.loc[0, postal_value] = 0
        if d['postal_code'] in postal_values:
            df.loc[0, d['postal_code']] = 1

        purpose_values = ['car', 'credit_card', 'educational', 'home_improvement', 'house', 'major_purchase',
                          'medical', 'moving', 'other', 'renewable_energy', 'small_business', 'wedding']
        # Drop 'application_type' column from DataFrame
        df.drop('purpose', axis=1, inplace=True)
        for purpose_value in purpose_values:
            df.loc[0, purpose_value] = 0
        if d['purpose'] in purpose_values:
            df.loc[0, d['purpose']] = 1

        # row_index = 0  # Index of the row you want to print
        # row = df.iloc[row_index]
        # for column_name, value in row.iteritems():
        #     print(f"{column_name}: {value}")

        # scale the df

        # row_index = 0
        # row = df_scaled.iloc[row_index]
        # for column_name, value in row.iteritems():
        #     print(f"{column_name}: {value}")

        expected_feature_names = ['loan_amnt', 'term', 'int_rate', 'installment', 'emp_length',
                                  'annual_inc', 'dti', 'open_acc', 'pub_rec', 'revol_bal', 'revol_util',
                                  'total_acc', 'initial_list_status', 'mort_acc', 'pub_rec_bankruptcies',
                                  'mort_acc_missing', 'emp_length_missing', 'issue_d_month',
                                  'issue_d_year', 'earliest_cr_line_month', 'MORTGAGE', 'NONE', 'OTHER',
                                  'RENT', 'Not Verified', 'Source Verified', 'car', 'credit_card',
                                  'educational', 'home_improvement', 'house', 'major_purchase', 'medical',
                                  'moving', 'other', 'renewable_energy', 'small_business', 'wedding',
                                  'DIRECT_PAY', 'JOINT', 'AP', 'AR', 'AZ', 'CA', 'CO', 'DC', 'DE', 'FL',
                                  'GA', 'IN', 'MD', 'MN', 'MO', 'MS', 'MT', 'NC', 'NJ', 'NY', 'OK', 'OR',
                                  'PA', 'TN', 'TX', 'UT', 'VT', 'WI', 'WV', 'WY', '00813', '05113',
                                  '11650', '22690', '29597', '48052', '86630', '93700']

        df = df.reindex(columns=expected_feature_names)
        # scaler not working
        df_scaled = scaler.transform(df)
        df_scaled = pd.DataFrame(df_scaled, columns=df.columns)
        # row_index = 0
        # row = df_scaled.iloc[row_index]
        # for column_name, value in row.iteritems():
        #     print(f"{column_name}: {value}")
        prediction = ML_MODEL.predict(df_scaled)
        form = PreditctForm(initial=d)
        context['form'] = form
        boolean_prediction = prediction[0]
        context['original_class'] = original_loan_status
        context['boolean_prediction'] = boolean_prediction
    return render(request, 'predict/index.html', context)


def index(request):
    context = {}
    record = getRandomRecord()
    form = PreditctForm(record)
    # print(record)
    context['boolean_prediction'] = 3
    context['form'] = form
    return render(request, 'predict/index.html', context)
