@ 创建日期:2020 年 1 月 19 日,20 点 46 分
@ 更新日期:2020 年 1 月 19 日,20 点 46 分

# 集合

## 什么是集合`set`?

- **用`{}`包起来的元素,不同元素之间用逗号分隔,称为集合**

## 集合的特性:

- 集合是`无序`的
- 集合中的元素`不重复`
- 集合不支持切片,下标索引

  ```py
  例子:

    print({1,2,3,4,5,6})
    print({'hello world'})

  输出结果: {1, 2, 3, 4, 5, 6}
            {'hello world'}

  ```

  ```py
  错误的例子:

    print({1, 2, 3, 4, 5, 6}[3:])
    print({1, 2, 3, 4, 5, 6}[3])
     # 集合是无序的,因此无法做切片

  输出结果:
   TypeError: 'set' object is not subscriptable

  ```

## 集合支持的操作:

- 支持的操作:`len` ,`in` ,`not in`
- 特有的操作:`-`差集,`&`交集,`|`并集

```py
例子:
  print(len({1, 2, 4, 6, 8, 9, }))
  print(len({'kayla', 'kayla', 'love', 'you'}))
  print(7 not in {1, 4, 7, 9, 0})
  print(7 in {1, 4, 7, 9, 0})
  print({1, 2, 3, 4} - {2, 3})
  print({1, 2, 3, 4} & {2, 3})
  print({1, 2, 3, 4} | {2, 3})

输出结果:  6
          3
          False
          True
          {1, 4}
          {2, 3}
          {1, 2, 3, 4}


```

## 如何定义空的集合?

```py
 #通过set

  print(type(set()))


 输出结果: <class 'set'>
```
