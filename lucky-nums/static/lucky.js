/** processForm: get data from form and make AJAX call to our API. */



luckyForm = $("#lucky-form")

function processForm(evt) {

    var name = document.getElementById('name').value
    var birth_year = document.getElementById('birth_year').value
    var email = document.getElementById('email').value
    var color = document.getElementById('color').value
    var type_of_fact = document.getElementById('type_of_fact').value
    
    output = {name:name, birth_year:birth_year,email:email,color:color,type_of_fact:type_of_fact}
    return output
}

/** handleResponse: deal with response from our lucky-num API. */

async function handleResponse(res) {
    console.log("passed data is ", res)
   

    if(res.length >= 2){
        $('#lucky-results').empty().append(`<h1>Your birth year:</h1><br><p>${res[0].text}</p><br>
    <h1>Your lucky number is ${res[1].number}, fun fact:</h1><br><p>${res[1].text}</p>`)
 
    } else {
        console.log("validation error")
 
        $('#lucky-results').empty().append(`<h1>${Object.values(res)}</h1>`)
    }
   


}




$("#lucky-form").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.
    var form = $(this);
    var actionUrl = form.attr('http://127.0.0.1:5000/numberapi');
    
    $.ajax({
        type: 'post',
        url: 'http://127.0.0.1:5000/numberapi',
        data: form.serialize(), // serializes the form's elements.
        success: function(data)
        {
          console.log(data)
          //alert(data.data); // show response from the php script.
          handleResponse(data)
          

        }
       
    });


});
