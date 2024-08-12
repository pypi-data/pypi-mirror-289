# math-expand Package

## 这个包是对Python原生的Math包进行的拓展，目前提供的方法如下：

- digits
  - take_digits(number, return_type) → list/dict
    - 方法用途
      - 取一个数的每一位数
    - 方法解析
      - 参数解析
        - number
          - 要取每一位数的数
        - return_type
          - 指定返回值的类型
          - 默认为l，有l（返回列表）,和d（返回字典）两种形式，其余值会导致输出一条错误信息。
      - 返回值
        - 由return_type参数决定
        - 返回值
          - list
            - 这个列表里包含了这个数从高到低每个数位的数字
          - dict
            - 这个字典的键是一个个计数单位，每个键对应的值便是当前键表示的计数单位上的值

### 使用 `pip install mathexpand` 命令安装它！
