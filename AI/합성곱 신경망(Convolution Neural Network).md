# 합성곱 신경망(Convolution Neural Network)



Sub Project 1의 명세서에서 CNN에대해 자세히 다루고 있다. 이미지를 처리하는 프로젝트이다보니 중요할 것 같아서 https://wikidocs.net/64066 를 참고해 공부하면서 정리를 해보았다

[위키독스](https://wikidocs.net/64066)

- 합성곱 신경망은 크게 합성곱층과(Convolution layer)와 풀링층(Pooling layer)으로 구성

![https://wikidocs.net/images/page/64066/convpooling.PNG](https://wikidocs.net/images/page/64066/convpooling.PNG)

> 그림에서 CONV는 합성곱 연산을 의미하고, 합성곱 연산의 결과가 활성화 함수 ReLU를 지납니다. 이 두 과정을 합성곱층이라고 합니다. 그 후에 POOL이라는 구간을 지나는데 이는 풀링 연산을 의미하며 풀링층이라고 합니다.

### 합성곱 연산

합성곱층은 합성곱 연산을 통해서 이미지의 특징을 추출하는 역할이다.

**커널(kernel)** 또는 **필터(filter)**라는 n×m 크기의 행렬로 **높이(height)×너비(width)** 크기의 이미지를 처음부터 끝까지 겹치며 훑으면서 n×m크기의 겹쳐지는 부분의 각 이미지와 커널의 원소의 값을 곱해서 모두 더한 값을 출력으로 하는 것을 말합니다

- 첫번째 스텝

![https://wikidocs.net/images/page/64066/conv4.png](https://wikidocs.net/images/page/64066/conv4.png)

- 두번째 스텝

![https://wikidocs.net/images/page/64066/conv5.png](https://wikidocs.net/images/page/64066/conv5.png)

- 세번째 스텝

![https://wikidocs.net/images/page/64066/conv6.png](https://wikidocs.net/images/page/64066/conv6.png)

- 네번째 스텝

![https://wikidocs.net/images/page/64066/conv7.png](https://wikidocs.net/images/page/64066/conv7.png)

- 특성 맵

  위와 같이 입력으로부터 커널을 사용하여 합성곱 연산을 통해 나온 결과를 **특성 맵(feature map)**이라고 한다.

  커널의 이동 범위가 위의 예제에서는 한 칸이었지만, 이 또한 사용자가 정할 수 있고 이 이동 범위를 **스트라이드(stride)**라고 합니다.

  ![https://wikidocs.net/images/page/64066/conv9.png](https://wikidocs.net/images/page/64066/conv9.png)

### 패딩

위의 예처럼 5 x 5 이미지에 3 x 3커널로 스트라이드를 1로 합성곱 연산을 하면 3 x 3 특성 맵을 얻는다.

합성곱 연산 이후에도 특성 맵의 크기가 입력의 크기와 동일하게 유지되도록 하고 싶다면 패딩(padding)을 사용하면 된다

![https://wikidocs.net/images/page/64066/conv10.png](https://wikidocs.net/images/page/64066/conv10.png)

### 가중치와 편향

- 가중치

  3 × 3 이미지를 처리한다고 가정해보자. 2 × 2 커널을 사용하고, 스트라이드는 1로 한다.

![https://wikidocs.net/images/page/64066/conv12.png](https://wikidocs.net/images/page/64066/conv12.png)

![https://wikidocs.net/images/page/64066/conv13.png](https://wikidocs.net/images/page/64066/conv13.png)

- 편향

  편향도 당연히 추가할 수 있다..

  편향은 커널을 적용한 뒤에 더할 수 있다.

  ![https://wikidocs.net/images/page/64066/conv14.png](https://wikidocs.net/images/page/64066/conv14.png)

  ### 특성 맵의 크기 계산 방법

  이건 너무 잘 정리 되어있어서 그냥 가져왔다.

  ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9f50fcca-9510-49b1-8c68-5c21fd8c46a9/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9f50fcca-9510-49b1-8c68-5c21fd8c46a9/Untitled.png)

### 3차원 텐서의 합성곱 연산

![https://wikidocs.net/images/page/64066/conv15.png](https://wikidocs.net/images/page/64066/conv15.png)

3차원 텐서의 합성곱을 하려면 데이터의 채널 수와 커널의 채널 수는 같아야 한다.

합성곱 연산을 채널마다 수행한다. 그리고 그 결과를 모두 더하여 최종 특성 맵을 얻는다.

주의 : 위의 연산에서 사용되는 커널은 3개의 커널이 아니라 3개의 채널을 가진 1개의 커널이라는 점(하지만 아직 무슨말인지 모르겠다;;;)