import numpy as np

a=np.array([1,3.9,-9,2])#넘파이는 c,c++로 만들어 짐.
print(a,a.ndim, a.shape, a.dtype) #데이터분석에 사용 pandas도 많이 사용
b= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(b, b.ndim, b.shape, b.dtype, b.strides)

c= np.array([[[1,2,3,4],[5,"6",7,8],[9,10,11,12]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(c, c.ndim, c.shape, c.dtype)
# ndim: 배열의 차원 수 shape: 배열의 차원과 크기를 나타냄 dtype: 데이터 타입
##float64는 c의 double m

