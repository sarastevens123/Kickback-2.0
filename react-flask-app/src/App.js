import React, { useState, useEffect } from 'react';
import LoginForm from './components/LoginForm'
import './App.css';

export default function App() {
  const adminUser = {
    email: "admin@admin.com",
    password: "admin123"
  }
  


  const [user, setUser] = useState({email:"", password:""});
  const [error, setError] = useState("");

  const Login = details => {
    console.log(details);

    if (details.email == adminUser.email && details.password == adminUser.password) {
      console.log("Logged In");
      setUser({
        name: details.name,
        password: details.password
      });
    } else {
        console.log("Details do not match!");
        setError("Details do not match!")
           }
  }

  const handleLogin = evt => {
    evt.preventDefault()
    const userJson = {'email': email, 'password': password };
    if (email === "" || password === "") {
      alert("Please enter required information.")
    } else {
      fetch('/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(userJson)
      })
      .then((response) => response.json())
      .then((userData) => {
        if (userData==="Incorrect Password" || userData) {
          alert(userData);
        } else {
          setUser(userData);
          confirmLogin(user);
        }
      })
    }
    };


  const Logout = () => {
    setUser({ email:"", password:""});
    console.log("logged out");
  }

  return (
    <div className="App">
      {(user.email != "") ? (
        <div className="welcome">
          <h2>Welcome to Kickback!</h2>
          <button onClick={Logout}>Logout</button>
          </div>

      ) : (
        <LoginForm Login={Login} error ={error}/>
      )}
    </div>
  )}