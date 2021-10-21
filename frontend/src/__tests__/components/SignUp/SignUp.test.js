import { screen } from '@testing-library/react';
import App from '../../../App';
import { renderWrappedWithRouter } from '../../../utils/test-utils';

test('renders the Login component correctly', () => {
    renderWrappedWithRouter(<App />, { initialEntries: ['/sign-up'] });

    const usernameInputElem = screen.getByPlaceholderText('username');
    const emailInputElem = screen.getByPlaceholderText('email');
    const passwordInputElem = screen.getByPlaceholderText('password');
    const firstNameInputElem = screen.getByPlaceholderText('First Name');
    const lastNameInputElem = screen.getByPlaceholderText('Last Name');

    expect(usernameInputElem).toBeInTheDocument();
    expect(usernameInputElem.required).toBe(true);

    expect(emailInputElem).toBeInTheDocument();
    expect(emailInputElem.required).toBe(true);

    expect(passwordInputElem).toBeInTheDocument();
    expect(passwordInputElem.required).toBe(true);

    expect(firstNameInputElem).toBeInTheDocument();
    expect(firstNameInputElem.required).toBe(false);

    expect(lastNameInputElem).toBeInTheDocument();
    expect(lastNameInputElem.required).toBe(false);
});
