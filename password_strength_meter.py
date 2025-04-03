import re

import streamlit as st

#styling
st.set_page_config(page_title="Password Strength Meter", page_icon="🌘" , layout="centered")

#custom css 
st.markdown(""""
<style>"
        .main {text-align: center;}"
        .stTextInput {width: 60% !important; margin: auto; }"
        .stButton button {width: 50%; background-color #4CAF50; color: white; font-size: 18px; }"
        .stButtonbutton:hover { background-color: #45a049}
</style>
""",unsafe_allow_html=True)

#title and descripition

st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its security level.🔍")

#function to check password metrer

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.appened("❌ password should be **atleast 8 character long**.")

    if re.search(r"[A-Z]", password)and re.search(r"[a-z]", password):
                 score += 1
    else:
           feedback.appened("❌ password should include**both uppercase (A-Z) and lowercase  (a-z) letters**.")

    if re.search(r"\d", password):
          score += 1
    else:
           feedback.appened("❌ password should include **atleast one number (0-9)**.")

#special character

    if re.search(r"[!@#$%^&*]", password):
          score += 1
    else:
           feedback.appened("❌ include  **at least one special character (!@#$%^&*)** .")

#display password strength results

    if score == 4:
          st.success("✅ **strong password** - your password is secure.")
    elif score == 3 :
          st.info("⚠️ ** moderate password** -consider improving security by adding more feature")
    else:
          st.error("❌ ** week password** - follow the suggestion below to strength it.")


#feedback

    if feedback:
       with st.expander("🔍** improve your password** "):
             for item in feedback:
                 st.write(item) 

password = st.text_input("enter your password:" , type="password", help="ensure your password is strong 🔐")


#button

if st.button("check strength"):
      if password:
            check_password_strength(password)

      else:
            st.warning("⚠️ please enter a password first!")   #show warning if password empty 