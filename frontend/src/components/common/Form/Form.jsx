

const Form = (props) => {
    const inputFields = [];

    for(const field in props){
        const inputField = props[field];
        inputFields.push(
            <input placeholder={field} { ...inputField } key={field}/>
        );
    }

    return (
        <div>
            {inputFields}
        </div>
    );
}

export default Form;