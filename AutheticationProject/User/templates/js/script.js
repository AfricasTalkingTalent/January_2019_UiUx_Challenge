const Url = 'http://127.0.0.1:8000/sign-up/'
function processSingUp() {
    var xhr = new XMLHttpRequest();
    xhr.open(form.method,form.action,true);
    xhr.setRequestHeader('Conent-Type','application/json;charset=UTF-8');
    var object = {
        "first_name":"brian",
        "last_name":"ogutu",
    };
    xhr.send(JSON.stringify(object))
    // const Data = {
    //     email: "Brian",
    //     first_name: "Okinyi"
    // };
    // const otherParam = {
    //     headers: {
    //         "content-type": "application/json;charset=UTF-8"
    //     },
    //     body: Data,
    //     method: "POST"
    // };
    // fetch(Url)
    //     .then(data => { return data.json() })
    //     .then(res => { console.log(res) })
}