import { useEffect, useState } from "react";

export default function Feed(props: any) {
    const [poems, setPoems] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        fetch('api/poems')
            .then(req => (
                req.json()
            ))
            .then(result => {
                if (result.error) throw new Error(result.error);
                // setPoems([...poems, result]);
            })
            .catch(err => {
                setError(err.message);
            });
    }, []);

    return (
        <div className='poem-container'>
            {
                // poems? 
                //     poems.map((poem) => (
                //         <div key={poem.id} className='poem'>
                //             <h3>{poem.title}</h3>
                //             <p>{poem.author}</p>
                //             <p>{poem.date}</p>
                //         </div>
                //     ))
                // :
                //     (
                //         error?
                //             <div>
                //                 {error}
                //             </div>
                //         :
                //             <div>
                //                 Loading...
                //             </div>
                //     )
            }
        </div>
    )
}