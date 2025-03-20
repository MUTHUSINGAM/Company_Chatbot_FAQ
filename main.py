import streamlit as st
from transformers import pipeline
import time

def chatbot():
    st.title("💬 dVerse Technologies Company AI Chatbot")
    st.write("Ask me anything about Dverse Technologies!")
    
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
    
    context = (
    "Dverse Technologies, founded in 2021, is an innovative, product-oriented company specializing in AI-driven assistive technology solutions. "
    "Headquartered in Chennai, Tamil Nadu, India, the company focuses on developing inclusive technology for individuals with visual impairments. "
    "Dverse Technologies’ flagship product, CuriO, is a non-braille human-computer interface designed to help visually impaired individuals code in mainstream programming languages, empowering them to work in the technology industry. "
    "The company also provides services to institutions, research organizations, and companies working on accessibility solutions, focusing on enabling inclusion in technology. "
    "Dverse Technologies was incubated at IIT Madras Research Park and is recognized as a Startup India participant. "
    "The company is led by a team of experienced professionals, with key founders being Sameer Malik, Krishna Thiruvengadam, Deepika Gopalakrishnan, and Vivek Devaraj. "
    "As of 2023, Dverse Technologies employs approximately 50-100 people, including engineers, AI specialists, accessibility experts, and business professionals. "
    "The company operates from 9 AM to 6 PM, Monday through Friday, with flexible working hours for certain teams based on project needs. "
    "Dverse Technologies has seen rapid growth and expects an income of approximately ₹5-8 crores in the current fiscal year (2024). "
    "The primary customers of Dverse Technologies include visually impaired individuals, educational institutions, tech companies, and government agencies focused on assistive technology and inclusion. "
    "The company collaborates with prestigious academic institutions such as Technische Universität Dresden and IIT Madras Research Park, and is supported by various sponsors in the accessibility and AI sectors. "
    "Dverse Technologies has achieved significant milestones, including the successful deployment of CuriO, recognition as a Startup India participant, and being incubated at IIT Madras Research Park. "
    "### Key Roles at Dverse Technologies and Employee Distribution:\n"
    "- **AI/ML Engineers**: 15-20 employees\n"
    "- **Software Developers**: 10-15 employees\n"
    "- **Accessibility Specialists**: 5-10 employees\n"
    "- **Research Scientists**: 5-8 employees\n"
    "- **Business Development Managers**: 5 employees\n"
    "Dverse Technologies is continuously expanding its team and is currently hiring for several key positions including AI/ML Engineers, Software Developers, Accessibility Specialists, Research Scientists, and Business Development Managers. "
    "Salaries vary based on the role and experience, with AI/ML Engineers starting at ₹8,00,000 per annum and Software Developers at ₹6,00,000 per annum. "
    "Candidates should have a strong background in relevant fields such as AI, software development, and accessibility, with proficiency in Python, machine learning frameworks, and AI algorithms being essential for technical roles. "
    "### Location and Contact Details:\n"
    "- **Headquarters**: Chennai, Tamil Nadu, India\n"
    "- **Other Collaborations and Offices**: IIT Madras Research Park, Technische Universität Dresden (Germany), and several other global locations.\n"
    "For more details on job vacancies and to apply, visit the Dverse Technologies careers page or check LinkedIn updates. "
    "You can contact Dverse Technologies for inquiries at: support@dverselabs.com\n"
    "Relevant links:\n"
    "LinkedIn: https://www.linkedin.com/company/dverse-technologies\n"
    "Website: https://www.dverselabs.com"
)
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display chat history
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["text"])

    # User input
    user_input = st.chat_input("Type your question here...")
    
    if user_input:
        
        st.session_state["messages"].append({"role": "user", "text": user_input})
        with st.chat_message("user"):
            st.write(user_input)
        
       
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                result = qa_pipeline(question=user_input, context=context)
                bot_response = result["answer"]
                time.sleep(1)
                st.write(bot_response)
        
        
        st.session_state["messages"].append({"role": "assistant", "text": bot_response})

if __name__ == "__main__":
    chatbot()
