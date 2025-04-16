import streamlit as st
from rdflib import Graph
from streamlit_agraph import TripleStore, agraph
from streamlit_extras.card import *
import streamlit.components.v1 as components

title = st.text_input("Subreddit Name", "r/")


# graph = Graph()
# graph.parse("http://www.w3.org/People/Berners-Lee/card")
# store = TripleStore()

# for subj, pred, obj in graph:
#     store.add_triple(subj, pred, obj, "")
    
# agraph(list(store.getNodes()), list(store.getEdges()),)

col1, col2, col3, col4, col5 = st.columns(5)

col1 = card(
        title="Hello World!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
        key='col1'
    )

col2 = card(
        title="Hello World!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
        key='col2'
    )

col3 = card(
        title="Hello World!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
        key='col3'
    )

col4 = card(
        title="Hello World!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
        key='col4'
    )

col5 = card(
        title="Hello World!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
        key='col5'
    )