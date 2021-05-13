
export default async function authenticate(fetchUri, reqBody) {
    try {
        let response = await fetch(fetchUri, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(reqBody)
        });

        response = await response.json();
        return response;
    } catch (err) {
        console.log(err);
        return err;
    }
}