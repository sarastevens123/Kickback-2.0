import React, { useState }  from 'react';

function LoginForm({ Login, error }) {
    const [details, setDetails] = useState({email:"", password:""});

    const submitHandler = evt => {
        evt.preventDefault();

        Login(details);
    }
    return (
        <form onSubmit={submitHandler}>
            <div className="form-inner">
                <h2>Login</h2>
                {(error != "") ? ( <div classname="error">{error}</div>) : ""}
                <div className="form-group">
                    <label htmlFor="email">Email:</label>
                    <input type="text" name="email" id="email" onChange={evt => setDetails({...details, email: evt.target.value})}value={details.email}/>
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password:</label>
                    <input type="password" name="password" id="password" onChange={evt => setDetails({...details, password: evt.target.value})}value={details.password}/>
                </div>
                <input type="submit" value="LOGIN" />
            </div>
        </form>
    )}

    export default LoginForm