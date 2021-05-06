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
    }, 
    firstName:{
        type: 'text',
        required: false,
        placeholder: 'First Name'
    },
    lastName: {
        type: 'text',
        required: false,
        placeholder: 'Last Name'
    }
};

export default function SignUp(props) {
    return (
        <div className='form-container sign-up'>
            <div className='form-title'>Sign Up</div>
            <Form {...formProps} />
        </div>
    );
}