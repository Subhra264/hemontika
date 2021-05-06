import './Form.scss';

const Form = (props) => {
    const inputFields = [];

    for(const field in props){
        const inputField = props[field];
        inputFields.push(
            <input placeholder={field} { ...inputField } key={field}/>
        );
    }

    return (
        <div className='form'>
            <form>
                {inputFields}
                <input type='submit' className='submit-button' value='Submit' />
            </form>
        </div>
    );
}

export default Form;