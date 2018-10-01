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