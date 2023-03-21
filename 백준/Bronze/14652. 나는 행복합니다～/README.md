# [Bronze V] 나는 행복합니다~ - 14652 

[문제 링크](https://www.acmicpc.net/problem/14652) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

수학, 사칙연산

### 문제 설명

<p>“나는 행복합니다~ 한화라서 행복합니다~”</p>

<p>행복한 이 노래 가사! 그렇다. 욱제는 한화 이글스의 열렬한 <!--[if gte vml 1]><v:shapetype id="_x0000_t75"
 coordsize="21600,21600" o:spt="75" o:preferrelative="t" path="m@4@5l@4@11@9@11@9@5xe"
 filled="f" stroked="f">
 <v:stroke joinstyle="miter"/>
 <v:formulas>
  <v:f eqn="if lineDrawn pixelLineWidth 0"/>
  <v:f eqn="sum @0 1 0"/>
  <v:f eqn="sum 0 0 @1"/>
  <v:f eqn="prod @2 1 2"/>
  <v:f eqn="prod @3 21600 pixelWidth"/>
  <v:f eqn="prod @3 21600 pixelHeight"/>
  <v:f eqn="sum @0 0 1"/>
  <v:f eqn="prod @6 1 2"/>
  <v:f eqn="prod @7 21600 pixelWidth"/>
  <v:f eqn="sum @8 21600 0"/>
  <v:f eqn="prod @7 21600 pixelHeight"/>
  <v:f eqn="sum @10 21600 0"/>
 </v:formulas>
 <v:path o:extrusionok="f" gradientshapeok="t" o:connecttype="rect"/>
 <o:lock v:ext="edit" aspectratio="t"/>
</v:shapetype><v:shape id="그림_x0020__x0025_d_x0020_1" o:spid="_x0000_i1027"
 type="#_x0000_t75" style='width:12pt;height:17pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="file:////Users/baekjoon/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image001.png"
  o:title=""/>
</v:shape><![endif]--><img src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14652/1.png" style="height:18px; width:12px">이다. 욱제는 여름방학을 맞아 치킨과 맥주를 챙겨 야구장을 방문했다! 하지만 이게 웬걸? 치맥에 정신이 팔린 욱제는 그만 자신의 관중석 위치가 담긴 티켓을 잃어버리고 말았다. 욱제가 유일하게 기억하는 것이라고는 자신의 관중석 번호 K뿐이다.</p>

<p>당신은 한화 이글스의 감독이다. 열혈<!--[if gte vml 1]><v:shape
 id="그림_x0020__x0025_d_x0020_2" o:spid="_x0000_i1026" type="#_x0000_t75"
 style='width:12pt;height:17pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="file:////Users/baekjoon/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image001.png"
  o:title=""/>
</v:shape><![endif]--><img src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14652/1.png" style="height:18px; width:12px">인 욱제의 방문에 깊은 감동을 받은 당신은 욱제가 잃어버린 자리를 찾아주려고 한다. 오늘 경기가 펼쳐지는 잠실구장은 세로 길이가 N, 가로 길이가 M인 N≤M 크기의 관중석을 가지고 있다. 관중석의 왼쪽 위는 (0, 0), 오른쪽 아래는 (N-1, M-1)으로 표시된다. 각 관중석에는 번호가 아래 그림처럼 매겨져있다. (0, 0)에서부터 0번으로 시작하여 오른쪽으로, 끝에 다다르면 그 아래에서 또 오른쪽으로 숫자가 증가해나가는 식이다.</p>

<p style="text-align: center;"><!--[if gte vml 1]><v:shape
 id="그림_x0020__x0025_d_x0020_3" o:spid="_x0000_i1025" type="#_x0000_t75"
 style='width:207pt;height:146pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="file:////Users/baekjoon/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image004.png"
  o:title=""/>
</v:shape><![endif]--><img src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14652/2.png" style="height:146px; width:207px"></p>

<p>당신은 관중석의 크기와 욱제 자리의 번호를 알고 있다. 욱제가 잃어버린 자리는 어디일까? 자리를 찾아서 욱제에게 알려주도록 하자!</p>

### 입력 

 <p>첫째 줄에 관중석의 크기를 나타내는 N, M과 잃어버린 관중석 번호를 나타내는 K가 주어진다. (1 ≤ N, M ≤ 30,000, 0 ≤ K ≤ N×M-1)</p>

### 출력 

 <p>욱제의 잃어버린 자리를 찾아서, 잃어버린 자리의 좌표 (n, m)를 하나의 공백을 사이에 두고 숫자만 출력한다.</p>

