import streamlit as st

# Set page title
st.set_page_config(page_title="Poaster Prototype", page_icon="🪧")
st.title("🪧 Poaster - AI Assistant Prototype")

# Output from sidebar outline generator
# content_type_container = st.container()
# content_text_container = st.empty()
outline_proposal = st.text_area(
    "Outline Proposal:",
    """    - Bullet Point 1
    - Bullet Point 2
    - Bullet Point 3
    - Bullet Point 4
    - Bullet Point 5"""
)
st.button("Generate Substack Post")

# Divider between outline proposal and actual content output
st.divider()

# Output from actual content generated
st.write("Here is your Substack blog:")
output_container = st.container(border=True, height=250)
output_container.write(
    """
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. Lots of text. 
    """
)


# Sidebar outline form callback
def form_callback():
    if not st.session_state.content_type or not st.session_state.content_text:
        print("Fields cannot be empty.")
    else:
        print("Alr you good.")
    #content_type_container.container(st.session_state.content_type)
    #content_text_container.text(st.session_state.content_text)

# Sidebar UI
with st.sidebar:

    st.header("Automation for Leaders We Deserve Content", divider="rainbow")

    with st.form(key='sidebar_form'):

        st.selectbox(
            "I am looking to write a...",
            ("Substack blog", "Tweet"),
            index=None,
            placeholder="Select...",
            key="content_type"
        )

        st.text_area("about...", key="content_text")

        st.form_submit_button(label='Generate Outline', on_click=form_callback)