import streamlit as st

st.set_page_config(
    page_title="Smart ATM",
    page_icon="🏦",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------
if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "pin" not in st.session_state:
    st.session_state.pin = "1234"

if "login" not in st.session_state:
    st.session_state.login = False

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
}

.main-title{
font-size:42px;
font-weight:bold;
color:white;
text-align:center;
margin-bottom:20px;
}

.card{
background:white;
padding:25px;
border-radius:20px;
box-shadow:0px 10px 30px rgba(0,0,0,.25);
}

.balance{
font-size:45px;
font-weight:bold;
color:#1e40af;
text-align:center;
}

.subtitle{
font-size:18px;
text-align:center;
color:gray;
}

.stButton>button{
width:100%;
background:#2563eb;
color:white;
border-radius:12px;
height:45px;
font-size:17px;
border:none;
}

.stButton>button:hover{
background:#1d4ed8;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Login
# -----------------------------
if not st.session_state.login:

    st.markdown("<div class='main-title'>🏦 Smart ATM</div>", unsafe_allow_html=True)

    col1,col2,col3=st.columns([1,2,1])

    with col2:

        st.markdown("<div class='card'>",unsafe_allow_html=True)

        st.subheader("Login")

        p=st.text_input("Enter ATM PIN",type="password")

        if st.button("Login"):

            if p==st.session_state.pin:
                st.session_state.login=True
                st.success("Login Successful")
                st.rerun()

            else:
                st.error("Invalid PIN")

        st.markdown("</div>",unsafe_allow_html=True)

# -----------------------------
# Dashboard
# -----------------------------
else:

    st.sidebar.title("🏦 Smart ATM")

    menu=st.sidebar.radio(
        "Navigation",
        ["Dashboard","Deposit","Withdraw","Change PIN"]
    )

    if st.sidebar.button("Logout"):
        st.session_state.login=False
        st.rerun()

    if menu=="Dashboard":

        st.markdown("<div class='main-title'>Bank Dashboard</div>",unsafe_allow_html=True)

        st.markdown(f"""
        <div class='card'>
        <div class='subtitle'>Available Balance</div>
        <div class='balance'>₹ {st.session_state.balance}</div>
        </div>
        """,unsafe_allow_html=True)

    elif menu=="Deposit":

        st.title("💰 Deposit Money")

        amount=st.number_input(
            "Amount",
            min_value=1,
            step=100
        )

        if st.button("Deposit"):

            st.session_state.balance+=amount
            st.success("Deposit Successful")

    elif menu=="Withdraw":

        st.title("💸 Withdraw Money")

        amount=st.number_input(
            "Withdraw Amount",
            min_value=1,
            step=100
        )

        if st.button("Withdraw"):

            if amount>st.session_state.balance:
                st.error("Insufficient Balance")
            else:
                st.session_state.balance-=amount
                st.success("Withdrawal Successful")

    elif menu=="Change PIN":

        st.title("🔐 Change PIN")

        old=st.text_input("Current PIN",type="password")

        new=st.text_input("New PIN",type="password")

        confirm=st.text_input("Confirm PIN",type="password")

        if st.button("Change PIN"):

            if old!=st.session_state.pin:
                st.error("Incorrect Current PIN")

            elif new!=confirm:
                st.error("PIN Does Not Match")

            elif len(new)!=4 or not new.isdigit():
                st.error("PIN must be 4 digits")

            else:
                st.session_state.pin=new
                st.success("PIN Changed Successfully")
