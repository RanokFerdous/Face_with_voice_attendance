import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)





# import streamlit as st


# def style_background_home():

#     st.markdown("""
#         <style>

#             /* Home page background */
#             .stApp {
#                 background: #E8F5E9 !important;
#             }

#             /* Student and Teacher cards */
#             .stApp div[data-testid="stColumn"] {
#                 background-color: #FFFFFF !important;
#                 padding: 2.5rem !important;
#                 border-radius: 1.5rem !important;
#                 border: 1px solid #D5E8D8 !important;
#                 box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
#             }

#             /* Student and Teacher headings */
#             .stApp div[data-testid="stColumn"] h1,
#             .stApp div[data-testid="stColumn"] h2,
#             .stApp div[data-testid="stColumn"] h3 {
#                 color: #000000 !important;
#             }

#             /* Card paragraph text */
#             .stApp div[data-testid="stColumn"] p {
#                 color: #333333 !important;
#             }

#         </style>
#     """, unsafe_allow_html=True)


# def style_background_dashboard():

#     st.markdown("""
#         <style>

#             /* Dashboard background */
#             .stApp {
#                 background: #F1F8F2 !important;
#             }

#         </style>
#     """, unsafe_allow_html=True)


# def style_base_layout():

#     st.markdown("""
#         <style>

#         @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&display=swap');


#         /* Hide Streamlit default header and footer */

#             #MainMenu, footer, header {
#                 visibility: hidden;
#             }


#         /* Main content layout */

#             .block-container {
#                 padding-top: 1.5rem !important;
#                 padding-bottom: 2rem !important;
#                 max-width: 1200px;
#             }


#         /* Main heading */

#             h1 {
#                 font-family: 'Outfit', sans-serif !important;
#                 font-size: 2.5rem !important;
#                 font-weight: 700 !important;
#                 color: #000000 !important;
#                 line-height: 1.2 !important;
#                 margin-bottom: 0.5rem !important;
#             }


#         /* Secondary heading */

#             h2 {
#                 font-family: 'Outfit', sans-serif !important;
#                 font-size: 2rem !important;
#                 font-weight: 700 !important;
#                 color: #000000 !important;
#                 line-height: 1.3 !important;
#                 margin-bottom: 0.5rem !important;
#             }


#         /* Other headings */

#             h3, h4, h5, h6 {
#                 font-family: 'Outfit', sans-serif !important;
#                 font-weight: 600 !important;
#                 color: #1B1B1B !important;
#             }


#         /* Normal text */

#             p, label, li {
#                 font-family: 'Outfit', sans-serif !important;
#                 color: #333333 !important;
#                 font-size: 15px;
#             }


#         /* All buttons */

#             button {
#                 background-color: #2E7D32 !important;
#                 color: #FFFFFF !important;
#                 border: 1px solid #2E7D32 !important;
#                 border-radius: 0.7rem !important;
#                 padding: 10px 20px !important;
#                 font-family: 'Outfit', sans-serif !important;
#                 font-weight: 600 !important;
#                 transition: all 0.25s ease-in-out !important;
#             }


#         /* Secondary buttons */

#             button[kind="secondary"] {
#                 background-color: #43A047 !important;
#                 color: #FFFFFF !important;
#                 border-color: #43A047 !important;
#             }


#         /* Tertiary buttons */

#             button[kind="tertiary"] {
#                 background-color: #263238 !important;
#                 color: #FFFFFF !important;
#                 border-color: #263238 !important;
#             }


#         /* Button hover */

#             button:hover {
#                 transform: translateY(-2px);
#                 filter: brightness(0.92);
#             }


#         /* Input fields */

#             input, textarea {
#                 border-radius: 0.5rem !important;
#                 font-family: 'Outfit', sans-serif !important;
#             }


#         /* Select box */

#             div[data-baseweb="select"] {
#                 border-radius: 0.5rem !important;
#             }


#         /* Data tables */

#             [data-testid="stDataFrame"] {
#                 border-radius: 0.7rem;
#                 border: 1px solid #D5E8D8;
#                 overflow: hidden;
#             }


#         /* Links */

#             a {
#                 color: #2E7D32 !important;
#             }


#         </style>
#     """, unsafe_allow_html=True)
