import { render,screen } from '@testing-library/react';
import Form from '../../../../components/Form/Form';

test('renders the Form component correctly', () => {
    const formProps = {
        fields: {
            username: {
                type: 'text',
                required: true,
                id: 'username'
            },
            email: {
                type: 'email',
                required: true,
                id: 'email'
            },
            name: {
                type: 'text',
                required: true,
                readOnly: true,
                value: 'John',
                placeholder: 'Your name',
                id: 'name'
            }
        }
    }

    render(<Form {...formProps} />);

    const usernameInputElem = screen.getByPlaceholderText('username');
    expect(usernameInputElem).toBeInTheDocument();
    expect(usernameInputElem.required).toBe(true);
    expect(usernameInputElem.id).toBe('username');

    const emailInputElem = screen.getByPlaceholderText('email');
    expect(emailInputElem).toBeInTheDocument();
    expect(emailInputElem.required).toBe(true);
    expect(emailInputElem.id).toBe('email');

    const nameInputElem = screen.getByPlaceholderText('Your name');
    expect(nameInputElem).toBeInTheDocument();
    expect(nameInputElem.required).toBe(true);
    expect(nameInputElem.readOnly).toBe(true);
    expect(nameInputElem.value).toBe('John');
    expect(nameInputElem.id).toBe('name');

});
