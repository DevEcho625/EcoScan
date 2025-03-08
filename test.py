import streamlit as st
from ultralytics import YOLO
from PIL import Image
tab1, tab2, tab3, tab4 = st.tabs(["Intro", "About Us","Scan", "FAQS"])
add_selectbox = st.sidebar.image("EcoScan_Slogan_Image.png")
@st.cache_resource


def models():


    mod = YOLO('best.pt')    
    return mod

with tab1:
   
    
    
    st.markdown("<h1 style='text-align: center; color: green;'>Home Page</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='text-align: center;'>
            Every day, the world generates millions of tons of waste, and India alone contributes over 277 million tons annually. 
            Globally, more than 2 billion tons of waste are generated each year, and a significant portion of this ends up in landfills or pollutes our oceans. 
            Sadly, much of this waste is recyclable, but due to improper sorting and lack of awareness, valuable materials are lost, and the environmental impact worsens. \n \n
        </div>
        """,
        unsafe_allow_html=True)
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            At EcoScan, we are committed to addressing this issue with cutting-edge technology. Using advanced AI models, our platform scans objects to instantly 
            determine if they are recyclable or not, ensuring that waste is sorted correctly at the source. By making recycling easier and more efficient, EcoScan 
            can help reduce the volume of waste entering landfills, conserve natural resources, and lower the overall environmental footprint. 
            Join us in reducing waste, protecting the environment, and building a cleaner future for generations to come.


        </div>
        """,
        unsafe_allow_html=True)
    

    st.markdown(
    """
    <div style='text-align: center; color: white; margin-top: 20px;'>
        Take a scan now by going to our Scanner tab!
    </div>
    """,
    unsafe_allow_html=True)

    
    st.subheader("Statistics:")
    col1, col2 = st.columns(2)
    with col1:
        st.image("image5.png", caption = "Plastic production in extremely high and is on the rise.")
    with col2:
        st.image("image6.png", caption = "Recyling centers aren't able to handle all the palstic they are getting, so they are sent to the ocean." )

with tab2:
    st.markdown("<h1 style='text-align: center; color: green;'>About Us</h1>", unsafe_allow_html=True)

    st.markdown(
    """
    <div style='text-align: center; color: white;'>
        I am a 15-year-old who is currently living in Hyderabad and studying at the International School of Hyderabad. 
        I started this project because I was very passionate about waste management when I found out that my home city generated 
        the most waste per capita in India. Worst of all, there was a huge amount of trash just outside my community. It led me to 
        research and start this app where we support more sustainable recycling practices by allowing our scanner to recognize 
        whether or not a household item is recyclable.
    </div>
    """,
    unsafe_allow_html=True)

    st.markdown(
    """
    <div style='text-align: center; color: white; margin-top: 20px;'>
        We aim to make sustainable practices more accessible by giving everyone the tools to reduce their environmental footprint. 
        We believe that small actions can lead to big change, and with EcoScan, everyone can play a role in building a cleaner, 
        more sustainable future.
    </div>
    """,
    unsafe_allow_html=True)

    #st.image("Photo1.png", caption = "Photo of me.")

with tab3:
    st.markdown("<h1 style='text-align: center; color: green;'>Scanner</h1>", unsafe_allow_html=True)
    st.write("Our scan requires a photo of the image that you want to check, and then we use \n AI software to see whether the image given is recyclabe or not. This AI software has a database of over \n 10K images. ")
    st.write("Take a scan now:")
    

    with st.container():


        img = st.file_uploader('Upload your image', type=['jpg', 'png', 'jpeg'])


        analyse = st.button('Analyze')




    if analyse:
        if img is not None:


            img = Image.open(img)


            st.markdown('Image Visualization')
                

            st.image(img)


            model = models()


            res = model.predict(img)


            label = res[0].probs.top5


            conf = res[0].probs.top5conf


            conf = conf.tolist()
            st.write('Detected: ' + str(res[0].names[label[0]].title()))

            st.write('Confidence level: ' + str(int(conf[0] * 100)) + "%")
            if int(conf[0] * 100) > 65:
                st.write("This is most likely recyclable")
            else:
                st.write("We are unsure if this is recyclable or not, please try agian by uploading another picture.")
    
    #st.link_button("View Disposal Places", "https://docs.google.com/spreadsheets/d/1wKDFh_wxPoZ63M9gJNmieAprUMBADP4-2XYra1Ji3Ck/edit?gid=0#gid=0")
    option = st.selectbox("To find suitable disposal centers, please enter the city that you stay in:", ("Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat", "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad", "Ludhiana"))
    

    
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
        st.write("Currently, the app works best when you scan one item at a time for the highest accuracy.")


    q3 = st.expander("Can the app help me reduce waste?")
    with q3:
        st.write("Absolutely! The app not only identifies recyclable items but also offers tips on how to reduce waste, \n reuse materials, and make eco-friendly choices.")


    q4 = st.expander("Can the app work offline?")
    with q4:
        st.write("The app requires an internet connection to access the AI detection software. However, you can still \nbrowse recycling tips and guidelines offline.")
   
    q5 = st.expander("Does the app store my photos?")
    with q5:
        st.write("No, the app doesn’t store your photos permanently. They are only used temporarily for analysis and \nare deleted afterward to ensure your privacy.")
