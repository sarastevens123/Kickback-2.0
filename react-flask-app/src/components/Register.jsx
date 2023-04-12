import React, { useState } from 'react'

export default function Register (props) {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [fname, setFname] = useState('');
    const [lname, setLname] = useState('');
    

    const handleSubmit = (evt) => {
        evt.preventDefault();
        console.log(email);
    }



    return (
        <>
        <form>
            <label htmlFor="email">email</label>
            <input type="email" value={email} onChange={(evt) => setEmail(evt.target.value)} />
            <label htmlFor="password">password</label>
            <input type="password" value={password} onChange={(evt) => setPassword(evt.target.value)} />
            <label htmlFor="fname">first name</label>
            <input type="fname" value={fname} onChange={(evt) => setFname(evt.target.value)} />
            <label htmlFor="lname">last name</label>
            <input type="lname" value={lname} onChange={(evt) => setLname(evt.target.value)} />
            
            <button onClick={props.onFormSwitch}>Register Account</button>
            
        </form>

            

        </>
    );
}