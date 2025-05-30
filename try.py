import streamlit as st

# Initialize session state to track if user made a selection
if 'selection_made' not in st.session_state:
    st.session_state.selection_made = False

st.subheader("Google News Selected")
st.markdown("**Note :- Select a time range**")

# Selectbox
options = st.selectbox(
    "Choose time range:",
    ['Select...', '1 month', '3 months', '6 months'],
    key="time_range"
)

# Check if user made a selection (not first load)
if options != 'Select...':
    st.session_state.selection_made = True

# Only run if user has made a valid selection
if st.session_state.selection_made and options != 'Select...':
    months = int(options.split()[0])
    st.success(f"✅ Running for {months} month(s)")
    # Call your main function here
    # MainRun(months)
else:
    st.warning("👈 Please select a valid time range.")
