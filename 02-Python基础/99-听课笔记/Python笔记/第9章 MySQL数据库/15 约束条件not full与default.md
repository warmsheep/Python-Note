### 约束条件not full与default

create table t15(
  id int unsigned zerofill
  );

desc t15;

```
  +-------+---------------------------+------+-----+---------+-------+
  | Field | Type                      | Null | Key | Default | Extra |
  +-------+---------------------------+------+-----+---------+-------+
  | id    | int(10) unsigned zerofill | YES  |     | NULL    |       |
  +-------+---------------------------+------+-----+---------+-------+
```

null:是否可以传空值

create table t16(
  id int,
  name char(6),
  sex enum("male","female") not null default "male"
  );

desc t16;
