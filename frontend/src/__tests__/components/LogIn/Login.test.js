import { render, screen } from '@testing-library/react';
import Login from '../../../components/LogIn/LogIn';

test('renders the Login component correctly', () => {
    render(<Login />);
    const usernameInputElem = screen.getByPlaceholderText('username');
    const emailInputElem = screen.getByPlaceholderText('email');
    const passwordInputElem = screen.getByPlaceholderText('password');

    expect(usernameInputElem).toBeInTheDocument();
    expect(usernameInputElem.required).toBe(true);

    expect(emailInputElem).toBeInTheDocument();
    expect(emailInputElem.required).toBe(true);

    expect(passwordInputElem).toBeInTheDocument();
    expect(passwordInputElem.required).toBe(true);
});