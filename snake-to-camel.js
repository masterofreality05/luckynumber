function snakeToCamel(input) {

    let splitUp = input.split("_")
    let first = splitUp[0]
    let rest = splitUp.slice(1)
    let capitalized_list = []

    for (let to_capitalize of rest){
        let capitalized = to_capitalize.charAt(0).toUpperCase().concat(to_capitalize.slice(1))
        capitalized_list.push(capitalized)
    }

    return first.concat(capitalized_list).replaceAll(",","")
    
}

