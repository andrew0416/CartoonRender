import cv2

def cartoonize_image(image):
    # 엣지 검출
    edges = cv2.Canny(image, 100, 200)
    
    # 엣지 강화
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    edges = cv2.dilate(edges, kernel)
    
    # 픽셀화
    color = cv2.stylization(image, sigma_s=200, sigma_r=0.9)
    
    # 엣지와 픽셀화된 이미지 합성
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return color

# 이미지 읽기
input_image = cv2.imread('human2.webp')

# 카툰 렌더링
output_image = cartoonize_image(input_image)

# 결과 출력
cv2.imshow('Cartoonized Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()