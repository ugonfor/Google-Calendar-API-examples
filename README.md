# Let's Use Google Calendar API
## 구글 캘린더 API

공식 레퍼런스 사이트 : https://developers.google.com/calendar
Sample 확인 가능 사이트 : https://developers.google.com/calendar/quickstart/python
Python reference : https://developers.google.com/calendar/v3/reference
참고할만한 사이트 : https://ai-creator.tistory.com/19

## How to Use?
Sample 확인 가능 사이트를 확인해보면 사용방법과 예시를 자세하게 볼 수 있으니 참고.
credentials.json을 처리하는 과정이 처음에는 익숙하지 않아 위 사이트에서 만들어주는 quickstart 프로젝트로 사용함.


## Why do
구글 캘린더를 사용하는 곳이 굉장히 많아짐으로써 이를 가공해서 나의 캘린더에 적용해보고자 함.

1. BoB 강의들 이름으로 분류해서 특정 조건을 만족하는 강의들만 내 캘린더에 추가하기 [BoB_Calendar.py]
각 강의들의 경우, 트랙에 나눠서 [취], [공] 등의 텍스트로 시작한다.
그래서 내가 들어야 하는 강의에 해당하는 것만 따로 추가하였다.
