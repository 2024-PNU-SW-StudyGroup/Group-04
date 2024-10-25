### 1. 프로젝트 소개
#### 1.1. 개발배경 및 필요성
> 이 프로젝트는 컴퓨터공학, 기계공학, 전기전자공학, 항공우주공학이 모두 융합되어있는 항공우주 기술 연구의 일환으로 시작되었다. ASTRO 위성부는 이에 따라 정보컴퓨터공학과 3명과 타 학과 수명이 연합해 구성되어있으며, 교육용으로 제작되는 캔위성을 제작하여 항공우주의 대중화에 앞장서려 하고 있다. <br/>
> 우리가 살고 있는 정보화 시대에서 우리가 가장 흔히 접하지만, 그 원리나 활용에 있어 가장 낯선 분야라고 할 수 있는 통신에 관해 우선 알려보려고 하고 있다. 대학생 수준에서 흔히 접하는 통신 방식은 기껏해야 블루투스이며, 조금 더 나아간다면 wifi 정도가 있을 것이다. 그러나 이러한 통신 방식을 직접 구현하고 제어하는 경우는 손에 꼽는다. <br/>
> 가장 대표적인 통신 방법인 2.4GHz 와이파이 통신 또한 단순히 단거리 핫스팟 정도로 여기는 것이 전부인만큼, 학부생이 막상 제대로 된 프로젝트를 진행하게 되면 통신 연결이 바르게 되지 않아 구현에 실패하는 경우가 많다. <br/>
> 실제로 본 팀 또한 915MHz의 라디오 통신을 통해 로켓의 데이터를 수신하려 했으나 실패한 적이 있으며, 같은 대회에 참가한 팀의 80% 가량이 통신 실패를 경험했다. <br/>
> 이에 따라 우리 위성부는 우리나라 국토 전지역에 펼쳐져있는 LTE 망을 활용하며, 동시에 인터넷의 계층들을 활용할 수 있는 방법을 연구하여 로켓뿐만 아니라 드론, 위성, 자동차 등에 모두 사용될 수 있는 무선통신 방식을 연구하고자 한다.
<br/>

#### 1.2. 개발목표 및 주요내용
> 1. LTE 통신망을 활용, 캔위성의 데이터를 최단시간 내에 원활히 전송
> 2. 2.4GHz, 5.8GHz 대역의 통신용 안테나 제작 및 테스트
> 3. 위성의 자세 분석 및 제어
<br/>

#### 1.3. 세부내용
> ○ 요구사항 분석
> 1. 해당 위성은 발사 및 사출, 낙하 시의 충격에도 불구하고 항시 통신이 작동가능해야 한다.
> 2. 통신 속도는 최소 100Mbps 이상의 통신속도를 보장해야 하며 1080p 수준의 MP4 규격 영상을 실시간으로 송출이 가능해야한다.
> 3. 해당 웹서버는 음성, 영상, 텍스트 등의 매체를 모두 저장 및 송수신이 가능해야한다.
>
> ○ 제한사항
> 1. 해당 통신 시스템은 지름 100mm, 높이 200mm의 원통형 용기 안에 집적될 수 있는 크기여야한다.
> 2. 해당 위성은 고도 400m 이상에서 통신이 가능해야 한다.
> 3. 음속 이상의 속도로 이동하는 상황에서 통신이 끊김 없이 이어져야 한다.
> 
> ○ 개발 환경
> 1. 리눅스 기반 운영체제
> 2. 파이썬 API 및 웹 서버 구축
> 3. 위성 구동을 위한 C++ 개발환경
> 4. 지상국 시스템(파이썬 GUI)
<br/>

#### 1.4. 기존 서비스(상품) 대비 차별성
> 기존의 불안정한 433MHz, 915MHz 대역의 저가형 RF 통신들을 대체하여 LTE 방식의 통신을 사용하게 되어 훨씬 더 높은 수준의 데이터를 실시간으로 송수신 할 수 있게 되며, 동시에 이를 활용하여 즉시 API와 연계할 수 있게 될 것이다. <br/>
> 이는 곧 기존에는 그저 발사 – 회수 – 분석 및 사후 강평으로 구성되던 로켓 및 캔위성 발사대회가, 발사 - 데이터 수집 - API 적용 – 현장 분석 – 회수 – 사후 강평으로 아예 새로운 방식으로 이어지도록 할 수 있다. <br/>
> 예를 들어, 기존의 캔위성 대회에서 수상한 산불 감시 캔위성의 경우 대회 당일에 할 수 있는 일은 그저 사진 촬영이 전부며, 대회 후 수집된 데이터를 분석하여 차후에 해당 현장에 산불이 발생했을 것이라고 발표할 뿐이었다.<br/>
> 이는 실질적으로는 아무런 의미가 없는 요식행위였으나, 현재 개발예정인 LTE 통신을 활용하게 될 시 발사 후 촬영된 사진을 캔위성이 즉시 API를 통해 분석, 산불 감지를 경고하고 대처할 수 있는 실용성을 지니게 될 것이다.
<br/>

#### 1.5. 사회적가치 도입 계획
> 본 프로젝트를 성공적으로 완료되게 되면 해당 기술을 공개하여 전국의 모든 학부생들이 이를 활용하여 각자 실용적인 캔위성들을 만들 수 있도록 지원할 계획이며, 이는 항공우주 기술을 접근하는 대학생들에게 보다 실전적이고 유의미한 활동의 기회가 되어 줄 것이다. <br/>
> 자연히 이는 산업 및 연구 현장에 한걸음 더 가까이 다가가게 해주는 가치 있는 경험이 될 것이며, 우리나라는 이를 통해 현장 경험을 가진 연구 인력들을 충분히 확보, 우주경쟁에 있어 한걸음 진보하게 될 것으로 기대한다.
<br/>


### 2.상세설계
#### 2.1. 시스템 구성도(개념도 미구현)
> 아래 시스템의 구성도 설명 내용 . 
<img width="600px" alt="시스템 구성도" src="https://github.com/pnuswedu/SW-Hackathon-2024/assets/34933690/f0e7c7ed-deb1-47ee-8090-32f712fa2b23">
<br/>

#### 2.3. 사용기술
| 이름                    | 버전    |
|:-----------------------:|:-------:|
| Python                  | 3.9.2   |
| Flask                   | 2.1.0   |
| Ubuntu                  | 20.04   |
| GNU Compiler Collection | 9.3.0   |
| GNU Make                | 4.2.1   |

<br/>


### 3. 개발결과
[코딩역량강화플랫폼 Online Judge](http://10.125.121.115:8080/)를 예시로 작성하였습니다.
#### 3.1. 전체시스템 흐름(도식도 미구현)
- 캔위성 <-> flask web server <-> 지상국 web server 플로우 차트
  > 전파의 Raw data 수신 <br/>
  > UNIX 도메인 소켓을 사용하여 C++와 Python 간 통신 <br/>
  > flask를 이용하여, raw data를 HTTP/3로 UDP 통신 프로토콜 사용하여 지상국으로 데이터 전송 <br/>

- 지상국 web에서 데이터 확인 및 전처리
  > 캔 위성에서 받아온 데이터의 에러 체킹 및 pre-processing <br/>
  > ML 혹은 DL로 전처리된 데이터 평가하여 전파 탐지 확인
  > 지상에서 관측된 전파 데이터와 비교하기 

<br/>

#### 3.2. 기능설명
##### ` 캔위성 데이터 수집 과정(c++내용)`
-  HOW TO 데이터 수집..
<br/>

##### ` 캔위성 통신과정(flask 내용 기술) `
- 통신과정
  - 세부 통신 과정 (모듈 설명?)
 
##### ` 전파 탐지 비교 `
- 받아온 데이터와 지상관측 데이터 비교


<br/>

#### 3.4. 디렉토리 구조(구현중)
##### ` 캔위성 내부 라즈베리 파이`(구현 예정)
```
├── build/                      # webpack 설정 파일
├── config/                     # 프로젝트 설정 파일
├── deplay/                     # 배포 설정 파일
├── src/                        # 소스 코드
│   ├── assets/                 # 이미지, 폰트 등의 정적 파일
│   ├── pages/                  # 화면에 나타나는 페이지
│   │   ├── page1/              # 페이지1
│   │   ├── page2/              # 페이지2
│   │   ├── components/         # 여러 페이지에서 공통적으로 사용되는 컴포넌트
│   ├── router/                 # 라우터
│   ├── store/                  # global state store
│   ├── styles/                 # 스타일
│   ├── utils/                  # 유틸리티
├── static/                     # 정적 파일
```

##### ` 지상국 내부 폴더`(구현 예정)
```
├── build/                      # webpack 설정 파일
├── config/                     # 프로젝트 설정 파일
├── deplay/                     # 배포 설정 파일
├── src/                        # 소스 코드
│   ├── assets/                 # 이미지, 폰트 등의 정적 파일
│   ├── pages/                  # 화면에 나타나는 페이지
│   │   ├── page1/              # 페이지1
│   │   ├── page2/              # 페이지2
│   │   ├── components/         # 여러 페이지에서 공통적으로 사용되는 컴포넌트
│   ├── router/                 # 라우터
│   ├── store/                  # global state store
│   ├── styles/                 # 스타일
│   ├── utils/                  # 유틸리티
├── static/                     # 정적 파일
```
<br/>


### 4. 설치 및 사용 방법(미수정)
**필요 패키지(캔위성)**
- 위의 사용 기술 참고

```bash
$ git clone https://github.com/test/test.git
$ cd test/frontend
$ npm i
$ export NODE_ENV="development" # windows: set NODE_ENV=development
$ npm run build:dll
$ export TARGET="http://localhost:8000"  # windows: set NODE_ENV=http://localhost:8000
$ npm run dev
```
<br/>

**필요 패키지(지상국)**
- 위의 사용 기술 참고

```bash
$ git clone https://github.com/test/test.git
$ cd test/frontend
$ npm i
$ export NODE_ENV="development" # windows: set NODE_ENV=development
$ npm run build:dll
$ export TARGET="http://localhost:8000"  # windows: set NODE_ENV=http://localhost:8000
$ npm run dev
```
<br/>


### 5. 소개 및 시연영상 (현재 구현 중, 추후 추가 예정)

<br/>

### 6. 팀 소개
| 이승재 | 정연수 | 윤주연 | 배소연 | 김준우 | 주기윤 |
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|<img width="100px" alt="MEMBER1" src="https://github.com/pnuswedu/SW-Hackathon-2024/assets/34933690/f5b5df2a-e174-437d-86b2-a5a23d9ee75d" /> | <img width="100px" alt="MEMBER2" src="https://github.com/pnuswedu/SW-Hackathon-2024/assets/34933690/fe4e8910-4565-4f3f-9bd1-f135e74cb39d" /> | <img width="100px" alt="MEMBER3" src="https://github.com/pnuswedu/SW-Hackathon-2024/assets/34933690/675d8471-19b9-4abc-bf8a-be426989b318" /> |<img width="100px" alt="MEMBER1" src="https://github.com/pnuswedu/SW-Hackathon-2024/assets/34933690/f5b5df2a-e174-437d-86b2-a5a23d9ee75d" /> | <img width="100px" alt="MEMBER2" src="https://github.com/pnuswedu/SW-Hackathon-2024/assets/34933690/fe4e8910-4565-4f3f-9bd1-f135e74cb39d" /> | <img width="100px" alt="MEMBER3" src="https://github.com/pnuswedu/SW-Hackathon-2024/assets/34933690/675d8471-19b9-4abc-bf8a-be426989b318" /> |
| member1@pusan.ac.kr | member2@gmail.com | member3@naver.com | member1@pusan.ac.kr | member2@gmail.com | member3@naver.com |
| c++ 데이터 전송 구현 | 인프라 구축 <br/> flask 프레임워크 개발 | LTE 통신 구현 | 통신 인프라 구축 <br/> (지상국) | 통신 인프라 구축 <br/> (캔위성) | 통신 인프라 구축 <br/> (캔위성) |


<br/>


### 7. 참여 후기 (최종때 작성)
- MEMBER1
  > 작성하세요.
- MEMBER2
  > 작성하세요.
- MEMBER3
  > 작성하세요.
- MEMBER4
  > 작성하세요.
- MEMBER5
  > 작성하세요.
- MEMBER6
  > 작성하세요.
<br/>
