from tracemalloc import start
from selenium import webdriver
from cloud.cloudService import Cloud
from fashionService.yoloLib import *
from util.timeTransform import transform_local_time
import multiprocessing as mp
import base64
import json
import re
import pymongo


def recommend_fashion(img):  # return string
    image_bytes = cv2.imencode('.jpg', img)[1].tobytes()
    img_b64 = base64.b64encode(image_bytes)
    img_b64 = img_b64.decode('UTF-8')
    cloud = Cloud()
    cloud.photo = img_b64
    fashion_data = cloud.combination_service()

    fashion_data = json.loads(fashion_data)

    google_data = fashion_data[1]["labelAnnotations"]
    azure_data = fashion_data[0]['faceAttributes']
    gender = azure_data['gender']
    age = int(azure_data['age'])
    print(gender, age)
    # print('眼鏡',azure_data['glasses'])
    # print('眼妝',azure_data['makeup']['eyeMakeup'])
    # print('唇妝',azure_data['makeup']['lipMakeup'])

    print("---------")

    # print("Google labels:")
    # for label in google_data:
    #     print(label["description"])

    # labelArray = []
    # for label in google_data:
    #    labelArray.append(label["description"])

    # labelStr = " ".join(labelArray)
    # print(labelStr)

    label_str = ''
    for label in google_data:
        label_str += (label["description"] + " ")

    TartanRegex = re.compile(r'Tartan')
    ActiveTRegex = re.compile(r'Active shirt')
    T_shirtRegex = re.compile(r'T-shirt')
    CocktailRegex = re.compile(r'Cocktail dress')
    ShirtRegex = re.compile(r'Dress shirt')
    PlaidRegex = re.compile(r'Plaid')
    DenimRegex = re.compile(r'Denim')
    SportswearRegex = re.compile(r'Sportswear')
    boardShortRegex = re.compile(r'board short')
    DressRegex = re.compile(r'Dress$')
    KneeRegex = re.compile(r'Knee')
    One_pieceRegex = re.compile(r'One-piece garment')
    OvercoatRegex = re.compile(r'Overcoat')
    VintageRegex = re.compile(r'Vintage clothing')
    JeansRegex = re.compile(r'Jeans')
    ShortsRegex = re.compile(r'Shorts')
    HeelsRegex = re.compile(r'High heels')
    SuitRegex = re.compile(r'Suit')
    CollarRegex = re.compile(r'collar')
    SleeveRegex = re.compile(r'Sleeve')

    Tartan = TartanRegex.search(label_str)
    Active_Tshirt = ActiveTRegex.search(label_str)
    T_shirt = T_shirtRegex.search(label_str)
    Cocktail = CocktailRegex.search(label_str)
    Shirt = ShirtRegex.search(label_str)
    Plaid = PlaidRegex.search(label_str)
    Denim = DenimRegex.search(label_str)
    Sportswear = SportswearRegex.search(label_str)
    boardShort = boardShortRegex.search(label_str)
    Dress = DressRegex.search(label_str)
    Knee = KneeRegex.search(label_str)
    One_piece = One_pieceRegex.search(label_str)
    Overcoat = OvercoatRegex.search(label_str)
    Vintage = VintageRegex.search(label_str)
    Jeans = JeansRegex.search(label_str)
    Shorts = ShortsRegex.search(label_str)
    Highheels = HeelsRegex.search(label_str)
    Suit = SuitRegex.search(label_str)
    Collar = CollarRegex.search(label_str)
    Sleeve = SleeveRegex.search(label_str)

    output = ''

    if gender == "female":
        if 6 <= age <= 10:
            output = "zara young girl clothing"
        elif 10 <= age <= 18:
            if Dress:
                output = "女學生 洋裝"
            else:
                output = "女學生 上衣"
        elif 18 <= age <= 30:
            if One_piece:
                if Denim:
                    output = "mouggan 連身褲"
                elif Overcoat:
                    output = "mouggan 風衣外套 大衣"
                else:
                    output = "長裙"
            elif Dress:
                if Shorts:
                    output = "短裙"
                elif Denim:
                    output = "mouggan 丹寧洋裝"
                elif Vintage:
                    output = "碎花洋裝"
                else:
                    output = "jendes 洋裝"
            elif Shirt:
                if Tartan:
                    output = "caco 女 格紋襯衫"
                if Jeans:
                    output = "jendes 牛仔褲"
                else:
                    output = "mouggan 襯衫"
            elif T_shirt:
                if Sportswear:
                    if Shorts:
                        output = "牛仔短褲"
                    elif Knee:
                        output = "皮革短裙"
                    else:
                        output = "Adidas 女款外套"
                elif Cocktail:
                    output = "長裙"
                else:
                    output = "牛仔褲"
            elif Sleeve:
                output = "meier q 襯衫"
            else:
                output = "漁夫帽"

        elif 31 <= age <= 50:
            if Dress:
                output = "brand dress"
            elif T_shirt:
                output = "mouggan 長裙"
            elif Shirt:
                output = "mobo 白 襯衫"
            else:
                output = "uniqlo 褲裙"
        else:
            output = "uniqlo 防曬外套"

    else:
        print(("男"))
        if 6 <= age <= 10:
            output = "zara young boy clothing"
        elif 10 <= age <= 18:
            if T_shirt:
                if Plaid:
                    output = "青少年 條紋上衣"
                else:
                    output = "男 卡通 上衣"
            else:
                output = "學生 運動褲"
        elif 18 <= age:
            if T_shirt:
                if Plaid:
                    if Collar:
                        output = "男款 襯衫"
                    else:
                        output = "男款 條紋上衣"
                elif Active_Tshirt:
                    output = "JERSCY 新色素T"
                elif boardShort:
                    output = "男生 休閒短褲"
                else:
                    output = "男款 Adidas 運動外套"
            elif Suit:
                output = "Calvin Klein slim fit  jacket"
            elif Shirt:
                output = "男款 襯衫"
            else:
                output = "男版 uniqlo 素T"
    return output, age, gender


# TODO 接照片去背與計算顏色比例
# def img_remove_background(img): --> return img
# def img_calculate_color(img): --> return color-percent with json


def crawl_google_image(query_string, user_name, customer_age, customer_gender, customer_time):
    category = query_string  # 放置query字串
    target_num = 1  # 張數

    url = "https://www.google.com.tw/search?q=" + \
          category + "&source=lnms&tbm=isch&sa=X"
    # The path of ChromeDriver
    # Target element xpath
    xpath = "//img[contains(@class,'Q4LuWd')]"

    # Ignition chrome
    driver_path = '/Users/jyun/Final-Project/python/FlaskServer/fashionService/chromedriver'
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(driver_path, chrome_options=option)

    pos = 0
    photo_num = 0
    Idle_count = 0
    done = False
    img_url_dic = {}
    img_result = []
    driver.get(url)
    while not done:
        pos += 500
        js = "document.documentElement.scrollTop=%d" % pos
        driver.execute_script(js)
        time.sleep(1)

        for element in driver.find_elements_by_xpath(xpath):
            try:
                img_url = element.get_attribute('src')
                if img_url != None and not img_url in img_url_dic:
                    img_url_dic[img_url] = ''
                    Idle_count = 0
                    photo_num += 1
                    data_to_mongo = {"user_name": user_name,
                                     "customer_sex": customer_gender,
                                     "customer_age": customer_age,
                                     "customer_time": customer_time,
                                     "customer_img_path": "static/image/customer/{}.jpg".format(customer_time),
                                     "customer_recommend_product": category,
                                     "customer_recommend_color": "blue",
                                     "customer_recommend_img": img_url}

                    client = pymongo.MongoClient(host='localhost', port=27017)
                    db = client['customer-info']
                    db.customer.insert(data_to_mongo)
                else:
                    Idle_count += 1
                if photo_num >= target_num or Idle_count >= 2000:
                    done = True
                    break
            except OSError:
                print('Occur OSError!')
                break
    print("Crawler download progress is completed.")
    print("Recommend Done!")
    driver.close()
    return 'Recommend done'


def gen_Video(video, width, height, model, count, user_name, category_names, colors):
    while True:
        begin_time = time.time()
        customer_time = transform_local_time(time.time())
        ret, frame = video.read()
        frame = cv2.resize(frame, (width, height))

        classes, confs, boxes = nnProcess(frame, model)
        start_time = time.time()
        if len(classes) == 1:
            count += 1
            if count == 30:
                
                count = 0
                print('write one picture')
                recommend_query_string, age, gender = recommend_fashion(frame)
                crawl_google_image(recommend_query_string,
                                   user_name, age, gender, customer_time)
                cv2.imwrite('static/image/customer/{}.jpg'.format(customer_time), frame,
                            [cv2.IMWRITE_JPEG_QUALITY, 100])

        frame = drawBox(frame, classes, confs, boxes, category_names, colors)
        frame = cv2.resize(frame, (800, 450))
        fps = 'fps: {:.2f}'.format(1 / (time.time() - begin_time))
        cv2.putText(frame, fps, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 204, 255), 2
                    )
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        end_time = time.time()
        print('Recommand Done!---spent {} second.'.format(end_time-start_time))
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
