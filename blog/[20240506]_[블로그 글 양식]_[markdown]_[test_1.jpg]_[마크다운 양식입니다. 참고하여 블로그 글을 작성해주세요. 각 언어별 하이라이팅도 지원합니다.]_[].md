데이터베이스(Database) 란?
데이터베이스는 컴퓨터 전공자가 아니더라도 우리의 일상생활에서 자주 접하는 용어 중 하나 일 것이다. 예를 들어, 인터넷 쇼핑몰에서 상품을 주문하거나, 학교에서 성적을 조회하거나, 은행에서 계좌를 관리할 때 등 다양한 상황에서 데이터베이스가 쓰인다. 데이터베이스는 어렵게 생각할 필요없이 데이터들을 저장하고 조회하는 프로그램이다. 쇼핑몰의 경우 상품 정보, 고객 정보, 주문 정보 데이터를 데이터베이스에서 가져와 조회하거나 정보를 저장하는 것이다. 
 
데이터베이스의 필요성
데이터를 저장하고 조회한다는 관점에서 어찌 보면 파일들을 폴더에 저장하여 정리하고 파일을 검색해서 조회하는 윈도우 파일 탐색기와 비슷해 보일수 있다. 하지만 데이터베이스는 이러한 단순한 데이터 저장소 개념을 넘어선 상위 호환 격이다. 데이터베이스는 프로그래밍과 같은 컴퓨터 언어(SQL)로 세밀히 제어가 가능하고, 어떻게 제어하느냐에 따라 성능이 천차 만별이다. 또한 데이터들끼리 중복된 정보가 있을 경우 이를 통합하여 구조적이며 효율적으로 데이터를 저장한다. 거기다 데이터베이스는 컴퓨터 언어로 제어가 가능하고 앱이나 웹을 통해 전세계로 공유가 가능하다.

이처럼 데이터베이스는 파일을 조직적으로 통합하여 자료 항목의 중복을 최대한 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체라고 할 수 있다.


데이터베이스의 데이터 특징
데이터베이스는 단순이 아무 데이터나 마구잡이로 저장해 놓지 않고 구조적인 형태를 유지하기 위해 나름 효율적인 데이터 저장 규칙이 존재한다.
 
통합된 데이터 (Integrated Data)
여러가지의 데이터를 통합하여 저장하는데 중복된 정보가 있다는 이를 그대로 저장하면 용량 낭비가 발생하는 비효율적인 현상이 발생한다. 그래서 데이터베이스는 이러한 중복된 정보에 대해서 데이터를 통합하여 자료의 중복을 최소화한 데이터의 모임으로 구성한다.

저장된 데이터 (Stored Data)
우리가 사진이나 동영상 파일을 하드디스크나 SSD에 저장하는 것처럼, 데이터베이스도 컴퓨터가 접근할 수 있는 매체에 데이터를 저장한다.

운영 데이터 (Operational Data)
데이터베이스는 주로 조직의 목적을 위해 존재하고 활용되는 운영 데이터를 다루는데 주요 이용된다. 예를 들어, 쇼핑몰의 경우 판매량이나 재고량 등이 운영 데이터이다. 단순하거나 임시적으로 데이터 저장이 필요하다면 굳이 무거운 데이터베이스 소프트웨어를 사용할 필요가 없고 그냥 폴더에 저장해 버리면 된다.

공유 데이터 (Shared Data)
여러 사람들이 공유하고 사용할 목적으로 통합 관리되는 데이터를 말한다. 아마 데이터베이스라는 소프트웨어를 사용하는 가장 근본적인 이유이기도 하다. 하나의 컴퓨터나 시스템을 위한 데이터가 아니라 여러 시스템들이 공용으로 엑세스하여 이용한다.  예를 들어, 쇼핑몰의 경우 판매자와 구매자가 같은 상품 정보를 보는걸 들 수 있다.
데이터베이스의 기능 특징
데이터베이스는 이러한 특수한 특징을 가진 데이터들을 효율적으로 관리하기 위해 다음과 같은 기능을 제공한다.

실시간 접근성 (Real-Time Accessibility)
데이터베이스는 사용자의 요구에 신속하고 정확하게 응답이 가능해야 한다. 예를 들어, 쇼핑몰 온라인의 경우 고객이 원하는 상품을 검색하거나 주문하는 것을 말한다.
 
계속적인 변화 (Continuous Evolution)
현실 세계의 변화를 반영하기 위해 새로운 데이터의 삽입(Insert), 삭제(Delete), 갱신(Update)로 항상 최신의 데이터를 유지하는 것을 말한다. 예를 들어, 쇼핑몰의 경우 상품 정보나 가격 정보를 상황에 따라 계속 변경할 수 있다.
 
동시 공용 (Concurrent Sharing)
다수의 사용자가 동시에 같은 내용의 데이터를 이용할 수 있어야 한다. 예를 들어, 쇼핑몰의 경우 여러 고객이 동시에 같은 상품을 조회하거나 구매할 수 있다.
 
내용에 의한 참조 (Content Reference)
데이터베이스에 있는 데이터를 참조할 때 사용자의 요구에 따른 데이터 내용으로 데이터의 위치나 주소로 데이터를 찾는다. C언어의 포인터나, URL 주소를 떠올리면 된다. 
 
데이터베이스의 언어 종류
본문 상단에서 데이터베이스는 컴퓨터 언어로 통신한다고 말했었다. 마치 프로그래밍과 비슷하다고 볼 수 있는데, 이러한 데이터베이스와 소통하기 위해 사용하는 언어를 데이터베이스 언어(Database Language)라고 한다. 그리고 데이터베이스 언어 중에서 가장 많이 사용되는 것이 여러분이 한번 쯤 들어본 SQL(Structured Query Language)이다. SQL은 관계형 데이터베이스에서 데이터를 정의하고 조작하고 제어할 수 있는 표준 언어로서, 대부분의 데이터베이스 시스템에서 지원한다. 그리고 데이터를 조회하느냐 삭제하느냐 생성하느냐에 따라 데이터베이스 언어는 크게 다음과 같이 4 가지로 나뉘게 된다.

