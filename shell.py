import streamlit as st
import graphviz

graph = graphviz.Digraph()

graph.edge("Jira", "GitHub")
graph.edge("Jira", "Slack")
graph.edge("Jira", "Sheets")

st.graphviz_chart(graph)