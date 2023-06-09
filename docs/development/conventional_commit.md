# 约定式提交一般格式

:::  tip Intorduce
约定式提交规范 Conventional Commits 是一种用于给提交信息增加人机可读含义的规范，是基于提交信息的轻量级约定，提供了一组用于创建清晰的提交历史的简单规则。
:::


```zh-cn
<类型>([可选的作用于]): <描述>

[可选的正文]

[可选的脚注]
```

```en
type(scope?): subject
body?
footer?
```

<hr>

## 类型/type

|type|含义|
| :------: | :-----------: |
|feat|新增功能|
|fix|修复bug|
|docs|更改文档|
|style|不影响代码含义的变化(空白，格式化，缺少分号等)|
|refactor|重构，不修复bug且不添加功能|
|ci|持续集成相关|
|test|测试相关|
|chore|重复性的日常任务|
|revert|恢复变更/回滚到上一个版本|
|perf|性能优化代码|
|build|构建方面相关|

## 作用域/scope
紧跟<类型>用小括号包住，值可以按照模块、包或者某个文件进行标注

## 描述/subject
作为本次commit的简介，一般不超过50个字符

## 正文/body
详细描述，可以分成多行
- 语法使用第一人称现在时
- 应当说明变动的动机以及与以前行为的对比

## 脚注/footer
仅描述两种情况
- 不兼容的变动： 如果当前代码与上一个版本不兼容，则 Footer 部分以BREAKING CHANGE开头，后面是对变动的描述、以及变动理由和迁移方法。
- 关闭 Issue: Closes #234

## 破坏式更改
约定式提交对破坏性变更有特殊的处理。如果 commit 的改动包含了破坏性的变更，有两种方式来表示：
- 第一种方式是在类型和范围之后添加感叹号，如 feat(api)!
- 第二种方式是在脚注中添加 BREAKING CHANGE, 如BREAKING CHANGE: some changes

