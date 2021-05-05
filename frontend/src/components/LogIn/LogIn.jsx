import Form from "../common/Form/Form";

const formProps = {
    userName: {
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
        <div>
            Log In
            <Form {...formProps} />
        </div>
    );
}