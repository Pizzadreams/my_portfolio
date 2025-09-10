import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention
# from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain
import base64
import pandas as pd

resume = "./docs/Redacted_Resume_For_Portfolio.pdf"
BG_IMG = "./assets/midnight_city.png"
# Load CSS file
with open("./styles/style.css") as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

def rs(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    no_comma = b.replace(',', '')
    st.markdown(no_comma)

def add_bg_img(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
            <style>
            .stApp {{
                background-image: url(data:image/png;base64,{encoded_string.decode()});
                background-size: cover;
            }}
            </style>
        """,
        unsafe_allow_html=True
    )

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''
        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://img.icons8.com/ios-filled/100/3355B9/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/3355B9/github.png",
                "email": "https://img.icons8.com/ios-filled/100/3355B9/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html

def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="View PDF here"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

def display_resume():
    # st.markdown(pdf_link(resume_url, "**Resume**"), unsafe_allow_html=True)
    show_pdf(resume)
    with open(resume, "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="Your_Resume.pdf",
            mime="application/pdf"
        )

def overview_streamlit_links():
    st.subheader("[Learn about Streamlit here](https://docs.streamlit.io/library/get-started)")

def pizza_data_generator_display():
    data = pd.read_excel('./projects_data/pizza_data.xlsx')
    col1, col2, col3 = st.columns([4,2,2])

    with col1:
        st.subheader('Raw Data')
        st.dataframe(data)
        st.markdown("&nbsp;")

    with col2:
        st.subheader('Filter Data')
        st.write('You can filter the data based on pizza size and style using the widgets below.')

        # Create filters
        size_filter = st.selectbox('Select Pizza Size:', ['sm', 'md', 'lg'])
        style_filter = st.selectbox('Select Pizza Style:', ['NY', 'Sicilian', 'Chicago', 'Detroit', 'Deep Dish'])

        # Apply filters
        filtered_data = data[(data['Pizza Size'] == size_filter) & (data['Pizza Style'] == style_filter)]

        # Display filtered data
        st.write(f"Filtered Data for {size_filter} {style_filter} Pizzas:")
        st.dataframe(filtered_data)
        st.markdown("&nbsp;")

    with col3:
        # Basic statistics
        st.subheader('Basic Statistics')
        st.write('Here are some basic statistics about the pizza data:')
        st.write(f"Number of Pizza Places: {data['Place Name'].nunique()}")
        st.write(f"Number of Customers: {data['Customer'].nunique()}")
        st.write(f"Total Number of Records: {len(data)}")

def display_let_it_rain_pizza():
    rain(
        emoji="🍕",
        font_size=50,
        falling_speed=7,
        animation_length="2",
    )

def display_contact_me():
    st.title("Contact Me")

    # Create a form #
    st.header("# This is a Work In Progress")
    with st.form(key='contact_form'):
        # Add a text input for the name
        name = st.text_input("Your Name")

        # Add a text input for the email
        email = st.text_input("Your Email")

        # Add a text area for the message
        message = st.text_area("Message")

        # Add a submit button
        submit_button = st.form_submit_button(label='Submit')

    # Handle form submission - TODO
    if submit_button:
        st.success("Message sent! We'll get back to you soon.")


def resources():
    # https://uigradients.com/
    TODO

def render_content():
    add_bg_img(BG_IMG)
    with st.sidebar:
        choose = option_menu(
            "Andrew", 
            ["About Me", "Overview", "Experience", "Relevant Skills", "Projects", "Resume", "Contact"],
            icons=['person fill', 'globe', 'clock history', 'tools', 'book half', 'clipboard', 'phone'],
            menu_icon="", 
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#2B2E47"},
                "icon": {"color": "blue", "font-size": "20px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#808080"},
                }
            )

        linkedin_url = "Your_LinkedIn_URL"
        github_url = "https://github.com/Pizzadreams"
        email_url = "mailto:Your_Email@gmail.com"
        with st.container():
            l, m, r = st.columns((0.11,2,0.1))
            with l:
                st.empty()
            with m:
                st.markdown(
                    social_icons(34, 34, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                    unsafe_allow_html=True)
            with r:
                st.empty()


    if choose == "About Me":
        with st.container():
            st.title("About Me")
            st.subheader("Customer Support & IT Professional")
            st.markdown("""<div class="custom-font">Welcome to my portfolio. I am an customer-focused IT professional who thrives on collaborative enviornments and continuous learning. Currently, 
            I have been working on couple of a small projects, one involving app development, and another as a dashboard for bug tracking. I enjoy learning about different cultures, languages and am eager
             leverage and contribute my interpersonal and technical skills in an inclusive environment.
            """, unsafe_allow_html=True)
            st.markdown("""<div class="custom-font"> Feel free to check out my projects! </div>""", unsafe_allow_html=True)
    elif choose == "Overview":   
        st.title("Overview")
        st.markdown("""
            Originally conceived as a single project, I soon discovered some features that Streamlit has to offer, especially when it comes to the visualization of data.
            While Streamlit is primarily designed for web application dashboarding, its extensive features contribute to a more visually appealing interface that is lightweight.

            With Python and Streamlit, I have decided to transform this single project into my portfolio. 
            It will serve as a repository for showcasing my personal projects, demonstrating my skills, and building credibility. Furthermore, 
            if after this endeavor, I plan to offer my code as open-source with hopes to encourage other learners to pursue their educational journeys in a similar way.
        """)
        overview_streamlit_links()

    elif choose == "Experience": 
        st.title("Experience")
        with st.container():
            st.subheader("Software Engineer")
            st.write("*November 2021 to July 2023*")
            st.markdown("""
                - Assess business requirements discussed in 3-Amigos/Triage to prepare testing scenarios
                - Test tracking utilized within Jira and qTest to centralize management and support Agile
                - QA Automation with Cypress as a tool for frontend integration and unit testing
                - Practice Behavior-Driven Development (BDD) methodology to create concise code and meet requirements
                - Add documentation and knowledge transfer material during software upgrade transition
            """)
            st.markdown("""
                `JavaScript` `Cypress` `qTest`
            """)

            st.subheader("SDET Intern")
            st.write("*May 2021 to November 2021*")
            st.markdown("""
                - Analyze and develop test scenarios after review of application and business specifications
                - Prepare Manual and Automated testing scenarios for system design of an application
                - Tracked tasks and tests within Jira and Agile for project management and delivery 
                - Execution of Smoke, Functional, and Regression test suite to test software functionality
                - Mobile Automation using Appium and QAF framework for both iOS and Android support
            """)
            st.markdown("""
                `Android Studio ` `Appium ` `Java 1.8 SE ` `Sauce Labs ` `TestNG ` `QMetry ` `XCode v12.4`
            """)

            st.subheader("Enterprise Support Technician II")
            st.write("*April 2019 to August 2020*")
            st.markdown("""
                - Resolved IT-related issues for a global network of 2,000 end-users in 40 locations
                - Mentored new Enterprise Support technicians by providing guidance and feedback/metrics
                - Prioritized and established process and procedures in accordance with company policy using Agile
                methodology
                - Maintaining accurate documentation for systems, processes, and troubleshooting procedures
            """)
            st.markdown("""
                `Active Directory ` `Citrix Director` `LANDesk Management ` `Pulse Secure`
            """)

            st.subheader("Cyber Security Analyst Associate")
            st.write("*June 2018 to February 2019*")
            st.markdown("""
                - Provided Tier 2 Support to meet deadlines and complying with established Service-Level Agreements
                - Documented security-related processes and procedures ensuring 100% accuracy
                - Managed accounts completing all security-related requests submitted by the client
                - Performed daily and weekly updates on various tools and systems to stay secured and compliant
                - Communicated with different teams to mitigate cybersecurity-related incidents
            """)

            st.subheader("Software/Application Development Intern")
            st.write("*June 2017 to August 2017*")
            st.markdown("""
                - Developed GUI-based code for an internal employee/project management system
                - Utilized Node and Git for server management and version control
                - Learned Agile Development acquiring principles and values for effective collaboration
                - Experienced development with ServiceNow resolving tasks for the OCIO self-service portal
            """)

            st.markdown("""
                `Angular` `HTML and CSS ` `Git ` `Java ` `Node ` `SQL`
            """)

    elif choose == "Relevant Skills":
            st.title("Relevant Skills")
            rs("Soft Skills", """
                - Ambitious learning behavior
                - Consistency in mood
                - Openminded and responsive to
                conversation
                - Motivated to inspire and build
                relationships
                - Encouraged by feedback
                - Committed to assignments and
                task"""
            )
            rs("Programming Languages and Frameworks", """
                - Cypress
                - JavaScript
                - Python
            """)

            rs("Tools & Technologies", """
                - Active Directory
                - Appium Desktop
                - Citrix Director
                - LANDesk Management
                - Pulse Secure
                - qTest
                - Sauce Labs
            """)

            rs("Version Control", """
                - Bitbucket
                - GitLab
            """)

            rs("Methodologies", """
                - Agile
                - Waterfall
            """)

            rs("Certifications", """
                - Programming Foundations (Coursera/Duke University)
                - Introduction to SQL (Coursera/University of Michigan)
                - Front End Web Development (Coursera/Hong Kong University of Science and Technology)
                - CompTIA Network+ (N10-007) - September 2019
                - CompTIA Healthcare IT Technician
            """)
    elif choose == "Resume":
        display_resume()
    elif choose == "Projects":
        # Create section for Projects
        #st.write("---")
        st.title("Projects")
        with st.container():
            st.header("#Spyntax")
            st.write("*A project using the Turtle library.*")
            st.markdown("""
                A captivating rainbow "pinwheel". This composition of concentric shapes, each adorned with the vivid colors of the rainbow to create a stimulative display.
            """)
            mention(label="Spyntax Repo", icon="github", url="https://github.com/Pizzadreams/PythonLearning/blob/main/PythonProjects/Turtle/spyntax.py",)
            
            show_spyntax_project = st.toggle("Click here to view 🌀 Spyntax")
            video_width = 800
            video_height = 700
            if show_spyntax_project:
                with st.container():
                    st.info("A captivating rainbow 'pinwheel' using Turtle.")
                    video_file = open("./assets/spyntax.mp4", "rb").read()

                    st.markdown(
                        f"""
                        <style>
                        video {{
                            width: {video_width}px;
                            height: {video_height}px;
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True
                    )
                    st.video(video_file, start_time=1)

        with st.container():
            st.header("#Pizza Data Generator")
            st.write("*Pizza Pie Data Delight - A pandas project using faker for data generation.*")
            st.markdown("""
                A project for me to gain experience with data analysis using the Pandas library in Python. 
                By creating and manipulating pizza-related data, I can practice various operations such as DataFrame creation, sorting, 
                filtering, and exporting data to Excel files.
            """)
            mention(label="Pizza Data Generator Repo", icon="github", url="https://github.com/Pizzadreams/PythonLearning/tree/main/PythonProjects/PizzaPieDataDelight",)
            
            show_pizza_project = st.toggle("Click to view the 🍕 project")
            if show_pizza_project:
                pizza_data_generator_display()

                show_raining_pizzas = st.toggle("Want more 🍕?")
                if show_raining_pizzas:
                    display_let_it_rain_pizza()
    elif choose == "Contact":
        display_contact_me()