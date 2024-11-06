from product_info import get_product_info_by_barcode, get_nutrition_info_by_report_no

def main():
    
    api_key_name = "b0db4232c70c49289cd0"
    api_key_detail = "oqdC/qEnEV/uF3Vy2pVZd4qFqZQTJkEVnv4wvLJIP/adzKf/BOn5/zQSQ/g0mEV5s53E7bSwXJ5wz0V8UNbGlw=="
    
    
    # 바코드 입력 받기
    barcode = input("바코드를 입력하세요: ")

    # 1. 바코드를 통해 제품 정보 가져오기
    product_info = get_product_info_by_barcode(barcode, api_key_name)
    if product_info:
        # 제품 정보에서 (이름 & 제품 번호) 추출
        product_name = product_info.get("PRDLST_NM", "이름 정보 없음")
        report_no = product_info.get("PRDLST_REPORT_NO", "번호 없음")
        
        # 콘솔에 제품 이름 출력
        print("1. 제품 이름:", product_name)

        
        # 2. 제품 번호를 이용하여 (알러지 & 영양 정보) 가져오기
        detail_info = get_nutrition_info_by_report_no(report_no, api_key_detail)
        
        if detail_info:
                nutrient = detail_info.get("nutrient", "영양 정보 없음")
                allergy = detail_info.get("allergy", "알러지 정보 없음")

                print("\n3. 영양 정보: ", nutrient)
                print("\n4. 알러지 정보: ", allergy)
                
        else:
                print("영양 성분 정보를 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
 

# 가능한 제품 

    # 오뚜기 진라면 순한맛
    # 바코드 번호 : 8801045571362
    # 제품 report_no : 19860309018680
    # 알러지 ..


    # 엄마사랑듬뿍삼각김밥김
    # 바코드 번호 : 8801266301373
    # report_no : 2003035813726
    # 알러지 : 알 수 없음


    # 참군고구마칩
    # 바코드 번호 : 8809678470007
    # report_no : 201903787252
    # 알러지 : 없음