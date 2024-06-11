import numpy as np
import pickle
import streamlit as st
import pandas as pd








#loading the saved model
loaded_model = pickle.load(open('C:/Users/Masterkim/projects/Loan prediction/trained_model.sav', 'rb'))


#create a function for prediction


def loan_pred(input_data):
    #changing the input data to numpy array

    input_array=np.asarray(input_data)

    #reshape

    input_array_reshape = input_array.reshape(1,-1)
    prediction= loaded_model.predict(input_array_reshape)
    print(prediction)

    
    if (prediction[0] == 0):
        print('The person is not eligibe for loan')
    else:
        print('The person is eligible for the loan')

def main():
    #giving a title
    st.title("Loan web app")
    st.write("Welcome to this loan web app")
    table = pd.DataFrame({'Terms':['Married', 'Not Married', 'Graduate', 'Not Graduate', 'Male', 'Female', 'Self Employed', 'working with a company'],
                           'Value to represent with': [1, 0, 0, 1, 1, 0, 1, 0]} )
    table_two = pd.DataFrame({'Term':['Bad Credit History', 'Good Credit History', 'Rural','urban','semiurban'],'Value to represent with': [0, 1,0, 2, 1] })
    st.dataframe(table)
    st.dataframe(table_two)

    #getting input data from users

    Gender = st.text_input('Gender of the applicant')
    Marriage_Status = st.text_input('Marriage Status')
    Dependents = st.text_input('Number of dependents')
    Education = st.text_input('Status of Education')
    Employed = st.text_input('Employment Status')
    ApplicantIncome = st.text_input('Applicant Salary in thousands')
    CoApplicantIncome = st.text_input('CoApplicant Salary in thousands')
    Loan_amount = st.text_input('Loan amount')
    Loan_amount_term = st.text_input('Loan amount term in months')
    Credit_history = st.text_input('Past credit reputation')
    property_area = st.text_input('Property area type')

 
    #code for prediction
    diagnosis = ' '
    
    #creating a button for prediction

    if st.button('Check result'):
        diagnosis = loan_pred([Gender, Marriage_Status, Dependents, Education, Employed, ApplicantIncome, CoApplicantIncome, Loan_amount, Loan_amount_term, Credit_history ,property_area ])

    st.success(diagnosis)








if __name__ == "__main__":
    main()
