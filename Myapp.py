import streamlit as st
import pandas as pd


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Built By Harshit Trehan"""

	st.title("The Medicinal Use Detector App")
	st.subheader("Built By Harshit And Gautam")
	html_temp = """
							<div style="background-color:#00FF00 ;padding:10px">
							<h1 style="color:white;text-align:center;">Lyrics Generator App</h1>
							</div>
							"""
	st.markdown("<span style=“background-color:#121922”>",unsafe_allow_html=True)

	from PIL import Image
	img = Image.open("medicine.jpg")
	st.image(img, width=400)
	menu = ["Home","About","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)
 
	if choice == "Home":
		st.subheader("Home")
		st.info("This is a medicinal use detection app aiming to tell the functions of the given medicine")
		st.success("Please Sign Up For Accessing the App")
	
	elif choice == "About":
		st.subheader("About")
		st.text("This is a Medicinal Use Detector App which helps in knowing the fuctiions and uses of the medicines by generating APIs from google. As many of the medicines are left unused at home due to lack of knowledge of their purpose. This app helps in making use of these medicines")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))
				st.balloons()

				task = st.selectbox("Task",["Add Post","Student","Faculty"])
				if task == "Add Post":
					st.subheader("Add Your Post")

				elif task == "Student":
					st.subheader("Student")
				elif task == "Faculty":
					st.subheader("Faculty")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')
		st.selectbox("Your Gender", ["Male", "Female", "Others"])
		Age=st.text_input("Age")

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")
			st.balloons()



if __name__ == '__main__':
	main()

  
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
