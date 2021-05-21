{%hackmd theme-dark %}
# Week3 進度報告
# Backend: 2021.05.21 Jeff
###### tags: `bcrypt` `JWT` `Google Vision API`
[TOC]
## 上週任務
![](https://i.imgur.com/m5VkTnw.png)


## Bcrypt
- [Bcrypt 是什麼](https://www.wikiwand.com/en/Bcrypt)？
:::info
一個 [Node.js Library](https://github.com/kelektiv/node.bcrypt.js)。能協助使用者密碼作雜湊。
:::

- Bcrypt 能幹嗎？
    - 使用時機
        - 當資料庫被盜，密碼不會被看光光
            - e.g. 
                - ![](https://i.imgur.com/Oa9TiOm.png)
                    - 紅色匡起來，密碼是明文
                    - 綠色匡起來，密碼已雜湊 -> 密碼經過雜湊（就算是資料庫管理者也不知道密碼）

- Bcrypt 原理？
    - Bcrypt 其實一個密碼雜湊函數(單向雜湊 => 不可逆)。
    - 組成圖示 => 輸出為 60 個字串（固定）
        - ![](https://i.imgur.com/hbcBesl.png)
        [reference link](https://www.wikiwand.com/en/Bcrypt)
        
        - ![](https://i.imgur.com/O3Iu2eN.png)
        [reference link](https://www.jianshu.com/p/2b131bfc2f10)
    - 雜湊流程：
        - ![](https://i.imgur.com/hEkAVV4.png)
        - 強度比較：
            - 明文 < 編碼 < 加密 < 雜湊 < 加鹽雜湊 < 加鹽 Bcrypt 雜湊(慢雜湊演算法)
    [reference link](https://medium.com/starbugs/how-to-store-password-in-database-sefely-6b20f48def92)
    - Cost factor = rounds = work factor => 若 rounds = 10 代表 雜湊 $2^{10}$ rounds。數字越大，代表需要的計算時間成本更高，破解難度更大。


        > 和 MD5 一起來比較的話，如果使用值為12的 work factor 的話，如果加密 “cool” 的話，bcrypt 需要0.3秒，而 MD5 只需要一微秒（百萬分之一秒）。也就是說，前面我們說的那個只需要40秒就可以窮舉完所有的可能的 MD5 編碼的密碼的演算法，在使用 bcrypt 下，需要12年。
        >>[reference link](https://www.jianshu.com/p/2b131bfc2f10)
- 在 backend 的實作 
    - import module
        - ```javascript=
          const { hashSync, genSaltSync } = require('bcrypt');
          ```
    - 時機在 backend 上的 code
        - ![](https://i.imgur.com/I9RSAIQ.png)

## JWT
- JWT 是什麼？
    :::info
    用於在雙方之間**安全**地將訊息作為 **JSON 物件傳輸**
    :::
- JWT 能幹嗎？
    - 優點：
        - 簡潔(compact) -> **體積非常的小**，可放在 URL 、 POST 參數或 HTTP Header 內發送請求，體積小意味著**傳輸速度快**。
        ![](https://i.imgur.com/Gr8Z8c9.png)
        - 自包含(self-contained) -> payload 裡面**就有所需要的資訊**，不需要再重新 query database 的資料。
    -  使用時機：
        -  授權 -> Client 帶著 JWT 而有相對應的資源。
        -  訊息交換 -> 因為可以透過公/私鑰做簽章，可以知道是誰發送的 JWT。也可以驗證內容是否遭到竄改。
        [reference link](https://5xruby.tw/posts/what-is-jwt)
- JWT 驗證流程
    - Login 階段(前提：資料庫已經有使用者帳號、密碼)
        :::info
        ```sequence
        Client->Auth Service: 1. Login with username and password

        Auth Service->User Service(MySQL): 2. Get user info
        User Service(MySQL)-->Auth Service: 3. Reply
        Auth Service->Auth Service: 4. Authenticate & generate token
        Auth Service->Auth Service: 5. Reply result
        Auth Service->Client: 6. Reply JWT if login valid
        ```
        :::
     - 使用服務階段
        :::info
        ```sequence
        Client->Auth Service: 1. Use suggesting system with JWT 
        Auth Service->Auth Service: 2. Verify JWT
        Auth Service->User Service: 3. Open the suggesting system page
        User Service-->Auth Service: 4. Reply
        Auth Service-->Auth Service: 5. Reply result
        Auth Service-->Client: 6. Reply result
        ```
        :::
        [reference link](https://jamessie.com/featured/%e6%b7%ba%e8%ab%87jwt%e7%9a%84%e5%ae%89%e5%85%a8%e6%80%a7%e8%88%87%e9%81%a9%e7%94%a8%e6%83%85%e5%a2%83/)
- JWT 原理
    - 組成圖示
    ![](https://i.imgur.com/3OgAfzk.png)
        - Header
        - Payload
        - Signature
    
    - 驗證流程
    ![](https://i.imgur.com/jsX9jfv.png)
- 在 backend 的實作 
    - Login 階段
        - ![](https://i.imgur.com/4tcBafz.png)
        - 四種狀況：
            - 藍色匡起來（無使用者名稱或錯誤的事件）
                - 沒背綠色框框的程式碼 -> MySQL 的錯誤處理
                - 綠色框框的程式碼 -> 無效的使用者名稱錯誤處理
            - 紅色匡起來（密碼正確或錯誤的事件）
                - 綠色框框的程式碼 -> 獲得 JWT (正確)
                - 沒背綠色框框的程式碼 -> 輸入錯誤密碼的錯誤處理
    - 使用服務階段
    ![](https://i.imgur.com/AfnObvp.jpg)

- 使用 Postman 測試小技巧 
    - Authoriaztion -> Bearer Token -> 替換 Token
    ![](https://i.imgur.com/NUpZ6FA.png)

## Google Vision API
- Google Vision API 是什麼？
    :::success
    Google Cloud’s Vision API offers powerful **pre-trained machine learning models** through **REST and RPC APIs**. Assign labels to images and quickly classify them into millions of predefined categories. **Detect objects and faces**, read printed and handwritten text, and **build valuable metadata** into your image catalog.
    [Reference](https://cloud.google.com/vision)
    :::
- Google Vision API 資料協定？
    - Request 
        - body
        ```json=
        {
          "requests":[
            {
              "image":{
                "content":"/9j/7QBEUGhvdG9zaG9...image contents...fXNWzvDEeYxxxzj/Coa6Bax//Z"
              },
              "features":[
                {
                  "type":"FACE_DETECTION",
                  "maxResults":10
                }
              ]
            }
          ]
        }
        ```
        - 注意
        :::danger
        **content-type 一定要加 charset=UTF-8**，否則會噴錯。
        e.g. 'content-type': 'application/json; charset=UTF-8'
        :::
    - [Response Format](https://cloud.google.com/vision/docs/labels)
        - **mid** - if present, contains a ****machine-generated identifier** (MID) corresponding to the entity's Google Knowledge Graph entry. Note that mid values remain unique across different languages, so you can use these values to tie entities together from different languages. To inspect MID values, refer to the Google Knowledge Graph API documentation.
        - **description** - the label description.
        - **score** - the **confidence score**, which ranges from 0 (no confidence) to 1 (very high confidence).
        - **topicality** - The relevancy of the ICA (Image Content Annotation) label to the image. It **measures how important/central a label is to the overall context of a page**.

- Google Vision API Result
    - Input(Convert to Base64):
        - ![](https://i.imgur.com/udrbSxH.png)
    - Output
        ```json=
        {
          "returnCode": "200",
          "detail": [
            {
              "labelAnnotations": [
                {
                  "mid": "/m/03q69",
                  "description": "Hair",
                  "score": 0.9861285,
                  "topicality": 0.9861285
                },
                {
                  "mid": "/m/0dzct",
                  "description": "Face",
                  "score": 0.9857265,
                  "topicality": 0.9857265
                },
                {
                  "mid": "/m/0k0pj",
                  "description": "Nose",
                  "score": 0.98358303,
                  "topicality": 0.98358303
                },
                {
                  "mid": "/m/06z04",
                  "description": "Skin",
                  "score": 0.9762376,
                  "topicality": 0.9762376
                },
                {
                  "mid": "/m/04hgtk",
                  "description": "Head",
                  "score": 0.9751926,
                  "topicality": 0.9751926
                },
                {
                  "mid": "/m/01dvt1",
                  "description": "Joint",
                  "score": 0.9750415,
                  "topicality": 0.9750415
                },
                {
                  "mid": "/m/06pj2k",
                  "description": "Lip",
                  "score": 0.9707111,
                  "topicality": 0.9707111
                },
                {
                  "mid": "/m/0f9swq",
                  "description": "Chin",
                  "score": 0.96725506,
                  "topicality": 0.96725506
                },
                {
                  "mid": "/m/0k65p",
                  "description": "Hand",
                  "score": 0.9582216,
                  "topicality": 0.9582216
                },
                {
                  "mid": "/m/027n3_",
                  "description": "Eyebrow",
                  "score": 0.9542992,
                  "topicality": 0.9542992
                },
                {
                  "mid": "/m/0ds4x",
                  "description": "Hairstyle",
                  "score": 0.9509009,
                  "topicality": 0.9509009
                },
                {
                  "mid": "/m/01ssh5",
                  "description": "Shoulder",
                  "score": 0.9408361,
                  "topicality": 0.9408361
                },
                {
                  "mid": "/m/014sv8",
                  "description": "Eye",
                  "score": 0.93863827,
                  "topicality": 0.93863827
                },
                {
                  "mid": "/m/03f52z",
                  "description": "Eyelash",
                  "score": 0.9263171,
                  "topicality": 0.9263171
                },
                {
                  "mid": "/m/0dzd8",
                  "description": "Neck",
                  "score": 0.88831997,
                  "topicality": 0.88831997
                },
                {
                  "mid": "/m/02p0tk3",
                  "description": "Human body",
                  "score": 0.88534075,
                  "topicality": 0.88534075
                },
                {
                  "mid": "/m/032tl",
                  "description": "Fashion",
                  "score": 0.88157994,
                  "topicality": 0.88157994
                },
                {
                  "mid": "/m/01k9lj",
                  "description": "Jaw",
                  "score": 0.88125896,
                  "topicality": 0.88125896
                },
                {
                  "mid": "/m/062581",
                  "description": "Sleeve",
                  "score": 0.8724503,
                  "topicality": 0.8724503
                },
                {
                  "mid": "/m/02qp_b",
                  "description": "Makeover",
                  "score": 0.86496717,
                  "topicality": 0.86496717
                },
                {
                  "mid": "/m/031974",
                  "description": "Waist",
                  "score": 0.8557286,
                  "topicality": 0.8557286
                },
                {
                  "mid": "/m/0244x1",
                  "description": "Gesture",
                  "score": 0.85260487,
                  "topicality": 0.85260487
                },
                {
                  "mid": "/m/06c7f7",
                  "description": "Lipstick",
                  "score": 0.83878326,
                  "topicality": 0.83878326
                },
                {
                  "mid": "/m/02qqd4n",
                  "description": "Fashion design",
                  "score": 0.8218539,
                  "topicality": 0.8218539
                },
                {
                  "mid": "/m/071j9r",
                  "description": "Cool",
                  "score": 0.8132745,
                  "topicality": 0.8132745
                },
                {
                  "mid": "/m/0fc1fy",
                  "description": "Black hair",
                  "score": 0.80930203,
                  "topicality": 0.80930203
                },
                {
                  "mid": "/m/09spj9",
                  "description": "Layered hair",
                  "score": 0.80235404,
                  "topicality": 0.80235404
                },
                {
                  "mid": "/m/02hqr87",
                  "description": "Fashion model",
                  "score": 0.8020067,
                  "topicality": 0.8020067
                },
                {
                  "mid": "/m/02pd__z",
                  "description": "Long hair",
                  "score": 0.7667365,
                  "topicality": 0.7667365
                },
                {
                  "mid": "/m/01f43",
                  "description": "Beauty",
                  "score": 0.7543108,
                  "topicality": 0.7543108
                },
                {
                  "mid": "/m/0408t8_",
                  "description": "Street fashion",
                  "score": 0.7379927,
                  "topicality": 0.7379927
                },
                {
                  "mid": "/m/02ksmb",
                  "description": "Brown hair",
                  "score": 0.7225363,
                  "topicality": 0.7225363
                },
                {
                  "mid": "/m/0294jb",
                  "description": "Blond",
                  "score": 0.7196876,
                  "topicality": 0.7196876
                },
                {
                  "mid": "/m/0404d",
                  "description": "Jewellery",
                  "score": 0.7194071,
                  "topicality": 0.7194071
                },
                {
                  "mid": "/m/081pkj",
                  "description": "Event",
                  "score": 0.70016056,
                  "topicality": 0.70016056
                },
                {
                  "mid": "/m/01vm1p",
                  "description": "Elbow",
                  "score": 0.6806076,
                  "topicality": 0.6806076
                },
                {
                  "mid": "/m/0463sg",
                  "description": "Fashion accessory",
                  "score": 0.6760009,
                  "topicality": 0.6760009
                },
                {
                  "mid": "/m/0dzdr",
                  "description": "Chest",
                  "score": 0.6736534,
                  "topicality": 0.6736534
                },
                {
                  "mid": "/m/03r18y",
                  "description": "Peach",
                  "score": 0.6631233,
                  "topicality": 0.6631233
                },
                {
                  "mid": "/m/0hgs2h_",
                  "description": "Bridal accessory",
                  "score": 0.657685,
                  "topicality": 0.657685
                },
                {
                  "mid": "/m/028mzr",
                  "description": "Hair coloring",
                  "score": 0.6307764,
                  "topicality": 0.6307764
                },
                {
                  "mid": "/m/0hgsb5g",
                  "description": "Day dress",
                  "score": 0.61831653,
                  "topicality": 0.61831653
                },
                {
                  "mid": "/m/02w3_2",
                  "description": "Formal wear",
                  "score": 0.5906528,
                  "topicality": 0.5906528
                },
                {
                  "mid": "/m/0cnmr",
                  "description": "Fur",
                  "score": 0.5857253,
                  "topicality": 0.5857253
                },
                {
                  "mid": "/m/05qdh",
                  "description": "Painting",
                  "score": 0.5792883,
                  "topicality": 0.5792883
                },
                {
                  "mid": "/m/02qbl1m",
                  "description": "Photo shoot",
                  "score": 0.5773519,
                  "topicality": 0.5773519
                },
                {
                  "mid": "/m/01dv4h",
                  "description": "Portrait",
                  "score": 0.5426634,
                  "topicality": 0.5426634
                },
                {
                  "mid": "/m/0hwky",
                  "description": "Pattern",
                  "score": 0.5369504,
                  "topicality": 0.5369504
                },
                {
                  "mid": "/m/0d1pc",
                  "description": "Model",
                  "score": 0.5320481,
                  "topicality": 0.5320481
                },
                {
                  "mid": "/m/0chml9",
                  "description": "Portrait photography",
                  "score": 0.50773615,
                  "topicality": 0.50773615
                }
              ],
              "localizedObjectAnnotations": [
                {
                  "mid": "/m/03gx245",
                  "name": "Top",
                  "score": 0.77517706,
                  "boundingPoly": {
                    "normalizedVertices": [
                      {
                        "x": 0.08164109,
                        "y": 0.46991932
                      },
                      {
                        "x": 0.8557673,
                        "y": 0.46991932
                      },
                      {
                        "x": 0.8557673,
                        "y": 0.99705213
                      },
                      {
                        "x": 0.08164109,
                        "y": 0.99705213
                      }
                    ]
                  }
                },
                {
                  "mid": "/m/01llx7",
                  "name": "Bracelet",
                  "score": 0.64256585,
                  "boundingPoly": {
                    "normalizedVertices": [
                      {
                        "x": 0.8477685,
                        "y": 0.33136028
                      },
                      {
                        "x": 0.94037557,
                        "y": 0.33136028
                      },
                      {
                        "x": 0.94037557,
                        "y": 0.4504279
                      },
                      {
                        "x": 0.8477685,
                        "y": 0.4504279
                      }
                    ]
                  }
                },
                {
                  "mid": "/m/01g317",
                  "name": "Person",
                  "score": 0.54514444,
                  "boundingPoly": {
                    "normalizedVertices": [
                      {
                        "x": 0.0060475226,
                        "y": 0.018381465
                      },
                      {
                        "x": 0.9973958,
                        "y": 0.018381465
                      },
                      {
                        "x": 0.9973958,
                        "y": 0.9973958
                      },
                      {
                        "x": 0.0060475226,
                        "y": 0.9973958
                      }
                    ]
                  }
                }
              ]
            }
          ]
        }
        ```
## 推薦 VSCode 套件 -> [Waka Time](https://wakatime.com/dashboard)
- 協助使用者紀錄寫 Code 的時間
    - ![](https://i.imgur.com/l9jBBsA.png)

## 問題討論
1. JWT 給前端帶？後端帶？
2. 架構的問題