import streamlit as st
from memberview import GymMemberManager


gym_instance = GymMemberManager()

tab1, tab2, tab3, tab4= st.tabs(["Add Member","View Member","Update Memeber","Delete Member"])

plans = ["1 month","2 months","3 months","6 months","8 months","1 year"]
with tab1:
    st.header("Add New Member....!")
    name = st.text_input("Enter Member Name")
    place = st.text_input("Enter Place Name")
    plan = st.selectbox("Enter The Plan",["1 month","2 months","3 months","6 months","8 months","1 year"])
    mobile = st.text_input("Enter Member Phone Number")
    fee = st.number_input("Enter The Fee")
    joining_date = st.date_input("Enter the Joining Date")
    if st.button("Submit"):
        gym_instance.post(name=name,place=place,plan=plan,mobile=mobile,fee=fee,joining_date=joining_date)
        st.success("Member added successfully....!")
        
        
with tab2:
    st.header("View Gym Member Details....!")
    records = gym_instance.get()
    print(records)
    if records:
       st.table(records)
    else:
        st.warning("No records found...!")
        
with tab3:
    st.title("Update Donor Details....!")
    records = gym_instance.get()
    
    if records:
        member_ids = [r[0] for r in records]
        id = st.selectbox("Select Member ID to Update", member_ids)
        
        record = gym_instance.get_object(id=id)
        name = st.text_input("Enter Member Name :", value = record[1])
        place = st.text_input("Enter Memebr Place :", value = record[2])
        mobile = st.text_input("Enter Member Mobile Number :", value = record[4])
        plan = st.selectbox("Select Plan",plans,
                            index = plans.index(record[3]),
                            key = "update_group")
        fee = st.number_input("Enter Fee :", value = record[5])
        joining_date =st.date_input("Joining Date :", value = record[6])
        
        
        if st.button("Update"):
            status, message = gym_instance.put(id=id,
                                               name=name,
                                               place=place,
                                               plan=plan,
                                               mobile=mobile,
                                               fee=fee,
                                               joining_date=joining_date)
            if status:
                st.success(message)
            else:
                st.error(message)
                
    else:
        st.warning("No member Found.....!")
    
with tab4:
    st.title("Delete Member")
    records = gym_instance.get()

    if records:
        member_ids = [record[0] for record in records]

        id = st.selectbox("Select Member ID to Delete",member_ids)

        if st.button("Delete Member"):
            status, message = gym_instance.delete(id=id)

            if status:
                st.success(message)
                st.rerun()
                st.success("Member deleted successfully....!")
            else:
                st.error(message)

    else:
        st.warning("No members available to delete.")