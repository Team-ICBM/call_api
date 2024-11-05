from product_info import get_product_info_by_barcode, get_nutrition_info_by_name

def main():
    
    api_key_name = "b0db4232c70c49289cd0"

    api_key_detail = "oqdC/qEnEV/uF3Vy2pVZd4qFqZQTJkEVnv4wvLJIP/adzKf/BOn5/zQSQ/g0mEV5s53E7bSwXJ5wz0V8UNbGlw=="
    
    # 바코드 입력 받기
    barcode = input("바코드를 입력하세요: ")

    # 1. 바코드를 통해 제품 정보 가져오기
    product_info = get_product_info_by_barcode(barcode, api_key_name)
    if product_info:
        # 제품 정보에서 이름 추출

        # product_name = product_info.get("PRDLST_NM", "이름 정보 없음")

        product_name = "매일우유 오리지널"
        # 콘솔에 제품 이름 출력
        print("제품 이름:", product_name)

        
        # 2. 제품 이름을 이용하여 알러지 & 영양 정보 가져오기
        detail_info = get_nutrition_info_by_name(product_name, api_key_detail)
        
        if detail_info:
            nutrient = detail_info.get("nutrient", "영양 정보 없음")
            allergy = detail_info.get("allergy", "알러지 정보 없음")

            print("영양 정보 : ", nutrient)
            print("알러지 정보 : ", allergy)
            
        else:
            print("영양 성분 정보를 찾을 수 없습니다.")
    else:
        print("제품 정보를 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
