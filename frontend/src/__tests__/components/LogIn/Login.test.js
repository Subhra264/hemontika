import { screen } from '@testing-library/react';
import App from '../../../App';
import { renderWrappedWithRouter } from '../../../utils/test-utils';

test('renders the Login component correctly', () => {
    renderWrappedWithRouter(<App />, { initialEntries: ['/log-in'] });

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