import streamlit as st
from chatbot import chatbot_response
from database import create_tables, get_complaints

# Initialize database
create_tables()

st.set_page_config(page_title="Tenant Services Chatbot", layout="centered")

st.title("🏠 Tenant Services Chatbot")
st.caption("Your digital caretaker 🤖")

# Chat memory
if "chat" not in st.session_state:
    st.session_state.chat = []

# User input
user_input = st.text_input("Ask your question here")

if st.button("Send"):
    if user_input.strip() != "":
        reply = chatbot_response(user_input)
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", reply))

# Display chat
for sender, message in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")

st.divider()

# Admin section
st.subheader("📋 Registered Complaints (Admin View)")
complaints = get_complaints()

if complaints:
    for c in complaints:
        st.write(f"🛠️ {c[1]} | Status: {c[2]} | Time: {c[3]}")
else:
    st.write("No complaints yet.")
