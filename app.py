# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 12:11:36 2022

@author: ddhanawa
"""
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import streamlit as st
from sqlalchemy import update
from datetime import date
import datetime

import numpy as np

datetime.datetime.now()

from sqlalchemy import Column,String,Integer,Float,ForeignKey,DATE
from sqlalchemy.ext.declarative import declarative_base
from PIL import Image
import pandas as pd

st.set_page_config(layout='wide',page_icon=':bar_chart:')
#img = Image.open("C:\\Users\\ddhanawa\\Downloads\\auto.jpeg")



Base = declarative_base()

class UserInput(Base):
    
    __tablename__ = "user"
    
    id = Column(Integer,primary_key = True)
    purchase_date = Column(DATE)
    sales_date = Column(DATE)
    seller_name = Column(String)
    seller_contact = Column(String)
    token_amount = Column(Integer)
    tokan_date = Column(DATE)
    first_part_payment = Column(Integer)
    first_part_payment_date = Column(DATE)
    first_part_payment_comment = Column(String)
    second_part_payment = Column(Integer)
    second_part_payment_date = Column(DATE)
    second_part_payment_comment = Column(String)
    third_part_payment = Column(Integer)
    third_part_payment_date = Column(DATE)
    third_part_payment_comment = Column(String)
    final_part_payment = Column(Integer)
    final_payment_date = Column(DATE)
    final_payment_comment = Column(String)
    
    purchase_amount = Column(Integer)
    model = Column(String)
    engine_number = Column(String)
    chassis_number = Column(String)          
    vehicle_Number = Column(String)
    year = Column(Integer)
    contact_Number = Column(String)
    owner_Financer_Name = Column(String)
    Parking = Column(Integer)
    RCbook = Column(Integer)
    Tax = Column(Integer)
    Machinical_exp = Column(Integer)
    Tyre_Stephny = Column(Integer)
    Commission = Column(Integer)
    Diseal = Column(Integer)
    Driver = Column(Integer)
    others = Column(Integer)
    final_purchase_price = Column(Integer)
    seller_name = Column(String)
    seller_contact = Column(Integer)
    commission1 = Column(Integer)
    sell_amount = Column(Integer)
    balance = Column(Integer)
    profitloss = Column(Integer)
    

class UserSearchInput(Base):
    
    __tablename__ = "search"
    
    id = Column(Integer,primary_key = True)
 
    searchstring = Column(String)

class UserInputPayAmount(Base):
    
    __tablename__ = "payment"
    id = Column(Integer,primary_key = True)
    
    payment_date = Column(DATE)
    payment_to = Column(String)
    amount = Column(Integer)
    


class UserInputRecAmount(Base):
    
    __tablename__ = "received"
    
    id = Column(Integer,primary_key = True)
    payment_received_date = Column(DATE)
    received_from = Column(String)
    amount = Column(Integer)
    


if __name__ == "__main__":
    engine = create_engine('sqlite:///Jaydeep_Finacial_database.db')
    Base.metadata.create_all(engine)

##############################



engine = create_engine('sqlite:///Jaydeep_Finacial_database.db')

Session = sessionmaker(bind=engine)

sess = Session()



#st.sidebar.image(img,use_column_width=True)

radio = st.sidebar.radio('Pages',options=['Dashboard','Purchase Entry','Daily Expenses','Sales Entry','Online Cars Details','Backup'])

def entry():
    
    
        def add_num(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):
            sum = num1+num2+num3+num4+num5+num6+num7+num8+num9+num10
            
            return sum
        
     
        
    

    
        with st.form(key='new',clear_on_submit=True):
            c1,c2,c3,c4 = st.columns(4)
            with c1:
                purchase_date = st.date_input('Date')
                model = st.text_input('Model').upper()
                vehicle_Number = st.text_input('Vehicle Number').upper()
                year = st.slider('Year',min_value=2000,max_value=2030)
                engine_number = st.text_input('Engine Number').upper()
                chassis_number = st.text_input('Chassis Number').upper()
      
            with c2:
                owner_Financer_Name = st.text_input('Party Name').upper()
                contact_Number = st.text_input('Contact Number')
                purchase_amount = st.number_input('Purchase Amount',key='pa',min_value=0,step=10000)
           
            with c3:
                
                Parking= st.number_input('Parking',key='Parking',min_value=0,step=1000)
                RCbook= st.number_input('RC Book',key='book',min_value=0,step=1000)
                Tax= st.number_input('Tax',key='tax',min_value=0,step=1000)
                Machinical_exp= st.number_input('Machinical Exp',key='Machinical',min_value=0,step=1000)
            with c4:
                Tyre_Stephny= st.number_input('Tyre /Stephny',key='Tyre',min_value=0,step=1000)
                Commission= st.number_input('Commission',key='Commission',min_value=0,step=1000)
                Diseal= st.number_input('Diseal',key='Diseal',min_value=0,step=1000)
                Driver= st.number_input('Driver',key='Driver',min_value=0,step=1000)
                others = st.number_input('Others',key='Others',min_value=0,step=1000)
                sum1= add_num(purchase_amount,Parking,RCbook,Tax,Machinical_exp,Tyre_Stephny,Driver,Commission,Diseal,others)
              
            submit = st.form_submit_button('Submit')
          
        if submit:
            try:
                entry = UserInput(purchase_date =purchase_date,model= model,vehicle_Number= vehicle_Number,year=year,owner_Financer_Name=owner_Financer_Name,contact_Number=contact_Number,purchase_amount=purchase_amount, Parking=Parking, RCbook=RCbook, Tax=Tax, Machinical_exp=Machinical_exp, Tyre_Stephny=Tyre_Stephny, Commission=Commission, Diseal=Diseal, Driver=Driver, others=others, final_purchase_price=sum1,chassis_number=chassis_number,engine_number=engine_number)
                sess.add(entry)
                sess.commit()
                st.success(f'Details Submitted successfully final vehicle price is {sum1}')
                
            except Exception as e:
                st.error(f'some error occured {e}')
       # if st.checkbox("view data"):
            
        #    results = sess.query(UserInput).all()
         #   for item in results:
          #      st.write(item.purchase_date,item.model,item.vehicle_Number,item.year,item.owner_Financer_Name,)

            

    

if radio == 'Purchase Entry':
    if __name__ == '__main__':
        entry()
        
  
def entry1():
    
        def balance_amt(num1,num2,num3,num4,num5):
            sum = (num1+num2+num3+num4+num5)
            
            return sum
            
       
     
        with st.form(key='new1',clear_on_submit=True):
            last_record = sess.query(UserInput.vehicle_Number).all()

            final_search = []
            
            for row in last_record:
           
               final_search.append(row.vehicle_Number)
            
          
           
            
            search_vehicle =st.selectbox('Choose Vehicle Number',options=final_search)
            results = sess.query(UserInput).filter(UserInput.vehicle_Number == search_vehicle)
    
           # search_vehicle =st.text_input('Search Vehicle Number')
            submit1 = st.form_submit_button('Search')
            
            #if submit1:
            
             #  entry = UserSearchInput(searchstring=search_vehicle)
              # sess.add(entry)
               #sess.commit()
               
               
            
    
            
       
           
            
            for row in results:
           
                purchase_date=row.purchase_date
                purchase_amount=row.purchase_amount
                model=row.model
                vehicle_Number=row.vehicle_Number
                year1=row.year
                contact_Number=row.contact_Number
                owner_Financer_Name=row.owner_Financer_Name
                Parking=row.Parking
                RCbook=row.RCbook
                Tax=row.Tax
                Machinical_exp=row.Machinical_exp
                Tyre_Stephny=row.Tyre_Stephny
                Commission=row.Commission
                Diseal=row.Diseal
                Driver=row.Driver
                others=row.others
                final_purchase_price=row.final_purchase_price
                seller_name=row.seller_name
                seller_contact=row.seller_contact
                commission1=row.commission1
                sell_amount=row.sell_amount
                balance=row.balance
                profitloss=row.profitloss
                sales_date=row.sales_date
                seller_name=row.seller_name
                seller_contact=row.seller_contact
                commission1=row.commission1
                
                token_amount=row.token_amount
                tokan_date=row.tokan_date
                first_part_payment=row.first_part_payment
                first_part_payment_date=row.first_part_payment_date
                first_part_payment_comment=row.first_part_payment_comment
                second_part_payment=row.second_part_payment
                second_part_payment_date=row.second_part_payment_date
                second_part_payment_comment=row.second_part_payment_comment
                third_part_payment=row.third_part_payment
                third_part_payment_date=row.third_part_payment_date
                third_part_payment_comment=row.third_part_payment_comment
                final_payment=row.final_part_payment
                final_payment_date=row.final_payment_date
                final_payment_comment=row.final_payment_comment
                
            
            c1,c2,c3,c4,c5 = st.columns([1.2,1.2,1,1,1])
            with c1:
                
                sales_date = st.date_input('Sell Date',sales_date)
                seller_name = st.text_input('Seller Name',seller_name).upper()
                seller_contact = st.text_input('Seller Contact',seller_contact)            
                sell_amount = st.number_input('Sell Amount',sell_amount,step=1000)
                commission1 = st.number_input('Commision',commission1,step=1000)
                tokan_date = st.date_input('Tokan Date',value=tokan_date)
                token_amount = st.number_input('Tokan Amount',token_amount,step=1000)
                first_part_payment = st.number_input('First Part Payment',first_part_payment,step=1000)
                first_part_payment_date = st.date_input('First Part Payment Date',first_part_payment_date)
                first_part_payment_comment = st.text_input('first Comment',first_part_payment_comment)
                second_part_payment = st.number_input('Second Part Payment',second_part_payment,step=1000)
                second_part_payment_date = st.date_input('SecondPart Payment Date',second_part_payment_date)
                second_part_payment_comment = st.text_input('Second Comment',second_part_payment_comment)
                third_part_payment = st.number_input('Third Part Payment',third_part_payment,step=1000)
                third_part_payment_date = st.date_input('Third Part Payment Date',third_part_payment_date)
                third_part_payment_comment = st.text_input('third Comment',third_part_payment_comment)
                final_payment = st.number_input('final Payment',final_payment,step=1000)
                final_payment_date = st.date_input('final Payment Date',final_payment_date)
                final_payment_comment = st.text_input('Final Comment',final_payment_comment)
                sum2 = balance_amt(token_amount,first_part_payment,second_part_payment,third_part_payment,final_payment)
                submit = st.form_submit_button('Submit')
                
                
               
            with c2:
            
                purchase_date = st.date_input('Purchase Date',purchase_date,disabled=True)
                final_purchase_amount = st.number_input('Final Purchase Price',final_purchase_price,disabled=True)
                
                balance = st.number_input('Balance Amount',value=sell_amount-sum2,disabled=True)
                
                profitloss = st.number_input("Profit/loss",value =sell_amount-final_purchase_amount-commission1,step=1000,disabled=True,format="%i")
                model = st.text_input('Model',model,disabled=True)
                year = st.slider('Year',min_value=2000,max_value=2030,value = year1,disabled=True)
      
            with c3:
                owner_Financer_Name = st.text_input('Party Name',owner_Financer_Name,disabled=True)
                contact_Number = st.text_input('Contact Number',contact_Number,disabled=True)
                purchase_amount = st.number_input('Purchase Amount',key='pa',min_value=0,step=10000,value = purchase_amount,disabled=True)
           
            with c4:
                vehicle_Number = st.text_input('Vehicle Number',vehicle_Number,disabled=True)

                Parking= st.number_input('Parking',key='Parking',min_value=0,step=1000,value = Parking,disabled=True)
                RCbook= st.number_input('RC Book',key='book',min_value=0,step=1000,value = RCbook,disabled=True)
                Tax= st.number_input('Tax',key='tax',min_value=0,step=1000,value =Tax,disabled=True)
                Machinical_exp= st.number_input('Machinical Exp',key='Machinical',min_value=0,step=1000,value = Machinical_exp,disabled=True)
            with c5:
                
                Tyre_Stephny= st.number_input('Tyre /Stephny',key='Tyre',min_value=0,step=1000,value=Tyre_Stephny,disabled=True)
                Commission= st.number_input('Commission',key='Commission',min_value=0,step=1000,value=Commission,disabled=True)
                Diseal= st.number_input('Diseal',key='Diseal',min_value=0,step=1000,value=Diseal,disabled=True)
                Driver= st.number_input('Driver',key='Driver',min_value=0,step=1000,value=Driver,disabled=True)
                others = st.number_input('Others',key='Others',min_value=0,step=1000,value=others,disabled=True)
               
                 
            
                
                
        
                
            
        if submit:
            try:
               sess.query(UserInput).filter(UserInput.vehicle_Number == search_vehicle).update({'sales_date': sales_date,'seller_name': seller_name,'seller_contact': seller_contact,'commission1': commission1,'sell_amount': sell_amount,'first_part_payment': first_part_payment,'first_part_payment_date': first_part_payment_date,'first_part_payment_comment': first_part_payment_comment,'second_part_payment_date': second_part_payment_date,'third_part_payment': third_part_payment,'third_part_payment_date': third_part_payment_date,'third_part_payment_comment': third_part_payment_comment,'final_payment_date': final_payment_date,'final_payment_comment': final_payment_comment,'final_part_payment': final_payment,'token_amount':token_amount,'tokan_date':tokan_date,'second_part_payment':second_part_payment,'balance':balance,'second_part_payment_comment':second_part_payment_comment,'profitloss':profitloss})
                                                                                               
               sess.commit()
               st.success('Details Submitted successfully') 
            except Exception as e:
                st.error(f'some error occured {e}')
    
if radio == 'Sales Entry':
    if __name__ == '__main__':
        entry1()


name = 'user'
name1 = 'received'
name2 = 'payment'




st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

df = pd.read_sql(f'SELECT vehicle_Number,model,seller_contact,sales_date,balance,tokan_date,token_amount,first_part_payment_date,first_part_payment,second_part_payment_date,second_part_payment,third_part_payment_date,third_part_payment,final_payment_date,final_part_payment,sell_amount,profitloss FROM "{name}"',engine,parse_dates=['purchase_date','sales_date','tokan_date','first_part_payment_date','second_part_payment_date','third_part_payment_date','final_payment_date'])
df1 = pd.read_sql(f'SELECT * FROM "{name1}"',engine,parse_dates='payment_received_date')
df2 = pd.read_sql(f'SELECT * FROM "{name2}"',engine,parse_dates='payment_date')

def detail_analysis():
    #global df,df1,df2
   # df = pd.read_sql(f'SELECT vehicle_Number,model,seller_contact,sales_date,balance,tokan_date,token_amount,first_part_payment_date,first_part_payment,second_part_payment_date,second_part_payment,third_part_payment_date,third_part_payment,final_payment_date,final_part_payment,sell_amount,profitloss FROM "{name}"',engine,parse_dates=['purchase_date','sales_date','tokan_date','first_part_payment_date','second_part_payment_date','third_part_payment_date','final_payment_date'])
   # df1 = pd.read_sql(f'SELECT * FROM "{name1}"',engine,parse_dates='payment_received_date')
    #df2 = pd.read_sql(f'SELECT * FROM "{name2}"',engine,parse_dates='payment_date')
    st.subheader(':bar_chart: Pending Amount Report')
    balance_amount = df[df['balance']>=1]
    st.write(balance_amount.to_html(), unsafe_allow_html=True)
    
    st.markdown('****************')
    
    st.subheader(':bar_chart: Monthly Sales/Profit')
    date_sale= df.groupby(df['sales_date'].dt.strftime('%B-%y'))[['sell_amount','profitloss','balance']].sum()
    col1,col2 = st.columns(2)
    with col1:
        st.line_chart(date_sale,use_container_width=False)
    with col2:    
        st.write(date_sale.to_html(), unsafe_allow_html=True)


    
    st.markdown('****************')
    col1,col2 = st.columns(2)
    with col1:
        st.subheader(':bar_chart: Monthly Received Amount')
        date_wise_exp = df1.groupby(df1['payment_received_date'].dt.strftime('%B-%y'))[['amount']].sum()
        st.write(date_wise_exp.to_html(), unsafe_allow_html=True)
        st.markdown('****************')
    
    
    with col2:
        st.subheader(':bar_chart: Monthly Expenses')
        date_wise_exp1 = df2.groupby(df2['payment_date'].dt.strftime('%B-%y'))[['amount']].sum()
        st.write(date_wise_exp1.to_html(), unsafe_allow_html=True)
        st.markdown('****************')
    st.subheader(':bar_chart: Top 5 Profitable Trades')
    profitloss = df.sort_values('profitloss',ascending=False).head(5)
    
    st.markdown('****************')
    st.subheader(':bar_chart: Purchase / Sales History')
    st.write(df.to_html(), unsafe_allow_html=True)
    st.markdown('*******************')
   
   
if radio == 'Dashboard':
    try:
        if __name__ == '__main__':
            detail_analysis()    
    except UnboundLocalError:
        st.write('Select proper gaaadi number')



def daily_expenses():
    with st.form(key='new',clear_on_submit=True):
        st.subheader('Amount Received')
        c1,c2,c3,c4 = st.columns([1,4,1,.1])
        
        with c1:
            payment_received_date = st.date_input('Date')
        with c2:
            received_from = st.text_input('Amount Received From')
        
        with c3:
            amount = st.number_input('Amount',step=2000,min_value=0)
     

            
            submit2 = st.form_submit_button('Submit')              
            
    if submit2:

            entry3 = UserInputRecAmount(payment_received_date=payment_received_date,received_from =received_from,amount=amount)
            sess.add(entry3)
            sess.commit()
            st.success('Details Submitted successfully')
            
        


def daily_expenses1():
    with st.form(key='new22',clear_on_submit=True):
        st.subheader('Amount Paid')
        c1,c2,c3,c4 = st.columns([1,4,1,.1])
        
        with c1:
            payment_date  = st.date_input('Date')
        with c2:
            payment_to  = st.text_input('Amount Paid to')
        
        with c3:
            amount = st.number_input('Amount',step=2000,min_value=0)
     

            
            submit2 = st.form_submit_button('Submit')              

    if submit2:
        entry4 = UserInputPayAmount(payment_date=payment_date,payment_to=payment_to,amount=amount)
        sess.add(entry4)
        sess.commit()
        st.success('Details Submitted successfully')

    st.subheader(':bar_chart: Amount Received')
    st.write(df1.to_html(), unsafe_allow_html=True)
    st.markdown('*******************')
    st.subheader(':bar_chart: Amount Paid')
    st.write(df2.to_html(), unsafe_allow_html=True)


if radio == 'Daily Expenses':
    if __name__ == '__main__':
        daily_expenses()
    
        daily_expenses1()
        
def backup():
        
        time = date.today()
        df.to_csv(f'Purchase_sales_register.csv')
        df1.to_csv('payment_rcvd_register.csv')
        df2.to_csv('payment_register.csv')
        st.success('Backup files created successfully')
    
if radio == 'Backup':
    if __name__ == '__main__':
        backup()


   
