import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge",page_icon="✨")

st.title("Growth Mindset Challenge: Web App with Streamlit ✨")
st.header("🚀Welcome to the Growth Mindset Challenge!🚀")
st.write("Embrace your potential and never stop striving to be better.Wishing you all the best on your journey to growth and success!")

# quote
st.header("💡Today's Growth Mindset Quote")
st.write("Your Mindset determines your success. Believe in growth, Embrace challenges, & keep learning!🌱✨")

st.header("What's Your Challenge Today?")
# user input field
user_input = st.text_input("Describe a challenge you are facing today: ")

# Condition
if user_input:
    st.success(f"You are facing: {user_input} keep pushing forword towards your goal")
else:
    st.warning("Tell us about a challenge to get started! ⭐")

# Reflecting
st.header("Reflect on your  challenge!")
#input field  for challenge
reflection=st.text_input("What did you learn from this challenge?")

# condition
if reflection:
    st.success(f"Great insight! Keep learning and grownig! {reflection} 🌟")
else:
    st.warning("Reflecting on past challenges can help you grow! 🌟 Share your difficulties")

    # Motivation
st.header("😇 Motivation")
st.write("Believe in your self. You are stronger than you thing, more capable than you imagine, and closer to your goals than you realize.")

# Achievement

st.header("🏆 Celebrate your Achievements!")
achievement=st.text_input("Share something you have recently achieved:")

if achievement:
    st.success(f"Congratulation! on your achievement! 🎉 {achievement}")
else:
    st.info("🎉Share your wins, no matter how big or small!")

# footer
st.write("Keep believing yourself. you are capable of amazing things!")
st.markdown("""
Created with 🧡 by [Faraz Alam]
""")