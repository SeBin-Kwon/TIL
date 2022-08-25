# 🎆 QuerySet API

### gt / gte

> greater than / greater than equal

```python
Entry.objects.filter(id__gt=4)
Entry.objects.filter(id__gte=4)
```

```sql
SELECT ... WHERE id > 4;
SELECT ... WHERE id >= 4;
```

### lt / lte

> less than / less than equal

```python
Entry.objects.filter(id__lt=4) Entry.objects.filter(id__lte=4)
```

```sql
SELECT ... WHERE id < 4; 
SELECT ... WHERE id <= 4;
```

### in

```python
Entry.objects.filter(id__in=[1, 3, 4]) Entry.objects.filter(headline__in='abc')
```

```sql
SELECT ... WHERE id IN (1, 3, 4);
SELECT ... WHERE headline IN ('a', 'b', 'c');
```

### startswith

> 와일드카드

```python
Entry.objects.filter(headline__startswith='Lennon')
```

```sql
SELECT ... WHERE headline LIKE 'Lennon%';
```

### istartswith

> 대소문자 구분 안함

```python
Entry.objects.filter(headline__istartswith='Lennon')
```

```sql
SELECT ... WHERE headline ILIKE 'Lennon%';
```

### endswith

```python
Entry.objects.filter(headline__endswith='Lennon') Entry.objects.filter(headline__iendswith='Lennon')
```

```sql
SELECT ... WHERE headline LIKE '%Lennon';
SELECT ... WHERE headline ILIKE '%Lennon'
```

### contains

```python
Entry.objects.get(headline__contains='Lennon') Entry.objects.get(headline__icontains='Lennon’)
```

```sql
SELECT ... WHERE headline LIKE '%Lennon%'; 
SELECT ... WHERE headline ILIKE '%Lennon%';
```

### range

```python
import datetime
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2005, 3, 31)
Entry.objects.filter(pub_date__range=(start_date, end_date))
```

```sql
SELECT ... WHERE pub_date
BETWEEN '2005-01-01' and '2005-03-31';
```

### 복합 활용

> 서브 쿼리

```python
inner_qs = Blog.objects.filter(name__contains='Cheddar')
entries = Entry.objects.filter(blog__in=inner_qs)
```

```sql
SELECT ...
WHERE blog.id IN (SELECT id FROM ... WHERE NAME LIKE '%Cheddar%’);
```

### 활용

>인덱싱 = 리밋
>
>슬라이싱 = 리밋 오프셋

```python
Entry.objects.all()[0]
Entry.objects.order_by('id')
Entry.objects.order_by('-id')
```

```sql
SELECT ...
LIMIT 1;
SELECT ...
ORDER BY id;
SELECT ...
ORDER BY id DESC;
```

<br>

## ORM 확장 (1:N)

### 모델링 (ORM)

```python
class Genre(models.Model):
name = models.CharField(max_length=30)

class Artist(models.Model):
name = models.CharField(max_length=30) debut = models.DateField()

class Album(models.Model):
name = models.CharField(max_length=30) genre = models.ForeignKey('Genre',
on_delete=models.CASCADE)
artist = models.ForeignKey('Artist',
on_delete=models.CASCADE)
```

### Foreign Key (외래키)

- 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)
  - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
- 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함

<br>

### models.ForeignKey 필드

- 2개의 필수 위치 인자

  - `Model class` : 참조하는 모델

  - `on_delete` : 외래 키가 참조하는 객체가 삭제되었을 때 처리 방식

    - `CASCADE` : 부모 객체(참조 된 객체)가 삭제됐을 때 이를 참조하는 객체도 삭제

    - `PROTECT` : 삭제되지 않음

    - `SET_NULL` : NULL 설정

    - `SET_DEFAULT` : 기본 값 설정

<br>

### Create

```python
artist = Artist.objects.get(id=1)
genre =  Genre.objects.get(id=1)
album = Album()
album.name = '앨범1'
album.artist = artist # 1. 객체의 저장
album.genre = genre
album.save()
```

<br>

### 참조와 역참조

```python
class Genre(models.Model):
name = models.CharField(max_length=30)
class Artist(models.Model):
name = models.CharField(max_length=30) debut = models.DateField()
class Album(models.Model):
name = models.CharField(max_length=30) genre = models.ForeignKey('Genre’,
on_delete=models.CASCADE)
artist = models.ForeignKey('Artist’,
on_delete=models.CASCADE)
```

```python
# 1. 참조
album = Album.objects.get(id=1) album.artist
# <Artist: Artist object (1)> album.genre
# <Genre: Genre object (1)>
# 2. 역참조
genre = Genre.objects.get(id=1) genre.album_set.all()
# <QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>
```

<br>

#### 예시

```python
# 1. Artist 생성
import datetime 
artist = Artist() 
artist.name = '아이브'
# 2021년 12월 1일
artist.debut = datetime.date(2021, 12, 1)
artist.save()

artist = Artist() 
artist.name = '아이유'
artist.debut = '2019-12-26'
artist.save()

# 1:N 관계에서의 Create

# 객체
# Class 정의를 genre로 했기 때문
album = Album()
album.name = '꽃'
# album.genre = 1
# ValueError: Cannot assign "1": "Album.genre" must be a "Genre" instance.       
genre = Genre.objects.get(id=1)
album.genre = genre
artist = Artist.objects.get(id=1)    
album.artist = artist
album.save()

# 값
# 테이블에 실제 필드는 _id가 붙어있기 때문
album = Album()
album.genre_id = 1
album.artist_id = 1
album.name = '미아'
album.save()

# N => 1 (참조)
# 앨범의 id가 1인 것의
album = Album.objects.get(id=1) # 앨범 객체
# 장르의 이름은..?
album.genre # 장르 객체
# <Genre: Genre object (1)>
album.genre.name
# '발라드'


# 1 => N (역참조)
# 클래스이름_set
# id가 1인 장르의 모든 앨범은?
g1 = Genre.objects.get(id=1)
g1.album_set.all() 
# <QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>
```

