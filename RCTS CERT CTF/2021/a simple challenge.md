# A simple challenge
![img](https://i.imgur.com/GUlyBy5.png)

- Attached file

```
Vm0weE1HRXlTWGxVYTJoVllXeGFVMWx0ZEV0alZuQlhWbXQwYVUxVk5WZFpWVlUxWVZaS2RHUkVXbFpOYWtVd1dWUkdSbVF4VG5GUmJHaHBVakpvVVZkc1pEUmpNV1JIWTBWb2JGSnJTbTlXYkZaM1RVWmtXR1JIZEZOTmEzQXdWbTF3WVZaWFNuTlhiVVpoVmpOU1RGa3llRk5XTVd3MlVtMXNhVkl5WTNsV1Z6QXhaREZrVmsxWVJsWmhhelZvVld4YWNrMUdjRmhOVlhSclVteEtNVmxyWkRSWFJrcFdZa1JPVjFKc2NGUlZWRXBUVm0xS1IySkZOVk5TUlVVMQ==
```

- The attached file looks like a base64 encoded string and every time I try to decode it returns another base64 encoded string so I wrote a python script so we can decode it till it returns an error (means it is no longer base64)

```python
import base64

cipher = "Vm0weE1HRXlTWGxVYTJoVllXeGFVMWx0ZEV0alZuQlhWbXQwYVUxVk5WZFpWVlUxWVZaS2RHUkVXbFpOYWtVd1dWUkdSbVF4VG5GUmJHaHBVakpvVVZkc1pEUmpNV1JIWTBWb2JGSnJTbTlXYkZaM1RVWmtXR1JIZEZOTmEzQXdWbTF3WVZaWFNuTlhiVVpoVmpOU1RGa3llRk5XTVd3MlVtMXNhVkl5WTNsV1Z6QXhaREZrVmsxWVJsWmhhelZvVld4YWNrMUdjRmhOVlhSclVteEtNVmxyWkRSWFJrcFdZa1JPVjFKc2NGUlZWRXBUVm0xS1IySkZOVk5TUlVVMQ=="
while True:
    try:
        base64_bytes = base64.b64decode(cipher.encode('ascii'))
        cipher = base64_bytes.decode('ascii')
        print(cipher)
    except:
        break
```

- Flag: flag{3nc0d1ng_1s_n0t_3ncrypt10n!}