# python 库

## **jquery**

### 安装 jquery 库

```shell
    pip install pyquery
```

### 检查 jquery 库

    In [1]: import pyquery
    In [2]: pyquery.text
    Out[2]: <module 'pyquery.text' from '/root/pp1/.venv/lib/python3.6/site-packages/pyquery/   text.py'>

### css 选择器

- .class (选择 class="hello" 的所有元素。)
- #id (选择 id="kayla" 的所有元素。)
- element (p 选择所有 <p> 元素。)
- div p (选择 <div> 元素内部的所有 <p> 元素。)
- [target]
- [target=_blank]
- p:first-child
- p:last-child
  注:
  **[]** ,将没有定义的属性名用[]表示
  **>** 亲儿子
  空格 子孙后代

### jquery 选择器

- 祖先
  - parent() ,方法返回被选元素的直接父元素。
  - parents() ,方法返回被选元素的所有祖先元素，它一路向上直到文档的根元素 (<html>)
  - parentsUntil() ,返回介于两个给定元素之间的所有祖先元素。
- 后代
  - children() ,返回被选元素的`所有直接子元素`
  - find() ,返回被选元素的`后代元素`，一路向下直到最后一个后代。
    注:
    `*`,所有
- 同胞
  - siblings() ,返回被选元素的所有同胞元素。
  - next() ,返回被选元素的下一个同胞元素
  - nextAll()
  - nextUntil()
  - prev()
  - prevAll()
  - prevUntil()
- 过滤
  - first() 方法返回被选元素的首个元素
  - last() 方法返回被选元素的最后一个元素。
  - eq() 方法返回被选元素中带有指定索引号的元素。
  - filter() 方法允许您规定一个标准。不匹配这个标准的元素会被从集合中删除，`匹配的`元素会被`返回`。
  - not() 方法`返回` `不匹配`标准的所有元素。

### pyQuery

(https://segmentfault.com/a/1190000005182997)
