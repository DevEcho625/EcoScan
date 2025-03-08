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
    option = st.selectbox("To find suitable disposal centers, please enter the city that you stay in:", ("City","Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat", "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad", "Ludhiana"))
    if option == "Mumbai":
        st.markdown(""" - Eco Recycling Ltd. \n - Address: Unit No. 422, 4th Floor, The Summit Business Bay, Andheri East, Mumbai, Maharashtra 400093 \n - Phone: +91 22 4005 2951 \n  - Types of Waste Collected: Electronic waste (e-waste), including discarded electronic devices and components.""")
    if option == "Delhi":
        st.markdown(""" - Name: Greenobin Recycling Pvt. Ltd.\n - Address: B-50, Mayapuri Industrial Area Phase I, New Delhi, Delhi 110064\n - Phone: +91 11 2811 6222\n - Types of Waste Collected: Paper and cardboard waste, confidential document destruction, and recycling services.\n """)
    if option == "Bengaluru":
        st.markdown(""" -  Name: Saahas Zero Waste\n - Address: #17, 35th Main, 6th Cross, BTM Layout 2nd Stage, Bengaluru, Karnataka 560068\n - Phone: +91 80 4168 9889\n - Types of Waste Collected: Municipal solid waste, dry waste (plastic, paper, metal), wet waste (organic/biodegradable), and e-waste.\n\n""")

    if option == "Hyderabad":
        st.markdown(""" - Name: Recykal\n - Address: Hyderabad, Telangana\n - Phone: Information not available\n - Types of Waste Collected: Plastic waste, paper waste, electronic waste, and metal waste. """)

    if option == "Ahmedabad":
        st.markdown(""" - Name: Ecoline\n - Address: Plot No. 47, GIDC Estate, Phase-1, Vatva, Ahmedabad, Gujarat 382445\n - Phone: +91 79 2583 3835\n - Types of Waste Collected: Industrial hazardous waste, chemical waste, and contaminated soil.""")

    if option == "Chennai":
        st.markdown("""- Name: Greater Chennai Corporation - Solid Waste Management\n - Address: Ripon Building, Chennai, Tamil Nadu 600003\n - Phone: +91 44 2530 1421\n - Types of Waste Collected: Municipal solid waste, including biodegradable (organic) and non-biodegradable (plastic, paper, metal) waste.""")

    if option == "Kolkata":
        st.markdown("""- Name: Kolkata E-waste Management\n - Address: 14B, Camac Street, 3rd Floor, Kolkata, West Bengal 700017\n - Phone: +91 33 2282 3744\n - Types of Waste Collected: Electronic waste (e-waste), including computers, mobile phones, and household appliances.""")

    if option == "Surat":
        st.markdown("""- Name: Surat Green Precast Pvt. Ltd.\n - Address: Plot No. 168, GIDC Estate, Pandesara, Surat, Gujarat 394221\n - Phone: +91 261 289 0770\n - Types of Waste Collected: Construction and demolition waste, concrete debris, and industrial waste.""")

    if option == "Pune":
        st.markdown(""" - Name: SWaCH Pune Seva Sahakari Sanstha\n - Address: Office No. 5, 2nd Floor, Gopal House, Katraj, Pune, Maharashtra 411046\n - Phone: +91 20 2432 8080\n - Types of Waste Collected: Municipal solid waste, dry waste (plastic, paper, metal), wet waste (organic/biodegradable), and e-waste.""")

    if option == "Jaipur":
        st.markdown(""" - Name: Jaipur Biofertilizers\n - Address: G-1/446, RIICO Industrial Area, Sitapura, Jaipur, Rajasthan 302022\n - Phone: +91 141 277 1844\n - Types of Waste Collected: Organic waste, agricultural waste, and biodegradable waste for composting.""")

    if option == "Lucknow":
        st.markdown("""- Name: Eco Wise Waste Management Pvt. Ltd.\n - Address: C-123, Talkatora Industrial Area, Lucknow, Uttar Pradesh 226011\n - Phone: +91 522 266 1234\n - Types of Waste Collected: Municipal solid waste, dry waste (plastic, paper, metal), and wet waste (organic/biodegradable).""")
    
    if option == "Kanpur":
        st.markdown(""" - Name: Kanpur Waste Management Pvt. Ltd.\n - Address: D-1, UPSIDC Industrial Area, Rooma, Kanpur, Uttar Pradesh 209402\n - Phone: +91 512 393 7000\n - Types of Waste Collected: Industrial hazardous waste, biomedical waste, and chemical waste.""")
    
    if option == "Nagpur":
        st.markdown("""- Name: Hanjer Biotech Energies Pvt. Ltd.\n - Address: Survey No. 37, Village - Bhandewadi, Kamptee Road, Nagpur, Maharashtra 440026\n - Phone: +91 712 264 0666\n - Types of Waste Collected: Municipal solid waste, organic waste, and recyclable materials.""")

    if option == "Indore":
        st.markdown("""- Name: Aasra Waste Management Pvt. Ltd.\n - Address: Plot No. 25, Scheme No. 78, Part II, Vijay Nagar, Indore, Madhya Pradesh 452010\n - Phone: +91 731 255 5525\n - Types of Waste Collected: Municipal solid waste, dry waste (plastic, paper, metal), and wet waste (organic/biodegradable).""")

    if option == "Bhopal":
        st.markdown("""- Name: Bhopal Municipal Solid Waste Management Pvt. Ltd.\n - Address: Near Adampur Chhawni, Bhanpur, Bhopal, Madhya Pradesh 462037\n - Phone: +91 755 273 0900\n - Types of Waste Collected: Municipal solid waste, including biodegradable and non-biodegradable waste.""")

    if option == "Visakhapatnam":
        st.markdown("""- Name: Green Waves Environmental Solutions\n - Address: Plot No. 19, APIIC Industrial Park, Gambheeram, Anandapuram, Visakhapatnam, Andhra Pradesh 531163\n - Phone: +91 891 286 6444\n - Types of Waste Collected: Electronic waste (e-waste), plastic waste, and metal waste.""")

    if option == "Patna":
        st.markdown("""- Name: Patna Municipal Corporation - Solid Waste Management\n - Address: New Market Station Road, Patna, Bihar 800001\n - Phone: +91 612 221 9504\n - Types of Waste Collected: Municipal solid waste, biodegradable waste, and recyclable materials.""")

    if option == "Vadodara":
        st.markdown("""- Name: Enviro Infrastructure Company Ltd.\n - Address: Plot No. 612, GIDC Estate, Waghodia, Vadodara, Gujarat 391760\n - Phone: +91 2668 262 200\n - Types of Waste Collected: Hazardous waste, industrial waste, and biomedical waste.""")

    if option == "Ghaziabad":
        st.markdown("""- Name: Ghaziabad Nagar Nigam - Solid Waste Management\n - Address: Navyug Market, Ghaziabad, Uttar Pradesh 201001\n - Phone: +91 120 279 1418\n - Types of Waste Collected: Municipal solid waste, dry waste (plastic, paper, metal), and wet waste (organic/biodegradable).""")

    if option == "Ludhiana":
        st.markdown("""Name: Ludhiana Municipal Corporation - Waste Management\n - Address: Zone D, Near Guru Nanak Bhawan, Ludhiana, Punjab 141001\n - Phone: +91 161 274 0101\n - Types of Waste Collected: Municipal solid waste, plastic waste, and e-waste.""")

    if option == "Tirupati":
        st.markdown("""- Name: Tirupati Municipal Corporation - Waste Management\n - Address: Municipal Office, Tirupati, Andhra Pradesh 517501\n - Phone: +91 877 222 5134\n - Types of Waste Collected: Municipal solid waste, organic waste, and plastic recycling.""")


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
