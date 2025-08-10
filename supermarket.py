import streamlit as st
import pandas as pd
 
st.title("Total Bill Calculator", width="stretch")

noOfUnits = 0

col1, col2, col3 = st.columns([3, 1, 1])

with col1:
   


    total_cost = st.number_input("Enter Total Cost", key="pre",min_value=0, step=1, format="%d")
        

    if total_cost:
           total_cost=int(total_cost)
           

          
            
if st.button("Calculate") :
    try:
        row=[]
        amount=int(total_cost)
       

        if amount >= 5000:
            discount = (amount / 100) * 20
            row.append(["Total Bill", discount, 20, total_cost])
            total_bill = round(total_cost - discount,2)
        elif amount >= 2500:
            discount = (amount / 100) * 15
            row.append(["Total Bill", discount, 15, total_cost])
            total_bill = round(total_cost - discount,2)
        elif amount >= 1000:
            discount = (amount / 100) * 10
            row.append(["Total Bill", discount, 10, total_cost])
            total_bill = round(total_cost - discount,2)

        total_bill = amount - discount
        total_cost=amount-discount
    
        
       

        st.info(f"Total charge: Rs.{total_bill:.2f}")

            

        df = pd.DataFrame(row,columns=["Description","Total Cost","Discount","Total Bill"])

        df["Total cost(Rs.)"] = df["Total cost(Rs.)"].apply(lambda x: f"{x:.2f}" if
                                                          isinstance(x, (int, float)) else x)
                
        df["Discount"] = df["Discount"].apply(lambda x: f"{x:.2f}" if
                                                          isinstance(x, (int, float)) else x)
                
        
        df["Total Bill"] = df["Total Bill"].apply(lambda x: f"{x:.2f}" if
                                                          isinstance(x, (int, float)) else x)        
        st.table(df)

    except Exception as e:
                st.error(f"Error calculating bill: {e}")