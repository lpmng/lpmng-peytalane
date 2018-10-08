function delete_transaction(element,id)
{
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function()
    {
        if (xhr.readyState === 4)
        {
            if (xhr.status === 200) 
            {
                element.parentNode.parentNode.removeChild(element.parentNode);
            }

        }
    }
    xhr.open('DELETE', '/reservation?id=' + encodeURIComponent(id), true)
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded')
    xhr.setRequestHeader('X-CSRFToken',getCookie("csrftoken"))
    xhr.send()
}

function set_user_admin(element,username)
{
    if(element.checked)
        admin = 1
    else
        admin = 0

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function()
    {
        if (xhr.readyState === 4)
        {
            if (xhr.status === 200) 
            {
                console.log("put admin ok")
            }

        }
    }
    xhr.open('PUT', '/reservation/admin/user?username=' + encodeURIComponent(username) + "&admin="+admin, true)
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded')
    xhr.setRequestHeader('X-CSRFToken',getCookie("csrftoken"))
    xhr.send()
}

function set_payment_delivered(element,id)
{
    if(element.checked)
        delivered = 1
    else
        delivered = 0

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function()
    {
        if (xhr.readyState === 4)
        {
            if (xhr.status === 200) 
            {
                console.log("put admin ok")
            }

        }
    }
    xhr.open('PUT', '/reservation/admin/food?id=' + encodeURIComponent(id) + "&delivered="+delivered, true)
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded')
    xhr.setRequestHeader('X-CSRFToken',getCookie("csrftoken"))
    xhr.send()
}

function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}