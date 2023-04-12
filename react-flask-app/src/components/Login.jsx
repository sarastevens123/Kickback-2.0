import React, { useState } from 'react'


export default function Login(props) {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleEmailChange = (evt) => setEmail(evt.target.value);
    const handlePasswordChange = (evt) => setPassword(evt.target.value);

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
            <button type="submit">Log In</button>
        </form>

            <button onClick={props.onFormSwitch}>Register</button>

        </>
    );
}