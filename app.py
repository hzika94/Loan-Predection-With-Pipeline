import streamlit as st
import joblib 
import pandas as pd

Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")

def predict(Gender, Married, Dependents, Education, Self_Employed,ApplicantIncome, CoapplicantIncome, LoanAmount,Loan_Amount_Term ,Credit_History,Property_Area):
    test_df = pd.DataFrame(columns = Inputs)
    test_df.at[0,"Gender"] = Gender
    test_df.at[0,"Married"] = Married
    test_df.at[0,"Dependents"] = Dependents
    test_df.at[0,"Education"] = Education
    test_df.at[0,"Self_Employed"] = Self_Employed
    test_df.at[0,"ApplicantIncome"] = ApplicantIncome
    test_df.at[0,"CoapplicantIncome"] = CoapplicantIncome
    test_df.at[0,"LoanAmount"] = LoanAmount
    test_df.at[0,"Loan_Amount_Term"] = Loan_Amount_Term
    test_df.at[0,"Credit_History"] = Credit_History
    test_df.at[0,"Property_Area"] = Property_Area
    result = Model.predict(test_df)[0]
    return result
    
def main():
    st.title("Loan App With Pipline")
    Gender = st.selectbox("Gender" , ['Male', 'Female'])
    st.text(Gender)
    Married = st.selectbox("Married" , ['No', 'Yes'])
    st.text(Married)
    Dependents = st.slider("Dependents" , min_value=0, max_value=10, value=0, step=1)
    st.text(Dependents)
    Education = st.selectbox("Education" ,['Graduate', 'Not Graduate'])
    st.text(Education)
    Self_Employed = st.selectbox("Self_Employed" , ['No', 'Yes'])
    st.text(Self_Employed)
    ApplicantIncome = st.slider("ApplicantIncome" , min_value=0, max_value=200000, value=0, step=1)
    st.text(ApplicantIncome)
    CoapplicantIncome = st.slider("CoapplicantIncome" , min_value=0, max_value=200000, value=0, step=1)
    st.text(CoapplicantIncome)
    LoanAmount = st.slider("LoanAmount" , min_value=1000, max_value=10000000, value=0, step=1000)
    st.text(LoanAmount)
    Loan_Amount_Term = st.selectbox("Loan_Amount_Term" , [360.0, 120.0, 240.0,180.0, 60.0, 300.0, 480.0, 36.0, 84.0, 12.0])
    st.text(Loan_Amount_Term)
    Credit_History = st.selectbox("Credit_History" , [1 , 0])
    st.text(Credit_History)
    Property_Area = st.selectbox("Property_Area" , ['Urban', 'Rural', 'Semiurban'] )
    st.text(Property_Area)
    if st.button("Predict"):
        st.text((Gender, Married, Dependents, Education, Self_Employed , ApplicantIncome, CoapplicantIncome, LoanAmount , Loan_Amount_Term , Credit_History , Property_Area))
        result = predict(Gender, Married, Dependents, Education, Self_Employed , ApplicantIncome, CoapplicantIncome, LoanAmount , Loan_Amount_Term , Credit_History , Property_Area)
        st.text(result)
        label = ["Not Accepted","Accepted"]
        st.text("The output is {}".format(label[result]))
if __name__ == '__main__':
    main()
    
    
