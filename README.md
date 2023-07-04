### TranslucentTB
#### This is a python version TranslucentTB maybe with tkinter and ctypes

A lightweight utility that makes the Windows taskbar translucent/transparent on Windows 10 and Windows11.

### Screenshots
![image](https://github.com/littlewhitecloud/TranslucentTB/assets/71159641/97763cac-2b58-4208-b98b-36d031c86880)
![image](https://github.com/littlewhitecloud/TranslucentTB/assets/71159641/761f84b4-5367-40a2-81ec-e9e97b2f19f5)
![image](https://github.com/littlewhitecloud/TranslucentTB/assets/71159641/78b2a579-4c5f-4d95-8b68-4fe2b4f2ba29)
![image](https://github.com/littlewhitecloud/TranslucentTB/assets/71159641/211f4147-ce5d-4f04-9126-e274369abdfd)

### Usage
```python
from translucenttb import blur # import the blur function
blur(blurtype="acrylic") # for example acrylic
# choose one type from ("clear", "noeffect", "blur", "acrylic")
```

### UI
![image](https://github.com/littlewhitecloud/TranslucentTB/assets/71159641/0a9ecdd5-f5ae-4fa9-b124-09a1e9ed849a)
```python
from translucenttb import Settings
example = Settings()
example.mainloop()
```
### Example:
<details>
    
```python
from time import sleep

from translucenttb import blur


def colorful():
    hexdict = [
        "#FF0000",
        "#FF3030",
        "#FF5656",
        "#FF7456",
        "#FFA500",
        "#FF7438",
        "#FF8956",
        "#FFAB56",
        "#FFB871",
        "#FFFF00",
        "#FFCD71",
        "#FFE071",
        "#FFF571",
        "#F4FF71",
        "#D8FF71",
        "#C8FF71",
        "#008000",
        "#9FF65B",
        "#00FFFF",
        "#79F65B",
        "#5FF65B",
        "#5BF67D",
        "#5BF69C",
        "#5BF67D",
        "#5BF6C5",
        "#5BF6DC",
        "#2AFFDC",
        "#2AFCFF",
        "#2AC5FF",
        "#2AADFF",
        "#2A87FF",
        "#2A6BFF",
        "#2A49FF",
        "#0000FF",
        "#2A35FF",
        "#3A2AFF",
        "#502AFF",
        "#602AFF",
        "#800080",
    ]

    for hexcolor in hexdict:
        blur("noeffect", hexcolor)
        sleep(0.1)


colorful()
```
https://github.com/littlewhitecloud/TranslucentTB/assets/71159641/a2d0b4cc-0698-46c0-b050-e3d89c788964

</details>
