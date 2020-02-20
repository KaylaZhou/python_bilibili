# 第十二章 函数式编程

## `reduce()`

- reduce() 函数会对参数序列中元素进行`连续计算`

### 1.使用方法

- 需要从 functools 模块中导入 reduce
- reduce 函数,`必须`要有`两个参数`
- 初始值,第一次计算时参与

  ```py

  from functools import reduce

  reduce(function, sequence, initial=None)

  ```

  ```py
  例子:
    list_x = [1, 2, 3, 4, 5, 6, 7, 8]

    r = reduce(lambda x, y: x+y, list_x)
    r1 = reduce(lambda x, y: x+y, list_x, 10)  # 初始值10,第一次计算时参
    print(r)
    print(r1

  ```

  ```py
  打印结果:36
          46
  ```

### 误区:

- reduce()函数做连续计算,不仅仅是连续相加.也可以相乘

### 扩展

    谷歌提出过一个大数据计算模型 `map/reduce` 是一个编程模型,map 在大数据中叫映射,reduce 在大数据中叫归约,主要做并行计算.  借鉴思想,就是函数式编程
