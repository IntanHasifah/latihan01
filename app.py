import stream.lit as st

page=[
    st.Page(page="page/pages1.py", title="Home", icon="🏘"),
    st.Page(page="page/pages2.py", title="Visualisasi Data", icon="📈"),
    st.Page(page="page/pages3.py", title="Settings", icon="🎲"), 
]

pg = st.navigation(
    page, 
    positon="sidebar",
    expanded=True
)

pg.run()