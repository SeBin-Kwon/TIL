# Vue

## 기본 설정

mac node/npm 설치

- `brew install node`

> `npm install --legacy-peer-deps`
>
> - 종속성 문제로 인해 삭제 및 재설치를 했지만 그래도 안됐다.
> - 아무래도 최신버전은 오류가 많은 것 같다.

vue 설치

- `sudo npm install -g vue`
- `sudo npm install -g @vue/cli` 

vue 설치 확인

- `vue --version`

프로젝트 설정

- `vue create {project이름}`
- 메뉴 선택
  - 커스텀할 땐 스페이스로 선택 가능
  - Babel를 구버전 브라우저에도 돌아갈 수 있도록 하는 필수요소
  - Router는 메뉴를 클릭했을 때 페이지가 넘어갈 수 있도록 해주는 추가 모듈
    - y 누르고 스탠다드 컨벤션 엔터
    - 저장할 때마다 자스 문법 체크해주기
    - 파일 분리 혹은 패키지 하나로 관리? -> 패키지
    - 즐겨찾기 해놓을 것인가?

vue router 설치

- `npm install vue-router --save`

vue bootstrap 설치

- `npm install vue bootstrap bootstrap-vue`

<br>

main.js

- main.js가 가장 먼저 실행된다.

```js
import { createApp } from 'vue'
import App form './App.vue'

//createApp이라는 함수에 App이라는 vue를 넣어서 index.html에 아이디가 app인 태그를 mount 시키겠다.
createApp(App).mount('#app')
```

App.vue

- `<template>` : html 코드가 들어감
- `<script>` : js 코드가 들어감
- `<style>` : css 코드가 들어감

vue는 index.html 하나로 모든 서비스가 실행된다.

<br>

App.vue

```vue
<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
  </nav>
</template>
```

router > index.js

```javascript
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]
```

- App.vue에 있는 `to`와 router > index.js에 있는 `path`가 일치해야한다.
- 이후 `component`에 해당하는 것을 실행
  - views 폴더에 있는 vue들은 js파일로 컴파일되고 app.js파일에 모두 포함된다.
- `name`은 중복되면 안된다.

<br>

`.prettierrc` 생성

> 코딩 컨벤션 맞춰주기

```json
{
  "semi":false,
  "bracketSpacing": true,
  "singleQuote": true,
  "useTabs": false,
  "trailingComma": "none",
  "printWidth": 80
}
```

package.json 열기

```json
"rules": { "space-before-function-paren": "off" }
```

<br>

```js
component: () => import(/* webpackChunkName: "about", webpackPrefetch:true */ '../views/AboutView.vue')
```

- `webpackChunkName`
  - 다른 컴포넌트들을 같은 청크 네임을 써서 하나로 묶어줄 수 있다.
  - 연관성이 있다면
- `webpackPrefetch:true`
  - 페이지 들어가자마자 바로 캐시에 저장함
  - 사이즈가 너무 큰 경우 미리 서버에서 가져올 수 있다.
    - 장점 : 탭 메뉴중 about을 들어갔들 때 빠르게 로딩이 된다.
    - 단점 : 그만큼 페이지 들어갈 때 오래걸림

> <router-view/> 지우면 안된다!

<br>

## 데이터 바인딩

> 새로운 vue파일을 만들 땐 꼭 router에도 추가시켜준다. (약간 장고에서 urls 포지션)

vue 파일 안에서만 스타일 적용시키고 싶을 때

- `<style scoped></style>`
  - `scoped`를 빼면 전역에 적용된다. 하지만 이렇게 하지않고 assets 폴더에 css 파일을 따로 만들어서 사용한다.

```vue
<template>
  <div>
    <h1></h1>
    <p></p>
  </div>
</template>
```

- vue2버전에서는 꼭 태그들을 최상위 태그(루트 태그)로 묶어줘야 에러가 안난다.
- vue3버전에서는 에러는 아니지만 빨간줄 표시만 해준다.

<br>

```vue
<script>
export default {
  data() {
    return {
      userName: 'John Doe',
      message: '',
      arr: [],
      obj: {}
    }
  }
}
</script>
```

- 이 화면에서 쓰이는 모든 데이터는 `data`함수의 키 밸류 형태로 선언되어야함
  - 그래야 자바스크립트나 html코드에 쓰일 수 있다.

```vue
<template>
  <div>
    <h1>Hello {{ userName }}</h1>
    <p></p>
  </div>
</template>
```

- 문자열은 `{{}}` 중괄호 2개 안에 넣는다.

>  error  Newline required at end of file but not found
>
> - 코드 맨 밑줄에 엔터 하나 넣어준다.

```vue
<template>
  <div v-html="htmlString"></div>
</template>
```

- html 바인딩은 디렉티브를 통해 넣는다.
  - 뷰의 디렉티브는 v 디렉티브이다.
  - InnerHtml로 넣어진다.

> 설정 > User Snippats > vue.json
>
> 코드 자동완성을 설정할 수 있다.

```json
  "Generate Basic Vue Code": {
    "prefix": "vue-start",
    "body": [
      "<template>\n\t<div></div>\n</template>\n\n<script>\nexport default {\n\tcomponents: {},\n\tdata() {\n\t\treturn {\n\t\t\tsampleData:''\n\t\t}\n\t},\n\tsetup() {},\n\tcreated() {},\n\tmounted() {},\n\tunmounted() {},\n\tmethods: {}\n}\n</script>\n\n<style scoped>\n</style>\n"
    ],
    "description": "Generate Basic Vue Code"
  }
```

- vue-start 쓰고 탭하면 위 코드가 자동완성 된다.

<br>

### 양방향 데이터바인딩

```vue
<template>
  <div>
    <input type="text" v-model="userId" />
    <button @click="myFunction">클릭</button>
    <button @click="changeData">변경</button>
    <br />
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      userId: 'sebin'
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    myFunction() {
      console.log(this.userId)
    },
    changeData() {
      this.userId = 'Deep Dive'
    }
  }
}
</script>
```

- `v-model`을 통해 `velue`값을 지정할 수 있다.
- 사용자가 밸류값을 바꾸면 자동으로 데이터가 바뀐다.
- vue에서는 `onclick`대신 `@click`을 사용하며 `myFunction();`에서 `();`를 모두 생략 가능하다
- 함수는 `methods`에 구현한다.
  - 앞에 쓰던 `function`이라는 키워드도 생략 가능하다
  - `this`를 통해 오브젝트 안에 정의된 키값에 접근할 수 있다.

> 태그 하나만 있는 것은 ` /`을 추가해준다. `< ... />`

```vue
    <br />
    <input type="text" v-model="num1" /> +
    <input type="text" v-model="num2" /> =
    <span>{{ num1 + num2 }}</span>
// 1 + 2 = 12
    <br />
    <input type="text" v-model.number="num3" /> +
    <input type="text" v-model.number="num4" /> =
    <span>{{ num3 + num4 }}</span>
// 1 + 2 = 3
...
data() {
    return {
      userId: 'sebin',
      num1: 0,
      num2: 0,
      num3: 0,
      num4: 0
    }
```

- `v-model`에 `.number`를 추가해주면 `int`형태가 된다.

> select도 유저가 밸류값을 바꿀 수 있으므로 양방향 데이터바인딩이다.
>
> v-model을 사용할 수 있다.

```vue
<template>
  <div>
    <select name="" id="" v-model="selectedCity">
      <option value=""></option>
      <option value="02">서울</option>
      <option value="051">부산</option>
      <option value="064">제주</option>
    </select>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      selectedCity: '02'
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
```

- `seletedCity`의 밸류값이 어떤 것이냐에 따라 미리 선택되어지는 것이 달라진다.

> 체크박스는 여러개 선택이 가능하므로 `배열`로 선언한다.

```vue
<template>
  <div>
    <div>
      <input type="checkbox" name="" id="html" value="HTML" v-model="favoriteLang" />
      <label for="html">HTML</label>
    </div>
    <div>
      <input type="checkbox" name="" id="css" value="CSS" v-model="favoriteLang" />
      <label for="css">CSS</label>
    </div>
    <div>
      <input type="checkbox" name="" id="js" value="JS" v-model="favoriteLang" />
      <label for="js">JavaScript</label>
    </div>
    <div>선택한 지역: {{ favoriteLang }}</div>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      favoriteLang: ['JS']
    }
  },
}
</script>
```

- 체크박스는 양방향 데이터바인딩이지만 밸류값을 바꾸는 것이 아닌 `checked`의 `True/False`의 값을 바꾼다.

> 라디오는 단 하나만 선택할 수 있으므로 배열이 아닌 `문자열`로 선언한다.

```vue
data() {
  return {
  favoriteLang: ''
  }
},
```

### views 폴더 vs components 폴더

> router 폴더 안 index.js에서는 path별 component가 명시되어 있다.

- router 속 component에 명시된 vue 파일 => **views 폴더**
- views 폴더 속 vue 파일 내부에서 component로 호출하는 vue 파일 => **components 폴더**

<br>

## 속성 바인딩

>  `readonly`
>
> 사용자가 값을 바꿀 수 없고 조회만 가능하다.

```vue
<input type="text" name="" id="" v-bind:value="userId" readonly />
```

- 사용자가 밸류값을 바꾸면 안될 때

  - `v-model`을 사용하는 것은 위험하다.
  - `v-bind:value`로 직접 바인딩 시키는 것이 좋다.

  ```vue
      <input type="text" name="" id="" :value="userId" readonly />
    </div>
  ```

  - `v-bind`는 생략 가능하다.

### 이미지 속성 바인딩

```vue
<img :src="imgSrc" alt="" style="width:100px; height:auto;">

<script>
export default {
  components: {},
  data() {
    return {
      userId: 'sebin',
      imgSrc: 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Vue.js_Logo_2.svg/1184px-Vue.js_Logo_2.svg.png'
    }
  },
```

- `v-bind`생략 가능하므로 `src`앞에 콜론`:`만 붙이면 된다.

### 밸류값에 따라 버튼 활성화/비활성화

```vue
<input type="search" name="" id="" v-model="txt1" />
<button :disabled="txt1 ===''">조회</button>
```

- txt1의 값이 비어있다면 `:disabled="txt1 ===''`가 True가 되면서 `disabled`가 활성화 된다.

<br>

### 셀렉트 옵션 반복문으로 생성

```vue
<template>
  <div>
    <select name="" id="">
      <option value=""></option>
      <option :value="city.code" :key="city.code" v-for="city in cities">{{city.title}}</option>
    </select>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      cities: [
        { title: '서울', code: '02' },
        { title: '부산', code: '051' },
        { title: '제주', code: '064' }
      ]
    }
  },
```

- `v-for="요소 in 배열"`
  - 반복문
  - `v-for`을 쓸 땐 **반드시 `key`를 바인딩 해야한다.**
    - `:key`를 통해 바인딩시킨다.
    - `key`는 유일한 값이 들어와야한다. 

```vue
 <div>
      <table>
        <thead>
          <tr>
            <th>제품번호</th>
            <th>제품명</th>
            <th>가격</th>
            <th>주문수량</th>
            <th>합계</th>
          </tr>
        </thead>
        <tbody>
          <tr :key="drink.drinkId" v-for="drink in drinkList">
            <td>{{ drink.drinkId }}</td>
            <td>{{ drink.drinkName }}</td>
            <td>{{ drink.price }}</td>
            <td><input type="number" name="" id="" v-model="drink.qty" /></td>
            <td>{{ drink.price * drink.qty }}</td>
          </tr>
        </tbody>
      </table>
    </div>

 drinkList: [
        {
          drinkId: '1',
          drinkName: '코카콜라',
          price: 700,
          qty: 1
        },
        {
          drinkId: '2',
          drinkName: '오렌지주스',
          price: 1200,
          qty: 1
        },
        {
          drinkId: '3',
          drinkName: '커피',
          price: 500,
          qty: 2
        }
      ]
```

> 만약 key로 쓸만한 Id값 등이 없을 경우
>
> - 인덱스를 사용한다.

```vue
<tr :key="i" v-for="(drink, i) in drinkList"></tr>
```

- i에 for문 index 값이 들어가게된다.

<br>

### 클래스 바인딩

```vue
<template>
  <div>
    <div :class="{'text-red': hasError, active: isActive}">클래스 바인딩</div>
    <div :class="class2">클래스 바인딩2</div>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      isActive: false,
      hasError: false,
      class2: ['active', 'hasError']
    }
  },
</script> 

<style scoped>
.active {
  background-color: greenyellow;
  font-weight: bold;
}
.text-red {
  color: red;
}
</style>
```

- class 바인딩은 오브젝트 형태로 여러개 한번에 할 수 있다.
- 키값에 class 명이, 밸류값에 true/false가 들어가서 UI를 동적으로 조작할 수 있다.
- class 명에 `-`가 들어갔으면 반드시 `''`로 감싸준다.
  - 없으면 안감싸도 된다.
- class2처럼 배열형태로 한번에 적용 가능하다.
  - 하지만 실무에서 많이 쓰이진 않는다.

<br>

### 스타일 바인딩

```vue
<template>
  <div>
    <div :style="style1">스타일 바인딩: 글씨는 green, 폰트크기: 30px</div>
    <button @click="style1.color='blue'">색상 바꾸기</button>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      style1: {
        color: 'green',
        fontSize: '30px'
      }
    }
  },
}
</script>
```

- 스타일도 오브젝트 형태로 키와 밸류로 이루어져있다.
- CSS의 `-`는 빼고 뒤에 글자를 대문자로 바꿔준다.

<br>

## Vue 이벤트

### 클릭 이벤트

```vue
<template>
  <div>
    <button @click="increaseCounter">Add 1</button>
    <p>{{ counter }}</p>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      counter: 0
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    increaseCounter() {
      this.counter += 1
    }
  }
}
</script>
```

### 체인지 이벤트 및 멀티 셀렉트

```vue
template>
  <div>
    <select name="" id="" @change="changeCity" v-model="selectedCity">
      <option value="">===도시선택===</option>
      <option
        :value="city.cityCode"
        :key="city.cityCode"
        v-for="city in cityList"
      >
        {{ city.title }}
      </option>
    </select>
    <select name="" id="">
      <option
        :value="dong.dongCode"
        :key="dong.dongCode"
        v-for="dong in selectedDongList"
      >
        {{ dong.dongTitle }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      selectedCity: '',
      cityList: [
        { cityCode: '02', title: '서울' },
        { cityCode: '051', title: '부산' },
        { cityCode: '064', title: '제주' }
      ],
      dongList: [
        { cityCode: '02', dongCode: '1', dongTitle: '서울 1동' },
        { cityCode: '02', dongCode: '2', dongTitle: '서울 2동' },
        { cityCode: '02', dongCode: '3', dongTitle: '서울 3동' },
        { cityCode: '02', dongCode: '4', dongTitle: '서울 4동' },
        { cityCode: '051', dongCode: '1', dongTitle: '부산 1동' },
        { cityCode: '051', dongCode: '2', dongTitle: '부산 2동' },
        { cityCode: '051', dongCode: '3', dongTitle: '부산 3동' },
        { cityCode: '064', dongCode: '1', dongTitle: '제주 1동' },
        { cityCode: '064', dongCode: '2', dongTitle: '제주 2동' }
      ],
      selectedDongList: []
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    changeCity() {
      this.selectedDongList = this.dongList.filter(
        (dong) => dong.cityCode === this.selectedCity
      )
    }
  }
}
</script>
```

- `v-model`을 통해 `selectedCity`의 밸류가 바뀜
- 그래서 `@chage`의 `changeCity`함수가 호출됨
  - `this.selectedDongList`는 `this.dongList.filter`가 된건데
  - 이 `filter`안에서 `dong`을 인자로 받고 `dong.cityCode === this.selectedCity`의 값을 리턴시킨다.

```vue
<select name="" id="">
      <option
        :value="dong.dongCode"
        :key="dong.dongCode"
        v-for="dong in dongList.filter(
        (dong) => dong.cityCode === selectedCity
      )"
      >
        {{ dong.dongTitle }}
      </option>
    </select>
```

- `v-for`안 배열부분에 함수를 직접 넣을 수 있다.
  - `this`는 빼줘야한다.
  - 가독성이 조금 떨어진다.
- `@`대신 `v-on`을 사용 할 수 있다.
  - `v-on:change`

> 이벤트도 전달 하고 싶을 때

```vue
<select name="" id="" @change="changeCity($event)" v-model="selectedCity">
<script> 
methods: {
    changeCity(event) {
      console.log(event.target.tagName)
      this.selectedDongList = this.dongList.filter(
        (dong) => dong.cityCode === this.selectedCity
      )
    }
  }
</script>
```

- `@change`에 `($event)`를 추가한다.
- `changeCity`함수에 인자로 `event` 추가
- `console.log(event.target.tagName)`를 추가하면 콘솔창에 어떤 이벤트가 발생했는지 알 수 있다. (SELECT)

<br>

### 버튼이 아닌 엔터키를 눌러도 버튼이 실행 되게끔 하기

> Keyup event 이용

```vue
<template>
  <div>
    <input
      type="search"
      name=""
      id=""
      @keyup="checkEnter($event)"
      v-model="searchText"
    />
    <button @click="doSearch">조회</button>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      searchText: ''
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    doSearch() {
      console.log(this.searchText)
    },
    checkEnter(event) {
      if (event.keyCode === 13) {
        this.doSearch()
      }
    }
  }
}
</script>
```

> enter키의 코드는 13이다

- `v-model`을 이용해서 양방향 데이터 바인딩 후 console.log로 확인
- `@keyup`이벤트로 만약 키코드가 13이라면 `doSearch`함수 실행

> Vue에서는 훨씬 간편한 방법이 있다.

```vue
<input
      type="search"
      name=""
      id=""
      @keyup.enter="doSearch"
      v-model="searchText"
    />
```

- `@keyup.해당 키` 하면 바로 함수 호출이 가능하다
  - `.enter`
  - `.tab`
  - `.delete`
  - `.esc`
  - `.space`
  - `.up`
  - `.down`
  - `.left`
  - `.right`
  - `.ctrl`

> 이벤트 버블링을 막기 위한 `stopPropagation` 함수
>
> 이벤트의 기본 기능을 막기 위한 `preventDefault` 함수

```vue
<button type="submit" @click.prevent="doSearch"></button>
```

- `.prevent` : `event.preventDefault();`
- `.stop` : `event.stopPropagation();`

<br>

## Vue Lifecycle

![](https://vuejs.org/assets/lifecycle.16e4c08e.png)

- `watch` 함수 : 데이터 관찰용

  ```vue
  <script>
  export default {
    watch: {
      input1() {
        console.log(this.input1)
      }
    }
  }
  </script>
  ```

- `v-if`

  ```vue
  <table v-if="tableShow">
    <tr>
    </tr>
  </table>
  ```

  - 해당 함수가 true라면 안에 요소들을 렌더링
  - false라면 렌더링을 안함
  - `v-show` : false라도 렌더링은 한다.
    - 만약 요소가 자주 보였다 안보였다 한다면 `v-show`를 쓸 것

