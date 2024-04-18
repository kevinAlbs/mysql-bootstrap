Create a file `hello.py`:
```
# hello.py
print ("Hello world")
# Use `input` to pause before exit.
input ("Press enter to continue")
```

Install `pyinstaller`:

```
pip install -U pyinstaller
```

Build the exe:
```
pyinstaller .\hello.py
```

Open the exe from `.\dist\hello\hello.exe`

