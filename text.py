import numpy as np
import matplotlib.pyplot as plt

# 입력 이미지 (5x5)
input_image = np.array([
    [1, 2, 0, 1, 0],
    [0, 1, 2, 1, 1],
    [1, 0, 1, 2, 0],
    [2, 1, 0, 1, 1],
    [0, 1, 2, 0, 1]
])

# 필터 (3x3)
filter = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

# 합성곱 연산 수행
output_image = np.zeros((3, 3))

for i in range(3):
    for j in range(3):
        region = input_image[i:i+3, j:j+3]
        output_image[i, j] = np.sum(region * filter)

# 결과 시각화
fig, axes = plt.subplots(1, 3, figsize=(10, 3))

axes[0].imshow(input_image, cmap='gray')
axes[0].set_title('입력 이미지')

axes[1].imshow(filter, cmap='gray')
axes[1].set_title('필터')

axes[2].imshow(output_image, cmap='gray')
axes[2].set_title('출력 이미지')

plt.show()
