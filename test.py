import streamlit as st
tab1, tab2, tab3, tab4 = st.tabs(["Intro", "About Us","Scan", "FAQS"])
add_selectbox = st.sidebar.image("EcoScan_Slogan_Image.png")

with tab1:
   

    
    st.markdown("<h1 style='text-align: center; color: green;'>Home Page</h1>", unsafe_allow_html=True)
        
    st.write("Every day, the world generates millions of tons of waste, and India alone contributes over 277 million tons annually. Globally, more than 2 billion tons of waste are generated each year, and a significant portion of this ends up in landfills or pollutes our oceans. Sadly, much of this waste is recyclable, but due to improper sorting and lack of awareness, valuable materials are lost, and the environmental impact worsens.")

    st.write("At EcoScan, we are committed to addressing this issue with cutting-edge technology. Using advanced AI models, our platform scans objects to instantly determine if they are recyclable or not, ensuring that waste is sorted correctly at the source. By making recycling easier and more efficient, EcoScan can help reduce the volume of waste entering landfills, conserve natural resources, and lower the overall environmental footprint. Join us in reducing waste, protecting the environment, and building a cleaner future for generations to come.")
    
    
    st.subheader("Statistics:")
    col1, col2 = st.columns(2)
    with col1:
        st.image("image5.png", caption = "Plastic production in extremely high and is on the rise.")
    with col2:
        st.image("image6.png", caption = "Recyling centers aren't able to handle all the palstic they are getting, so they are sent to the ocean." )

with tab2:
    st.markdown("<h1 style='text-align: center; color: green;'>About Us</h1>", unsafe_allow_html=True)

    st.write("I am a 15 year old who is currently living in Hyderabad and studying at the International School of Hyderabad. I started this project becuase I was very passionate about waste management when I found out the my home city genereated the most waste per capita in India. Worst of all, there was a huge amounts of trash just outside my community. It lead me to research and start this app where we support more sustainble recyling practices by allowing our scanner to recognize whether or not a household item is recylable. ")
    st.write("We aim to make sustainable practices more accessible by giving everyone the tools to reduce their environmental footprint. We believe that small actions can lead to big change, and with EcoScan, everyone can play a role in building a cleaner, more sustainable future.")
with tab3:
    st.markdown("<h1 style='text-align: center; color: green;'>Scanner</h1>", unsafe_allow_html=True)
    st.write("Our scan requires a photo of the image that you want to check, and then we use \n AI software to see whether the image given is recyclabe or not. This AI software has a database of over \n 10K images. ")
    st.write("Take a scan now:")
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "txt", "pdf", "png"])

# Process the uploaded file
    if uploaded_file is not None:
    # Display file details
        st.write("Filename:", uploaded_file.name)
        st.write("File size:", uploaded_file.size, "bytes")


with tab4:
    st.markdown("<h1 style='text-align: center; color: green;'>FAQs</h1>", unsafe_allow_html=True)

    question1 = st.expander("What does this app do?")
    with question1:
        st.write("The app uses AI detection software to identify whether an item is recyclable or not. Simply take a photo or \nscan the item, and the app will provide guidance on how to dispose of it properly.")
   
    q1 = st.expander("Is it always accurate")
    with q1:
        st.write("Our AI is trained to be highly accurate, but no system is perfect. If you're unsure about the results, \nyou can check the app's recycling guidelines or verify with your local recycling center. The accuracy \n is the highest with household x")
   
    q2 = st.expander("Can I scan multiple items at once?")
    with q2:
        st.write("Currently, the app works best when you scan one item at a time for optimal accuracy.")


    q3 = st.expander("Can the app help me reduce waste?")
    with q3:
        st.write("Absolutely! The app not only identifies recyclable items but also offers tips on how to reduce waste, \n reuse materials, and make eco-friendly choices.")


    q4 = st.expander("Can the app work offline?")
    with q4:
        st.write("The app requires an internet connection to access the AI detection software. However, you can still \nbrowse recycling tips and guidelines offline.")
   
    q5 = st.expander("Does the app store my photos?")
    with q5:
        st.write("No, the app doesn’t store your photos permanently. They are only used temporarily for analysis and \nare deleted afterward to ensure your privacy.")
