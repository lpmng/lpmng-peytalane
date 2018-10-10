
function searchFood(element)
{
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function()
    {
        if (xhr.readyState === 4)
        {
            if (xhr.status === 200) 
            {
                Array.from(document.getElementsByClassName("food-line")).forEach(
                    (element) =>
                    {
                        let pizza_name = element.id.replace("container-","")
                        response = xhr.responseText
                        list_pizzas = JSON.parse(this.response).pizzas
                        
                        if (list_pizzas.indexOf(pizza_name) > -1)
                        {
                            element.style.display = ""
                        }
                        else
                        {
                            element.style.display = "none"
                        }
                    }
                )
            }

        }
    }
    xhr.open('GET', '/reservation/search/food?s=' + encodeURIComponent(element.value), true)
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded')
    xhr.setRequestHeader('X-CSRFToken',getCookie("csrftoken"))
    xhr.send()
}