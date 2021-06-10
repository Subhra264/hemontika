import { useState } from "react";
import Form from "../common/Form/Form";
import authenticate from '../../utils/authenticate';

export default function LogIn(props) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');

    const changeUsername = (ev) => {
        setUsername(ev.target.value);
    };

    const changePassword = (ev) => {
        setPassword(ev.target.value)
    };

    const changeEmail = (ev) => {
        setEmail(ev.target.value);
    };

    const logIn = async (ev) => {
        ev.preventDefault();

        const response = await authenticate(`/api-auth/login`, {
            username,
            email,
            password
        });

        console.log(username, email, password);
        console.log(response);
    }
    
    const formProps = {
        fields: {
            username: {
                type: 'text',
                required: true,
                onChange: changeUsername
            },
            password: {
                type: 'password',
                required: true,
                onChange: changePassword
            },
            email: {
                type: 'email',
                required: true,
                onChange: changeEmail
            }
        },
        onSubmit: logIn
    };

    return (
        <div className='form-container log-in'>
            <div className='form-title'>Log In</div>
            <Form {...formProps} />
        </div>
    );
}