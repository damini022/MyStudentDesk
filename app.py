import streamlit as st
from database import connect_db, create_table

# create table
create_table()

st.title("🎓 Student Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Student", "View Students", "Update Student", "Delete Student"]
)

# ADD STUDENT
if menu == "Add Student":
    st.subheader("Add Student")

    name = st.text_input("Name")
    roll = st.text_input("Roll Number")
    course = st.text_input("Course")
    marks = st.number_input("Marks", 0, 100)

    if st.button("Add"):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (name, roll_no, course, marks) VALUES (?, ?, ?, ?)",
            (name, roll, course, marks)
        )
        conn.commit()
        conn.close()
        st.success("Student Added Successfully ✅")

# VIEW STUDENTS
elif menu == "View Students":
    st.subheader("All Students")

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()

    st.table(data)

# UPDATE STUDENT
elif menu == "Update Student":
    st.subheader("Update Student Marks")

    sid = st.number_input("Student ID", step=1)
    new_marks = st.number_input("New Marks", 0, 100)

    if st.button("Update"):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "UPDATE students SET marks=? WHERE id=?",
            (new_marks, sid)
        )
        conn.commit()
        conn.close()
        st.success("Student Updated ✅")

# DELETE STUDENT
elif menu == "Delete Student":
    st.subheader("Delete Student")

    sid = st.number_input("Student ID", step=1)

    if st.button("Delete"):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE id=?", (sid,))
        conn.commit()
        conn.close()
        st.warning("Student Deleted ❌")


