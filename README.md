# Image-to-Image Generator

이 프로젝트는 딥러닝을 사용하여 입력 이미지를 다른 스타일이나 형태로 변환하는 이미지 생성 도구입니다.

## 설치 방법

```bash
# 저장소 클론
git clone https://github.com/SOSONAGI/image-to-image-generator.git
cd image-to-image-generator

# 필요한 패키지 설치
pip install -r requirements.txt
```

## 사용 방법

```python
from src.generator import ImageGenerator

# 생성기 초기화
generator = ImageGenerator()

# 이미지 로드 및 생성
input_image = generator.load_image('path/to/input/image.jpg')
output_image = generator.generate(input_image)

# 결과 저장
generator.save_image(output_image, 'path/to/output/image.jpg')
```

## 프로젝트 구조

```
├── requirements.txt
├── src/
│   ├── generator.py     # 이미지 생성 모델
│   └── utils.py         # 유틸리티 함수
```

## 향후 계획

- [ ] 다양한 스타일 변환 모델 추가
- [ ] 웹 인터페이스 구현
- [ ] 배치 처리 기능 추가

## 라이선스

MIT License