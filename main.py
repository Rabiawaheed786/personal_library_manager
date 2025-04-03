import streamlit as st
import json

# Load & save library data
def load_library_data():
    try:
        with open("library_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library_data(data):
    with open("library_data.json", "w") as file:
        json.dump(data, file, indent=4)

# Initialize library data
library_data = load_library_data()

# Page Title with Emoji
st.title("📚 Personal Library Manager")

menu = st.sidebar.radio("📌 Select an option", ["📖 View Library", "➕ Add Book", "❌ Remove Book", "🔍 Search Book", "💾 Save and Exit"])

# View Library
if menu == "📖 View Library":
    st.subheader("📚 Your Library")
    if library_data:
        st.table(library_data)
    else:
        st.warning("📭 Your library is empty. Add some books!")

# Add Book
elif menu == "➕ Add Book":
    st.subheader("📥 Add a New Book")
    title = st.text_input("📘 Title")
    author = st.text_input("✍️ Author")
    genre = st.text_input("📂 Genre")
    year = st.number_input("📅 Year", min_value=1900, max_value=2100, step=1)
    read_status = st.checkbox("✅ Mark as Read")

    if st.button("➕ Add Book"):
        if title and author and genre:
            library_data.append({
                "Title": title,
                "Author": author,
                "Genre": genre,
                "Year": year,
                "Read": "✔️ Yes" if read_status else "❌ No"
            })
            save_library_data(library_data)
            st.success("🎉 Book added successfully!")
            st.rerun()
        else:
            st.error("⚠️ Please fill in all fields!")

# Remove Book
elif menu == "❌ Remove Book":
    st.subheader("🗑 Remove a Book")
    book_titles = [book["Title"] for book in library_data]

    if book_titles:
        selected_book = st.selectbox("📌 Select a book to remove", book_titles)
        if st.button("❌ Remove Book"):
            library_data = [book for book in library_data if book["Title"] != selected_book]
            save_library_data(library_data)
            st.success("🗑 Book removed successfully!")
            st.rerun()
    else:
        st.warning("📭 No books in your library. Add some books!")

# Search Book
elif menu == "🔍 Search Book":
    st.subheader("🔍 Search for a Book")
    search_term = st.text_input("🔎 Enter Title or Author")
    
    if st.button("🔎 Search"):
        results = [book for book in library_data if search_term.lower() in book["Title"].lower() or search_term.lower() in book["Author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("🚫 No books found matching your search.")

# Save and Exit
elif menu == "💾 Save and Exit":
    save_library_data(library_data)
    st.success("✅ Library data saved successfully!")
