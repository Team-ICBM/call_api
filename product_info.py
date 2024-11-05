import requests

# 1. 바코드를 통해 제품 정보 가져오기
import requests
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def get_product_info_by_barcode(barcode, api_key):
    url = f"http://openapi.foodsafetykorea.go.kr/api/{api_key}/C005/json/1/1/BAR_CD={barcode}"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.content)
        product_info = {
            "PRDLST_NM": data["C005"]["row"][0]["PRDLST_NM"],  # 제품명
        }
        return product_info
    else:
        print("바코드 API 요청 실패:", response.status_code)
        return None



def get_nutrition_info_by_name(product_name, api_key):
    url = "https://apis.data.go.kr/B553748/CertImgListServiceV3"
    params = {
        'serviceKey': api_key,
        'prdlstNm' : product_name,
        'returnType' : 'json',
        'numOfRows' : '1'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        item = data['body']['items']
        if item:
            product_info = {
                "nutrient": item[0]['item']['nutrient'],
                "allergy": item[0]['item']['allergy']
            }

            return product_info
        else:
            print(f"'{product_name}'에 대한 정보가 없습니다.")
            return None
    else:
        print(response.url)
        print("성분 정보 API 요청 실패:", response.status_code)
        return None
    

