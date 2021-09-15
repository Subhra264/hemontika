import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Form, { FormProps } from '../Form/Form';
import authenticate from '../../utils/authenticate';

export default function LogIn(props: any) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [error, setError] = useState('');

    const changeUsername: React.ChangeEventHandler = (ev: React.ChangeEvent) => {
        setUsername((ev.target as HTMLInputElement).value);
    };

    const changePassword: React.ChangeEventHandler = (ev: React.ChangeEvent) => {
        setPassword((ev.target as HTMLInputElement).value);
    };

    const changeEmail: React.ChangeEventHandler = (ev: React.ChangeEvent) => {
        setEmail((ev.target as HTMLInputElement).value);
    };

    const logIn: React.MouseEventHandler = async (ev: React.MouseEvent) => {
        ev.preventDefault();

        try {
            const response = await authenticate(`/api-auth/login`, {
                username,
                email,
                password
            });

            console.log(username, email, password);
            console.log(response);
        } catch(err) {
            console.log('Error logging user', (err as Error).message);
            setError((err as Error).message);
        }
    };
    
    const formProps: FormProps = {
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
        onSubmit: logIn, 
        error
    };

    return (
        <div className='form-container log-in'>
            <div className='form-title'>Log In</div>
            <Form {...formProps} >
                <div className="form-footer">
                    Don't have an account? <Link to='/sign-up'>Create One!</Link>
                </div>
            </Form>
        </div>
    );
}