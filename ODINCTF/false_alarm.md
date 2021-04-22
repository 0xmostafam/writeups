# False Alarm / Web / Easy

## Description

Try to make a dummy alert

---

## Solution

viewing the page source i found this code

```javascript
function loadObj(){
 var cc=eval('('+unescape(aacc)+')');
 document.getElementById('msg').textContent=cc.message;
}

if(window.location.hash.indexOf('mass')==-1)
  var aacc="({\"message\":\"Hello User!\"})";
else
  var aacc=location.hash.substr(window.location.hash.indexOf('mass=')+5);
```

and

```javascript
var tmp =location.hash;

        $.ajax({
        type: "POST",
        url: "Tc5IQib027qvyjSMfHjOMaLk.php",
        data: {"tmp":tmp},
        success: function(data,status){
            eval(data)
            }
        }); 
```

i understood that i need to manipulate the URL and add a hash value of string `mass=` and add the payload after it 

forming this url `https://ch6.sbug.se/#mass=alert(%22xss%22)`

---

## Flag

FLAG{DOMDOM-XSS-1337}