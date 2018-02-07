## 适用范围

### 适合执行，给出门店id,反查出门店所在db的详细信息并且在对应的数据库中执行相应的脚本

### 因为这个是在shop的每个库中都需要执行，所以在cmdbshop中在每个stack每个db中一个shopid ，写在excel 中
select * from cmdbshop where stackId in ("a03a","a02a","a01a") GROUP BY stackId,dbname ;

### 然后去执行