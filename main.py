import streamlit as st

from consumption_outputs import ConsumptionOutput

# Create an instance of ConsumptionOutput
consumption_output = ConsumptionOutput()

def app():
    st.title("Welcome to Reality AI! Here is your weekly parental control analysis")

    analysis_results, recommendations = consumption_output.run_analysis()


    # Display recommendations
    st.header("Recommendations + Action Items")
    for recommendation in recommendations:
        st.write("⚠️⚠️⚠️⚠️")
        st.write(recommendation)
        st.write("---------------------------------")

if __name__ == "__main__":
    app()
