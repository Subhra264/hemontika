import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Form, { FormProps } from '../Form/Form';
import authenticate from '../../utils/authenticate';

export default function SignUp (props: any) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [error, setError] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');

    const changeUsername: React.ChangeEventHandler = (ev: React.ChangeEvent<HTMLInputElement>) => {
        setUsername(ev.target.value);
    };

    const changeEmail: React.ChangeEventHandler = (ev: React.ChangeEvent<HTMLInputElement>) => {
        setEmail(ev.target.value);
    };

    const changePassword: React.ChangeEventHandler = (ev: React.ChangeEvent<HTMLInputElement>) => {
        setPassword(ev.target.value);
    };

    const changeFirstName: React.ChangeEventHandler = (ev: React.ChangeEvent<HTMLInputElement>) => {
        setFirstName(ev.target.value);
    };

    const changeLastName: React.ChangeEventHandler = (ev: React.ChangeEvent<HTMLInputElement>) => {
        setLastName(ev.target.value);
    };

    const signUp: React.MouseEventHandler = async (ev: React.MouseEvent) => {
        ev.preventDefault();

        try {
            const response = await authenticate(`/api-auth/signup`, {
                username,
                email,
                password,
                firstName,
                lastName
            });

            console.log(username, email, password, firstName, lastName);
            console.log(response);
        } catch(err) {
            console.log('Error signing user', (err as Error).message);
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
            }, 
            firstName:{
                type: 'text',
                required: false,
                placeholder: 'First Name',
                onChange: changeFirstName
            },
            lastName: {
                type: 'text',
                required: false,
                placeholder: 'Last Name',
                onChange: changeLastName
            }
        },
        onSubmit: signUp,
        error
    };

    return (
        <div className='form-container sign-up'>
            <div className='form-title'>Sign Up</div>
            <Form {...formProps} >
                <div className="form-footer">
                    Already have an account? <Link to='/log-in'>Log In</Link>
                </div>
            </Form>
        </div>
    );
}