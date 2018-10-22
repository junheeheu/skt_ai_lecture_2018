2018년 영상인식 강좌의 실습을 위한 Code
================================

- 본 Code는 SKT에 모든 권한이 있다.
- 본 Code는 2018년 영상인식 강좌의 실습을 하는 학생들을 위한 한시적 사용을 목적으로 하고 있으며, 강좌 이외의 목적으로 활용될 수 없다.

실습 항목
------------------------
* Image Load by OpenCV
* Draw Rectangle for a face on the image by OpenCV
* Regist Gallery Face Image using postman
* Recognize a Face

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

