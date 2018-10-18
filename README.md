2018년 영상인식 강좌의 실습을 위한 Code
================================

- 본 Code는 SKT에 모든 권한이 있다.
- 본 Code는 2018년 영상인식 강좌의 실습을 하는 학생들을 위한 한시적 사용을 목적으로 하고 있으며, 강좌 이외의 목적으로 활용될 수 없다.

Code 동작 환경
------------------------
* OS: Ubuntu 16.04 64bit
* 개발환경: python2.7
* 관련 dependency
  * sudo apt-get install python2.7-dev python-pip
  * sudo pip install -U pip==9.0.3
  * sudo pip install jupyter
  * sudo apt-get install libopencv-dev python-opencv
  * sudo pip install matplotlib

만약 Ubuntu 환경이 없다면
------------------------
* AWS (Amazon Web Service)를 통해 환경을 무료로 제공 받을 수 있다.
  * [AWS사용설명서](https://drive.google.com/open?id=1oDysftiGrr3yo3qX1jfLJmiRu8xhiNRd62tjk5LvdgQ)

AWS 실습 환경 사용 방법
------------------------

* 접속 방법
~~~
$ ssh -i /path/to/your_key.pem -L 8888:127.0.0.1:8888 ubuntu@your.aws.ip.add 
~~~
ex:
~~~
$ ssh -i ~/Downloads/skt_lecture.pem -L 8888:127.0.0.1:8888 ubuntu@52.79.44.222 
~~~

* 접속 후 jupyter notebook 실행
~~~
$ jupyter notebook
~~~

현재 사용되는 인식 엔진에 대해
------------------------

* 현재 사용되는 인식 엔진은
  * 얼굴 검출은 정면으로 제한된다.
  * 한 사람에 대한 결과만 return 한다.
    * 얼굴이 2개 이상일 경우, 결과 return의 기준은 얼굴의 크기로 정의된다.
* 학기 프로젝트를 위해 사용이 필요한 경우 junhee.heu_at_sk.com 으로 연락 요망

* 관련 사용법은 [사용설명서](https://drive.google.com/open?id=1xdimVwZrJDpLWi5YQWzTPKJZ-1Cbf0fcQdnPoTLYbNc) 를 참고한다.
* Gallery 등록을 위해 ([postman_collection파일_Download_Link_1](https://drive.google.com/open?id=1vHNmktm4SE9MIIBXWY1s9qh6eGJjVNxY) or [postman_collection파일_Download_Link_2](https://github.com/junheeheu/skt_ai_lecture_2018/blob/master/VIC%20API.postman_collection.json))을 다운받아 사용한다.

* https://github.com/junheeheu/skt_ai_lecture_2018