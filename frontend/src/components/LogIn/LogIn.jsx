import Form from "../common/Form/Form";

const formProps = {
    username: {
        type: 'text',
        required: true
    },
    password: {
        type: 'password',
        required: true
    },
    email: {
        type: 'email',
        required: true
    }
};

export default function LogIn(props) {
    return (
        <div className='form-container log-in'>
            <div className='form-title'>Log In</div>
            <Form {...formProps} />
        </div>
    );
}