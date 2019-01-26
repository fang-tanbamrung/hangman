## for Thai
#### การ run program
1. ลง python2.7(lib : json, termcolor)
2. เข้า directory ที่ไฟล์ hangman.py อยู่
3. run ใน terminal/cli(command line interface) ตามคำสั่ง
    ```bash
    $ python hangman.py
    ```
#### การเพิ่มคำศัพท์
1. เพิ่มไฟล์ตามชื่อหมวดหมู่.json แล้วเพิ่มข้อมูลในรูปแบบ
    [
        {
            "hint":"คำใบ้1",
            "word":"คำศัพท์1"
        },
        {
            "hint":"คำใบ้2",
            "word":"คำศัพท์2"
        }
    ]

2. เพิ่มชื่อหมวดหมู่ในไฟล์ category.json ในรูปแบบ
    {
        "cate":[
            "reptile",
            "mammal",
            "ชื่อหมวดหมู่ที่ตรงกับชื่อไฟล์"
        ]
    }

## for English
####  run program
1. install python2.7(lib : json, termcolor)
2. on hangman.py directory
3. run this command on terminal/cli(command line interface)
    ```bash
    $ python hangman.py
    ```
#### add vocabulary
1. add file 
    ```bash
    [name of category].json 
    ```
    and in file add data like this
    ```bash
    [
        {
            "hint":"1st hint",
            "word":"1st word"
        },
        {
            "hint":"2nd hint",
            "word":"2nd word"
        },
        .
        .
        .,
        {
            "hint":"last hint",
            "word":"last word"
        }
    ]
    ```

2. add name of category(same of file name that just add) in  category.json inform
```bash
    {
        "cate":[
            "reptile",
            "mammal",
            "[name of category]"
        ]
    }
```
