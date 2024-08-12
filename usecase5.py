
import streamlit as st
import streamlit as st

st.set_page_config(
    
    page_title= "Saudi Arabia Used Cars",
    page_icon= "👩🏻‍💻",
)

st.image("header.png", use_column_width=True)



st.title("Jobs and much more around 👩🏻‍💻.")
st.markdown("""In the heart of the digital age, jobs increase at times and decrease at other times. The salary fluctuates based on several factors, including years of experience, and we he right job for me? Ok where? Which region accounts for a large share of jobs? What is the average salary limit for recent graduates?""")
st.markdown("""Let's look together at what the job entails !""")


st.markdown("""Let's ask some questions so we can have a little knowledge about it """)
st.markdown("---")



st.subheader(" What proportion of job postings is attributed to each region within the kingdom?")
st.image("jobVSregion.png", use_column_width=True)
#st.image(jobVSregion.png, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.write(
    """
The region with the largest share of jobs is Riyadh, followed by many regions, the same as Makkah Al-Mukarramah and Al-Sharqiya, respectively.
"""
)

##################################


st.markdown("---")

st.subheader(" Is there a gender preference indicated in the job postings?")
st.image("count_gender.png", use_column_width=True)


st.write("""
The graph shows that there is no preference in the first place for a specific gender, but some advertisements still prefer males.""")


#################################!SECTION


st.markdown("---")

st.subheader(" What is the expected salary range for fresh graduates?")
st.image("salary_fresh.png", use_column_width=True)


st.write("""
From what is shown in the chart, we expect the salary limits for recent graduates with less than three years of experience to range from 4,000 to 9,000. """)


################################!SECTION


st.markdown("---")

st.subheader(" Are job opportunities predominantly targeted at individuals with experience, or is there room for fresh graduates as well?")
st.image("exp_jobposting.png", use_column_width=True)


st.write("""
There is a higher demand for fresh graduates than for those with experience""")

st.markdown("---")


##################!SECTION


st.subheader("Which sector creates more jobs?")
st.image("company_type.png", use_column_width=True)


st.write("""
The private sector is higher in job posting""")

st.markdown("---")


#####!SECTION




st.write("""
Based on the data, Riyadh provides many opportunities, and recent graduates are highly attracted by business owners
Now you know a lot about jobs, start looking for work now ...""")


