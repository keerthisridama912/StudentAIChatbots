import streamlit as st
import ollama
import chromadb

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Student AI Chatbot",
    page_icon="🎓",
    layout="centered"
)

# -------------------------------
# Title
# -------------------------------
st.title("🎓 Student AI Chatbot")
st.write("Ask me about Java, Python, exams, study, interviews, or college.")

# -------------------------------
# ChromaDB Setup
# -------------------------------
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="student_knowledge"
)

# -------------------------------
# Student Knowledge
# -------------------------------
documents = [
    "Java is a programming language used to create applications and software.",
    "Python is a simple and beginner-friendly programming language.",
    "DSA means Data Structures and Algorithms.",
    "DBMS means Database Management System.",
    "An internship gives students practical experience.",
    "A resume contains education, skills, projects, certificates and achievements.",
    "Students should practice coding regularly to improve programming skills.",
    "For exams, students should understand concepts and revise important questions.",
    "An interview tests communication, technical knowledge and problem-solving skills."
]

# -------------------------------
# Ollama Embedding Function
# -------------------------------
def get_embedding(text):
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )

    return response["embedding"]


# -------------------------------
# Add Documents to ChromaDB
# -------------------------------
if collection.count() == 0:

    embeddings = []

    for document in documents:
        embedding = get_embedding(document)
        embeddings.append(embedding)

    collection.add(
        ids=[f"doc_{i}" for i in range(len(documents))],
        documents=documents,
        embeddings=embeddings
    )


# -------------------------------
# User Input
# -------------------------------
question = st.text_input(
    "💬 Ask your question:"
)


# -------------------------------
# Generate Answer
# -------------------------------
if question:

    try:

        # Create embedding for question
        question_embedding = get_embedding(question)

        # Search ChromaDB
        results = collection.query(
            query_embeddings=[question_embedding],
            n_results=3
        )

        # Get relevant documents
        retrieved_docs = results["documents"][0]

        # Combine documents
        context = "\n".join(retrieved_docs)

        # -------------------------------
        # Prompt for Ollama
        # -------------------------------
        prompt = f"""
You are a helpful Student AI Assistant.

Answer the student's question in simple and easy English.

Use the following knowledge:

{context}

Student Question:

{question}

Give a clear and beginner-friendly answer.
"""

        # -------------------------------
        # Generate AI Answer
        # -------------------------------
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response["message"]["content"]

        # -------------------------------
        # Display Answer
        # -------------------------------
        st.subheader("🤖 AI Answer")
        st.write(answer)

    except Exception as e:

        st.error("Something went wrong.")

        st.write("Error:")
        st.code(str(e))

        st.info(
            "Make sure Ollama is running and both "
            "llama3.2 and nomic-embed-text are installed."
        )