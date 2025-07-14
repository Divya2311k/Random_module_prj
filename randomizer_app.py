import streamlit as st
import random

st.set_page_config(page_title="🎲 Randomizer Playground", layout="centered")

st.title("🎲 Randomizer Playground")
st.markdown("Explore Python's built-in `random` module interactively.")

# Sidebar for selection
option = st.sidebar.selectbox(
    "Choose an operation",
    [
        "Random Integer",
        "Random Float",
        "Shuffle a List",
        "Pick One Item",
        "Sample Multiple Items",
        "Normal Distribution",
        "Uniform Distribution"
    ]
)

# Random Integer
if option == "Random Integer":
    st.header("🔢 Random Integer Generator")
    a = st.number_input("Min value", value=1)
    b = st.number_input("Max value", value=10)
    if st.button("Generate"):
        st.success(f"🎯 Result: {random.randint(int(a), int(b))}")

# Random Float
elif option == "Random Float":
    st.header("🎯 Random Float between [0.0, 1.0)")
    if st.button("Generate"):
        st.success(f"💧 Float: {random.random():.5f}")

# Shuffle
elif option == "Shuffle a List":
    st.header("🔀 Shuffle a List")
    input_text = st.text_input("Enter comma-separated items", "apple, banana, cherry, date")
    if st.button("Shuffle"):
        items = [x.strip() for x in input_text.split(",")]
        random.shuffle(items)
        st.success(f"Shuffled List: {items}")

# Pick One
elif option == "Pick One Item":
    st.header("🎯 Random Choice from List")
    input_text = st.text_input("Enter comma-separated items", "red, blue, green")
    if st.button("Pick"):
        items = [x.strip() for x in input_text.split(",")]
        st.success(f"Picked: {random.choice(items)}")

# Sample
elif option == "Sample Multiple Items":
    st.header("📦 Random Sample (No Duplicates)")
    input_text = st.text_input("Enter comma-separated items", "dog, cat, fish, bird")
    k = st.slider("How many to pick?", min_value=1, max_value=5, value=2)
    if st.button("Sample"):
        items = [x.strip() for x in input_text.split(",")]
        if len(items) >= k:
            sample = random.sample(items, k)
            st.success(f"Sampled Items: {sample}")
        else:
            st.warning("Need at least k items to sample from.")

# Normal Distribution
elif option == "Normal Distribution":
    st.header("📊 Generate Random Number (Normal Distribution)")
    mu = st.number_input("Mean (μ)", value=0.0)
    sigma = st.number_input("Standard Deviation (σ)", value=1.0)
    if st.button("Generate"):
        val = random.gauss(mu, sigma)
        st.success(f"Generated Value: {val:.4f}")

# Uniform Distribution
elif option == "Uniform Distribution":
    st.header("📈 Generate Random Float (Uniform Distribution)")
    a = st.number_input("Min value", value=0.0)
    b = st.number_input("Max value", value=10.0)
    if st.button("Generate"):
        val = random.uniform(a, b)
        st.success(f"Uniform Value: {val:.4f}")
