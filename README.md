# JSON Config

A lightweight Python module for a simple config class. Use JSON files for your settings.   

_feel free to expand this class_

## Example

### JSON File
```json
{
    "settings":
    {
        "languages": ["de", "en"]
    }
}
```

### Python File
```python
from config import Config

# name of your settings file
# write your full path here, if your file isn't located in the same directory
conf = Config("settings.json") 

# access a key in your settings file
languages = conf["settings"]["languages"]
```
   
   Published under [MIT License](https://gitlab.com/fabianschilf/json-config/blob/master/LICENSE)