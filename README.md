# Cartoomization
### Feature
- 이미지를 이하의 순으로 카툰화 한다.
1. canny로 엣지 검출
2. getStructuringElement로 엣지 강화
3. edge를 마스크로 쓰기 위해 반전
4. stylization으로 픽셀화
5. 엣지와 픽셀화 이미지 합성
6. 원본 이미지와 카툰 이미지를 9:11 비율로 합성
### Good Case
![image](https://github.com/andrew0416/Cartoonization/assets/5708754/ff9767c9-d267-4046-8341-a924ce8bd2d3)
![image](https://github.com/andrew0416/Cartoonization/assets/5708754/37d4b325-760d-4f7d-adc4-bad6a6db963e)
<br>
- 아마존 숲이 카툰처럼 잘 바뀌었다
### Bad Case
![image](https://github.com/andrew0416/Cartoonization/assets/5708754/12f30111-2c8d-4993-8dc0-1e5ccc8ea23c)
![image](https://github.com/andrew0416/Cartoonization/assets/5708754/8057cb00-bf33-47d0-abe1-03c52a46a64a)
<br> 
- 카툰화하는 과정에서 눈 같은 신체 부위가 이상하게 변했다.
- 줄무늬 옷이나 뜨개질 옷 같은 부분이 어색하다
### Limitation
- 뭉뚱그려서 표현하여도 분위기를 충분히 알 수 있는 배경의 경우 충분히 만화처럼 묘사된다.
- 하지만 사람과 같이 세밀한 묘사가 중요하고 작은 변화가 큰 분위기의 변화를 가져오는 객체의 경우 상당히 어색하게 보인다
