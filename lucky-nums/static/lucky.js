/** processForm: get data from form and make AJAX call to our API. */

luckyForm = $("#lucky-form")

function processForm(evt) {

    var name = document.getElementById('name').value
    var birth_year = document.getElementById('birth_year').value
    var email = document.getElementById('email').value
    var color = document.getElementById('color').value
    var type_of_fact = document.getElementById('type_of_fact').value
    

    input = {name:name, birth_year:birth_year,email:email,color:color,type_of_fact:type_of_fact}
    return input
}

/** handleResponse: deal with response from our lucky-num API. */

async function handleResponse(data) {
    console.log("passed data is ", data)
    const res = await axios.post("http://127.0.0.1:5000/numberapi", data)
    console.log(res)
    $('body').append(res.data.text + "tes test tes")
    
    return res
}


$("#lucky-form").on("submit",function(e){
    e.preventDefault()
    handleResponse(processForm())
});

