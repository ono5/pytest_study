# flake8

```
pytest test_one.py && flake8
```

# pytestの検索

test_xxxx.py xxxx_test.py のファイルを検索する。

# 命名規則

* テストファイルの名前は、test_<something>.py または、<something>_test.py という形式でなければならない
* テストメソッドやテスト関数の名前は test_<something> とう形式でなければならない
* テストクラスの名前は、Test<Something> という形式でなければならない

# テストを一つだけ実行

```bash
pytest -v tasks/test_four.py::test_asdict
```

# pytest オプション

### --help

ヘルプを表示

```bash
python --help
```

### --collect-only

指定したオプションと構成に基づいて時刻されるテストを表示する。

テスト対象一覧。

```bash
$ pytest --collect-only
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      
<Module test_one.py>
  <Function test_passing>
<Module test_two.py>
  <Function test_failing>
<Module tasks/test_four.py>
  <Function test_asdict>
  <Function test_replace>
<Module tasks/test_three.py>
  <Function test_defaults>
  <Function test_member_access>
```

## -k EXPRESSION

- k オプションは、実行するテスト関数を、式を使って検索できるようにしたフィルタ。

テストに一意な名前がついている場合は、テストを個別に実行するためのショートカットとしても利用可能。

```bash
# テスト対象を確かめる
$ pytest -k "asdict or defaults" --collect-only
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items / 4 deselected                                                                                                                                                                                                       
<Module tasks/test_four.py>
  <Function test_asdict>
<Module tasks/test_three.py>
  <Function test_defaults>

# テストする
$ pytest -k "asdict or defaults"
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items / 4 deselected                                                                                                                                                                                                       

tasks/test_four.py .                                                                                                                                                                                                             [ 50%]
tasks/test_three.py .  
``` 

# -m MARKERPR

マーカーは、テスト関数の一部に名前をつけ、それらの関数をまとめて実行できるようにする。

```bash
# run_these_please というマーカーを付与して、実行

 $ pytest -v -m run_these_please
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items / 4 deselected                                                                                                                                                                                                       

tasks/test_four.py::test_asdict PASSED                                                                                                                                                                                           [ 50%]
tasks/test_three.py::test_member_access PASSED                                                                                                                                                                                   [100%]

# その他のパターン
$ pytest -v -m mark1 and mark2
$ pytest -v -m mark1 and not mark2
$ pytest -v -m mark1 or mark2
```

## -x, --exitfirst

テスト失敗時に、後続のテストが走らないようにする。

```bash
 $ pytest -x
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      

test_one.py .                                                                                                                                                                                                                    [ 16%]
test_two.py F

=============================================================================================================== FAILURES ===============================================================================================================
_____________________________________________________________________________________________________________ test_failing _____________________________________________________________________________________________________________

    def test_failing():
>       assert (1, 2, 3) == (3, 2, 1)
E       assert (1, 2, 3) == (3, 2, 1)
E         At index 0 diff: 1 != 3
E         Use -v to get the full diff

test_two.py:2: AssertionError
```

## --tb=style

トレースバックのオプション。

```bash
 $ pytest --tb=no
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      

test_one.py .                                                                                                                                                                                                                    [ 16%]
test_two.py F                                                                                                                                                                                                                    [ 33%]
tasks/test_four.py ..                                                                                                                                                                                                            [ 66%]
tasks/test_three.py ..   


 $ pytest --tb=short
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      

test_one.py .                                                                                                                                                                                                                    [ 16%]
test_two.py F                                                                                                                                                                                                                    [ 33%]
tasks/test_four.py ..                                                                                                                                                                                                            [ 66%]
tasks/test_three.py ..                                                                                                                                                                                                           [100%]

=============================================================================================================== FAILURES ===============================================================================================================
_____________________________________________________________________________________________________________ test_failing _____________________________________________________________________________________________________________
test_two.py:2: in test_failing
    assert (1, 2, 3) == (3, 2, 1)
E   assert (1, 2, 3) == (3, 2, 1)
E     At index 0 diff: 1 != 3
E     Use -v to get the full diff

$ pytest --tb=line
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      

test_one.py .                                                                                                                                                                                                                    [ 16%]
test_two.py F                                                                                                                                                                                                                    [ 33%]
tasks/test_four.py ..                                                                                                                                                                                                            [ 66%]
tasks/test_three.py ..                                                                                                                                                                                                           [100%]

=============================================================================================================== FAILURES ===============================================================================================================
/Users/hono/Desktop/pytest_code/ch1/test_two.py:2: assert (1, 2, 3) == (3, 2, 1)
```

## --maxfail=num

テストが失敗する数に上限を持たせる。

```bash
$ pytest --maxfail=2 --tb=no
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      

test_one.py .                                                                                                                                                                                                                    [ 16%]
test_two.py F                                                                                                                                                                                                                    [ 33%]
tasks/test_four.py ..                                                                                                                                                                                                            [ 66%]
tasks/test_three.py ..     

$ pytest --maxfail=1 --tb=no
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      

test_one.py .                                                                                                                                                                                                                    [ 16%]
test_two.py F
```

## -s, --capture=method

テスト実行中に print 文の出力を標準出力に書き出すことができる。

```bash
# Start / End 
pytest -s tasks/test_four.py 
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collecting ... -------------Start Test-------------------
-------------End Test-------------------
collected 2 items                                                                                                                                                                                                                      

tasks/test_four.py ..


 $ pytest  tasks/test_four.py 
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 2 items                                                                                                                                                                                                                      

tasks/test_four.py ..                                                                                                                                                                                                            [100%]
```

## -l, --showlocals

テストが失敗した場合に、そのテストのローカル変数を表示する。

````bash
pytest -l tasks/test_four.py 
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 2 items                                                                                                                                                                                                                      

tasks/test_four.py F.                                                                                                                                                                                                            [100%]

=============================================================================================================== FAILURES ===============================================================================================================
_____________________________________________________________________________________________________________ test_asdict ______________________________________________________________________________________________________________

    @pytest.mark.run_these_please
    def test_asdict():
        """_asdict() should return a dictionary."""
        t_task = Task('do something', 'okken', True, 21)
        t_dict = t_task._asdict()
        expected = {'summary': 'do something',
                    'owner': 'okken',
                    'done': True,
                    'id': 21}
>       assert t_dict != expected
E       AssertionError: assert OrderedDict([('summary', 'do something'), ('owner', 'okken'), ('done', True), ('id', 21)]) != {'done': True, 'id': 21, 'owner': 'okken', 'summary': 'do something'}

expected   = {'done': True, 'id': 21, 'owner': 'okken', 'summary': 'do something'}
t_dict     = OrderedDict([('summary', 'do something'), ('owner', 'okken'), ('done', True), ('id', 21)])
t_task     = Task(summary='do something', owner='okken', done=True, id=21)

tasks/test_four.py:18: AssertionError
````

## --lf, --last-failed

最後に失敗しているテストだけ実行する。

```bash
$ pytest --lf
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items / 5 deselected                                                                                                                                                                                                       
run-last-failure: rerun previous 1 failure

test_two.py F                                                                                                                                                                                                                    [100%]

=============================================================================================================== FAILURES ===============================================================================================================
_____________________________________________________________________________________________________________ test_failing _____________________________________________________________________________________________________________

    def test_failing():
>       assert (1, 2, 3) == (3, 2, 1)
E       assert (1, 2, 3) == (3, 2, 1)
E         At index 0 diff: 1 != 3
E         Use -v to get the full diff

test_two.py:2: AssertionError

$ pytest --lf --tb=no
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items / 5 deselected                                                                                                                                                                                                       
run-last-failure: rerun previous 1 failure

test_two.py F   
```

## --ff, --failed-first

最後に失敗したテストを実行ご、残りの成功しているテストを実行する。

```bash
$ pytest --ff --tb=no
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      
run-last-failure: rerun previous 1 failure first

test_two.py F                                                                                                                                                                                                                    [ 16%]
test_one.py .                                                                                                                                                                                                                    [ 33%]
tasks/test_four.py ..                                                                                                                                                                                                            [ 66%]
tasks/test_three.py ..                                                                                                                                                                                                           [100%]
```

## -v, --verbose

詳細情報を出力する。

```bash
 $ pytest -v --ff --tb=no
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      
run-last-failure: rerun previous 1 failure first

test_two.py::test_failing FAILED                                                                                                                                                                                                 [ 16%]
test_one.py::test_passing PASSED                                                                                                                                                                                                 [ 33%]
tasks/test_four.py::test_asdict PASSED                                                                                                                                                                                           [ 50%]
tasks/test_four.py::test_replace PASSED                                                                                                                                                                                          [ 66%]
tasks/test_three.py::test_defaults PASSED                                                                                                                                                                                        [ 83%]
tasks/test_three.py::test_member_access PASSED  
```

## -q, --quiet

出力される情報が少なくなる。

```bash
 pytest -q
.F....                                                                                                                                                                                                                           [100%]
=============================================================================================================== FAILURES ===============================================================================================================
_____________________________________________________________________________________________________________ test_failing _____________________________________________________________________________________________________________

    def test_failing():
>       assert (1, 2, 3) == (3, 2, 1)
E       assert (1, 2, 3) == (3, 2, 1)
E         At index 0 diff: 1 != 3
E         Full diff:
E         - (1, 2, 3)
E         ?  ^     ^
E         + (3, 2, 1)
E         ?  ^     ^

test_two.py:2: AssertionError
1 failed, 5 passed in 0.07 seconds

$ pytest -q --tb=line
.F....                                                                                                                                                                                                                           [100%]
=============================================================================================================== FAILURES ===============================================================================================================
/Users/hono/Desktop/pytest_code/ch1/test_two.py:2: assert (1, 2, 3) == (3, 2, 1)
1 failed, 5 passed in 0.06 seconds
```

## --durations=N

テストが実行された後に、もっとも時間がかかった N 個のテスト/セットアップ/ティアダウンを表示する。

```bash
$ pytest --durations=3 tasks
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 4 items                                                                                                                                                                                                                      

tasks/test_four.py ..                                                                                                                                                                                                            [ 50%]
tasks/test_three.py ..                                                                                                                                                                                                           [100%]

======================================================================================================= slowest 3 test durations =======================================================================================================
0.11s call     tasks/test_four.py::test_asdict

(0.00 durations hidden.  Use -vv to show these durations.)
```

## --skip --skipif

テストをスキップできる。


```bash
$ pytest -v XXXX

# スキップした理由を知りたい場合
$ pytest -rs XXXX
```

## -r

指定されたテストの要約情報を pytest の出力に追加する。

```bash
  -r chars              show extra test summary info as specified by chars
                        (f)ailed, (E)error, (s)skipped, (x)failed, (X)passed,
                        (p)passed, (P)passed with output, (a)all except pP.
                        Warnings are displayed at all times except when
                        --disable-warnings is set
```

# テスト分類

* ユニットテスト
  - 関数やクラスなど、コードのごく一部をチェックするテスト。単体テストとも呼ばれる。

* 結合テスト
  - 複数のクラスやサブシステムなど、ひと回り大きなコードをチェックするテスト。
    ユニットテストより大きく、システムテストより小さい。

* システムテスト
  - テストしているシステム全体をチェックするテスト。エンドツーエンドテストとも呼ばれる。
    システムテストは、可能な限り、エンドユーザー環境に近い環境で行われる。
    
* 機能テスト
  - システムのただ一つの機能をチェックするテスト
 
* 皮下テスト
  - 最終的なエンドユーザーインターフェースに対して実行されるのではなく、表面のすぐ下にある
    インターフェイスに対して実行されるテスト。

# pytest ファイル

* pytest.ini
  - プロジェクト全体の構成情報。プロジェクトに最大一つ用意する(必須ではない)。

* conftest.py
  - pytest によって、ローカルプラグインであると見なされるファイルで、フック関数やフィクスチャを含んでいる場合もある。
  * フック関数
    - pytest の実行プロセスの一部にコードを挿入することで、pytest の動作方法を変更する手段。
  * フィクスチャ
    - テスト関数の前後に実行されるセットアップ関数とティアダウン関数であり、テストに使用されるリソースやデータを表すために使用できる。
    
# pytest assert

[Demo of Python failure reports with pytest](https://docs.pytest.org/en/latest/example/reportingdemo.html)

# テスト関数にマークをつける

テスト関数に @pytest.mark.XXXX のデコレータを付与する。

# テストをパラメーター化する

## デコレータ

@pytest.mark.parametrize('<引数>', <引数値>)

```bash
@pytest.mark.parametrize('task',
                         [Task('sleep', done=True),
                          Task('wake', 'brian'),
                          Task('breathe', 'BRIAN', True),
                          Task('exercise', 'BrIaN', False)])
def test_add_2(task):
    """Demonstrate parametrize with one parameter."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('summary, owner, done',
                         [('sleep', None, False),
                          ('wake', 'brian', False),
                          ('breathe', 'BRIAN', True),
                          ('eat eggs', 'BrIaN', False),
                          ])
def test_add_3(summary, owner, done):
    """Demonstrate parametrize with multiple parameters."""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))


@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    """Slightly different take."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done)
            for t in tasks_to_try]


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    """Demonstrate ids."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', [
    pytest.param(Task('create'), id='just summary'),
    pytest.param(Task('inspire', 'Michelle'), id='summary/owner'),
    pytest.param(Task('encourage', 'Michelle', True), id='summary/owner/done')])
def test_add_6(task):
    """Demonstrate pytest.param and id."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():
    """Demonstrate parametrize and test classes."""

    def test_equivalent(self, task):
        """Similar test, just within a class."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        """We can use the same data for multiple tests."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id

```

## テストID

pytest が文字列に変換しやすい型を使用すると、テストIDとしてパラメータの値が使用されるため、
出力が読みやすくなる。

```bash
(env) $ pytest -v test_add_variety.py::test_add_3
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch2/tasks_proj/tests, inifile: pytest.ini
collected 4 items                                                                                                                                                                                                                      

test_add_variety.py::test_add_3[sleep-None-False] PASSED                                                                                                                                                                         [ 25%]
test_add_variety.py::test_add_3[wake-brian-False] PASSED                                                                                                                                                                         [ 50%]
test_add_variety.py::test_add_3[breathe-BRIAN-True] PASSED                                                                                                                                                                       [ 75%]
test_add_variety.py::test_add_3[eat eggs-BrIaN-False] PASSED

# テストID sleep-None-False
$ pytest -v test_add_variety.py::test_add_3[sleep-None-False]
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch2/tasks_proj/tests, inifile: pytest.ini
collected 1 item                                                                                                                                                                                                                       

test_add_variety.py::test_add_3[sleep-None-False] PASSED

# テストID にスペースが含まれている場合は、必ず引用符("")で囲んでください。
$ pytest -v "test_add_variety.py::test_add_3[eat sleep-None-False]"
```

## ids パラメータ
parametrize オプションの ids を使って、テストのデータセットをそれぞれのIDといsて使用する。

```bash
# 引用符がいる
$ pytest -v "test_add_variety.py::test_add_5[Task(exercise,BrIaN,False)]"
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch2/tasks_proj/tests, inifile: pytest.ini
collected 1 item                                                                                                                                                                                                                       

test_add_variety.py::test_add_5[Task(exercise,BrIaN,False)] PASSED                                                                                                                                                               [100%]
```

# パラメータのID化
パラメータを id パラメータに渡すとパラメータを識別できる。

```bash
@pytest.mark.parametrize('task', [
    pytest.param(Task('create'), id='just summary'),
    pytest.param(Task('inspire', 'Michelle'), id='summary/owner'),
    pytest.param(Task('encourage', 'Michelle', True), id='summary/owner/done')])
def test_add_6(task):
    """Demonstrate pytest.param and id."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
    
 $ pytest -v test_add_variety.py::test_add_6
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch2/tasks_proj/tests, inifile: pytest.ini
collected 3 items                                                                                                                                                                                                                      

test_add_variety.py::test_add_6[just summary] PASSED                                                                                                                                                                             [ 33%]
test_add_variety.py::test_add_6[summary/owner] PASSED                                                                                                                                                                            [ 66%]
test_add_variety.py::test_add_6[summary/owner/done] PASSED                                                                                                                                                                       [100%]

$ pytest -v "test_add_variety.py::test_add_6[just summary]"
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch2/tasks_proj/tests, inifile: pytest.ini
collected 1 item                                                                                                                                                                                                                       

test_add_variety.py::test_add_6[just summary] PASSED  
```

# pytest フィクスチャ

## 概要

フィクスチャは、テストコードの構造化に欠かせない部分で、実際のテスト関数の実行に先立って、
pytest によって実行される関数。

* テストで使用するデータの取得
* テストを実行する前にシステムを既知の状態にする
* 複数のテストで使用するデータの準備

## 使用方法

@pytest.fixture() を使って、実行したい関数をフィクスチャにする。
テスト関数のパラメータリストにフィクスチャの名前を指定すると、テストを実行する前に
そのフィクスチャが pytest によって実行される。

テスト関数にデータを返すこともできる。

```bash
import pytest

@pytest.fixture()
def some_data():
    ""Return answer to ultimate question.""
    return 42

def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42
```

## 命名規則

pytest は、同じ名前のフィクスチャを現在のテストモジュール内で探す。
見つからなかった場合は、conftest.py ファイルも調べる。

## conftest.py を通じてフィクスチャを共有

複数のテストでフィクスチャを共有したい場合は、conftest.py をテストファイルと一緒に配置する。

ルートディレクトリのサブディレクトリに別の conftest.py を配置できる。
その場合は、そのディレクトリおよびそこに含まれているテストだけフィクスチャを利用できる。

conftest.py は、import conf でインポートしにこと。pytest によって読み込まれるローカルプラグインになるため。

ルートディレクトリに conftest.py を設置すれば、全てのテストで利用できる。

## tmpdir
テストで一時ディレクトリを扱うときに便利なフィクスチャ。

## yield

通常フィクスチャはテスト関数の実行前に処理されるが、yield を使用すると制御がテスト関数に譲渡され、
テスト関数終了後に残りの処理を実行できる。

yield 実行前 -> setUp, 実行後 -> tearDown のようなもの。

yield の後処理は、必ず実行される。(テストがエラーの場合でも)

yield からデータを返すことも可能。

## 構造化

コメントに GIVEN(前提) / WHEN (こうしたら) / THEN (こうなる) 形式のコメントでテストを構造化する。

こうしておくと task_db がフィクスチャであることがわかりやすくなる。(Given のコメントをみて)

```bash
def test_add_returns_valid_id(tasks_db):
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized tasks db (task_db が初期化ずみであるとすれば)
    # WHEN a new task is added(新しいタスクが追加されたときに)
    # THEN returned task_id is of type int(返される task_id は、int 型)
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)
```

以下の理由により、GIVEN の内容をできるだけフィクスチャとして表現するようにする。

 * テストが読みやすくなり、よって管理しやすくなる
 * フィクスチャでの assert や例外が ERROR になるのに対し、テストでの assert や例外が FAILED になる。
   よって、テストが失敗するのはテストの内容が直接失敗した時だけにできる。

## --setup-show

どのフィクスチャがどのように実行されたかを確認するためのオプション

```bash
$ pytest -v test_add.py -k valid_id
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch3/a/tasks_proj/tests, inifile: pytest.ini
collected 3 items / 2 deselected                                                                                                                                                                                                       

test_add.py::test_add_returns_valid_id PASSED

$ pytest --setup-show -v test_add.py -k valid_id
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch3/a/tasks_proj/tests, inifile: pytest.ini
collected 3 items / 2 deselected                                                                                                                                                                                                       

test_add.py::test_add_returns_valid_id 
SETUP    S tmpdir_factory
        SETUP    F tmpdir (fixtures used: tmpdir_factory)
        SETUP    F tasks_db (fixtures used: tmpdir)
        func/test_add.py::test_add_returns_valid_id (fixtures used: tasks_db, tmpdir, tmpdir_factory)PASSED
        TEARDOWN F tasks_db
        TEARDOWN F tmpdir
TEARDOWN S tmpdir_factory
```

## 複数のフィクスチャ
フィクスチャは、テスト関数や他のフィクスチャから利用できる。

```bash
@pytest.fixture()
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False))


@pytest.fixture()
def tasks_mult_per_owner():
    """Several owners with several tasks each."""
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),

        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),

        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel'))


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connected db with 3 tasks, all unique."""
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    """Connected db with 9 tasks, 3 owners, all with 3 tasks."""
    for t in tasks_mult_per_owner:
        tasks.add(t)
        

def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() affect on tasks.count()."""
    # GIVEN a db with 3 tasks
    #  WHEN another task is added
    tasks.add(Task('throw a party'))

    #  THEN the count increases by 1
    assert tasks.count() == 4
```

## フィクスチャのスコープ

フィクスチャの scope オプションパラメータは、フィクスチャのセットアップとティアダウンの実行タイミングを制御する。

* scope='function'
 - デフォルトのスコープ。テスト関数ごとに 1 回実行される。セットアップ部分は、このフィクスチャを使用しているテストの前に実行される。
   ティアダウン部分は、このフィクスチャを使用しているテストの後に実行される。
   
* scope='class'
 - テストクラスにテストメソッドがいくつ定義されているかに関係なく、テストクラスごとに 1 回実行される。
 
* scope='module'
 - モジュールにテスト関数、テストメソッド、他のフィクスチャがいくつ定義されているかに関係なく、モジュールごとに 1 回実行される。
   1 ファイルにつき、1 回実行される。

* socpe='session'
 - セッションごとに 1 回実行される。pytest コマンドでテストを 1 回実行するのが 1 1セッションとなる。
   セッションスコープのフィクスチャを使用するテストメソッドやテスト関数は全て、同じセットアップ/ティアダウン呼び出しを共有する。
   
フィクスチャが他のフィクスチャに依存する場合、依存先のフィクスチャは同じスコープかそれよりも広いスコープのものに限られる。
   
```bash
"""Demo fixture scope."""

import pytest


@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture."""


@pytest.fixture(scope='module')
def mod_scope():
    """A module scope fixture."""


@pytest.fixture(scope='session')
def sess_scope():
    """A session scope fixture."""


@pytest.fixture(scope='class')
def class_scope():
    """A class scope fixture."""


def test_1(sess_scope, mod_scope, func_scope):
    """Test using session, module, and function scope fixtures."""


def test_2(sess_scope, mod_scope, func_scope):
    """Demo is more fun with multiple tests."""

@pytest.mark.usefixtures('class_scope') # クラスでフィクスチャを使う指定
class TestSomething():
    """Demo class scope fixtures."""

    def test_3(self):
        """Test using a class scope fixture."""

    def test_4(self):
        """Again, multiple tests are more fun."""
```

## usefixtures

テスト関数やクラスに @pytest.mark.usefixtures('fixture1', 'fixture2') というマーカーを割り当てる方法もある。

usefixtures には、使用するフィクスチャの名前をコンマ区切りの文字列として指定できる。

テストでフィクスチャの戻り値を使用できるのは、そのフィクスチャがパラメータリストで指定されている場合のみ。
usefixtures を使用するとフィクスチャの戻り値を使用できない。

## autouse

autouse=True にするとフィクスチャを常に実行できるようになる(パラメータに指定しないで)。

この機能は、ある処理を必ず実行したい場合で、処理の結果やデータにテストが依存したいないときに便利。

常に実行されてしまうので、使いどころが重要。

## フィクスチャのパラメータ化

フィクスチャもパラメータ化できる。

```bash
"""Test the tasks.add() API function."""

import pytest
import tasks
from tasks import Task

tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))

task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done)
            for t in tasks_to_try]


def equivalent(t1, t2):
    """Check two tasks for equivalence."""
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))


@pytest.fixture(params=tasks_to_try)
def a_task(request):
    """Using no ids."""
    return request.param


def test_add_a(tasks_db, a_task):
    """Using a_task fixture (no ids)."""
    task_id = tasks.add(a_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, a_task)


@pytest.fixture(params=tasks_to_try, ids=task_ids)
def b_task(request):
    """Using a list of ids."""
    return request.param


def test_add_b(tasks_db, b_task):
    """Using b_task fixture, with ids."""
    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, b_task)


def id_func(fixture_value):
    """A function for generating ids."""
    t = fixture_value
    return 'Task({},{},{})'.format(t.summary, t.owner, t.done)


@pytest.fixture(params=tasks_to_try, ids=id_func)
def c_task(request):
    """Using a function (id_func) to generate ids."""
    return request.param


def test_add_c(tasks_db, c_task):
    """Use fixture with generated ids."""
    task_id = tasks.add(c_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, c_task)

```

request は、組み込みフィクスチャの一つであり、フィクスチャの呼び出し状態を表わす。

このフィクスチャには param というフィールドがあり、@pytest.fixture(params=tasks_to_tyr) にて、
param に代入されているリストの要素が 1 つ設定される。

テスト関数をパラメータ化するとそのテスト関数を複数回実行できる。一方、フィクスチャをパラメータ化すれば、
そのフィクスチャを使用するすべてのテスト関数を、それぞれ複数回実行できるようになる。

# 組み込みフィクスチャ

## tmpdir / tmpdir_factory
テストを実行する前に一時ディレクトリを作成し、テストの終了時にそのディレクトリを削除する。

ファイルの読み取り、書き込み、または変更を行うテストをする場合は、1 回のテストだけで使用するファイルや
ディレクトリの作成に tmpdir を使用する。関数スコープのフィクスチャのため、一時ファイルや一時ディレクトリを
1 つのテスト内でのみ利用する場合に用いる。

逆に 1 つのテスト関数の枠を超えて存続するようなファイルやディレクトリを tmpdir で作成することはできない。

```bash
def test_tmpdir(tmpdir):
    # tmpdir already has a path name associated with it
    # join() extends the path to include a filename
    # the file is created when it's written to
    a_file = tmpdir.join('something.txt')

    # you can create directories
    a_sub_dir = tmpdir.mkdir('anything')

    # you can create files in directories (created when written)
    another_file = a_sub_dir.join('something_else.txt')

    # this write creates 'something.txt'
    a_file.write('contents may settle during shipping')

    # this write creates 'anything/something_else.txt'
    another_file.write('something different')

    # you can read the files as well
    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'
```

tmpdir から返される値は、[py.path.local](https://py.readthedocs.io/en/latest/path.html) 型のオブジェクト。

複数のテストで使用するディレクトリを準備したい場合は、tempdir_factory を使用する。
ttmpdir_factory は、セッションスコープのフィクスチャ。

セッションスコープで作成されたファイルは、セッションが終了するまで存続します。

```bash
def test_tmpdir_factory(tmpdir_factory):
    # you should start with making a directory
    # a_dir acts like the object returned from the tmpdir fixture
    a_dir = tmpdir_factory.mktemp('mydir')

    # base_temp will be the parent dir of 'mydir'
    # you don't have to use getbasetemp()
    # using it here just to show that it's available
    base_temp = tmpdir_factory.getbasetemp()
    print('base:', base_temp)

    # the rest of this test looks the same as the 'test_tmpdir()'
    # example except I'm using a_dir instead of tmpdir

    a_file = a_dir.join('something.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'
```

セッションで使用するベースディレクトリは、以下。

```bash
$ pytest -q -s test_tmpdir.py::test_tmpdir_factory
base: /private/var/folders/zx/vr9x_3l51g3d02wd9dl7_vkw0000gn/T/pytest-of-hono/pytest-0
.
1 passed in 0.06 seconds
```

pytest-0 の 0 の部分は、テスト実行ごとにインクリメントされる。

また、ベースディレクトリは、テスト終了後、すぐに削除されるわけではなく、直近の数回分だけ残して過去のものは
pytest がクリーンアップしてくれる。

ベースディレクトリを指定したい場合は、pytest --basetemp=<ディレクトリ名>を指定する。

## 他のスコープの一時ディレクトリを使用する
モジュールスコープやクラススコープで一時ディレクトリが必要な場合は、必要なスコープのフィクスチャを新たに作成し、
そこから tmpdir_factory を呼び出す。

```bash
"""Demonstrate tmpdir_factory."""

import json
import pytest


@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    """Write some authors to a data file."""
    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'Sau Paulo'}
    }

    file_ = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file:{}'.format(str(file_)))

    with file.open('w') as f:
        json.dump(python_author_data, f)
    return file


----------

"""Some tests that use temp data files."""
import json


def test_brian_in_portland(author_file_json):
    """A test that uses a data file."""
    with author_file_json.open() as f:
        authors = json.load(f)
    assert authors['Brian']['City'] == 'Portland'


def test_all_have_cities(author_file_json):
    """Same file is used for both tests."""
    with author_file_json.open() as f:
        authors = json.load(f)
    for a in authors:
        assert len(authors[a]['City']) > 0
```

## pytestconfig

コマンドライン引数やコマンドラインオプション、構成ファイル、プラグインを通じた pytest の実行方法を制御できる。

このフィクスチャは、request.config のショートカットであり、pytest config object とも呼ばれる。

pytestconfig には、カスタムコマンドラインオプションを追加できる。

コマンドラインオプションの値は、pytestconfig から直接読み取ることができるが、新たにオプションを追加し、
pytest に解析させるには、フック関数を追加する必要がある。

フック関数は、pytest の振る舞いを制御するもう一つの方法。

pytest のコマンドラインに新しいオプションを追加するには、フック関数 pytest_addoption() を定義し、
pytest から呼び出されるようにする。

```conftest.py
def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true",
                     help="some boolean option")
    parser.addoption("--foo", action="store", default="bar",
                     help="foo: bar or baz")
```

pytest_addoption() を通じたコマンドラインオプションの追加は、プラグインで行うか、プロジェクトの
ディレクトリ構造ルートにある conftest.py ファイルで行うこと。サブディレクトリで行うべきではない。

```bash
pytest --help

custom options:
  --myopt              some boolean option
  --foo=Foo            foo: bar or baz
```

テストから利用する方法

```bash
import pytest


def test_option(pytestconfig):
    print('"foo" set to:', pytestconfig.getoption('foo'))
    print('"myopt" set to:', pytestconfig.getoption('myopt'))
```

pytestconfig は、フィクスチャであるため、他のフィクスチャからもアクセスできる。


```bash
@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo


@pytest.fixture()
def myopt(pytestconfig):
    return pytestconfig.option.myopt


def test_fixtures_for_options(foo, myopt):
    print('"foo" set to:', foo)
    print('"myopt" set to:', myopt)
```

## cache

テストセッションの情報を次のテストセッションに渡したい場合、cache を利用する。

cache は、あるテストセッションに関する情報を格納し、次のテストセッションで取得するためのフィクスチャ。

--last-failed と --failed-first もこの仕組みを利用している。

セッションに格納された情報は、以下のコマンドから確認できる。

```bash
pytest --cache-show
```

キャッシュをクリアしたい場合は、--cache-clear オプションを使用する。

cache フィクスチャのインターフェースを以下に示す。

```bash
cache.get(<キー>, <デフォルト>)
cache.set(<キー>, <値>)
```

キーの名前は、アプリケーションまたはプラグインの名前で始まり、スラッシュ、キー名の別の部分、スラッシュ・・・
という形式で構成される。


.cache ディレクトリのデータは、JSON 形式で表現されるので、JOSON と互換性があれば、どのような値でも問題ない。

```bash
import datetime
import pytest
import random
import time


@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(':', '_')
    # nodeid's can have colons
    # keys become filenames within .cache
    # replace colons with something filename safe
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)
    if last_duration is not None:
        errorstring = "test duration over 2x last duration"
        assert this_duration <= last_duration * 2, errorstring


@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())
```

# pytest の構成
pytest の構成ファイルを以下に示す。

* pytest.ini
  - pytest のデフォルトの振る舞いを変更できるようにするメインの構成ファイル。
 
* conftest.py
  - ローカルプラグイン。conftest.py ファイルが存在するディレクトリとその全てのサブディレクトリでフック関数とフィクスチャが利用可能になる。

* __init__.py
  - このファイルをテストディレクトリごとに配置すると、複数のテストディレクトリで同じ名前のテストファイルを使用できるようになる。

* tox.ini
  - tox の pytest.ini に相当するファイル。このファイルを追加する場合、pytest.ini は不要。(設定の一本化)

## .ini ファイルの有効なオプション

```bash
$ pytest --help

[pytest] ini-options in the first pytest.ini|tox.ini|setup.cfg file found:

  markers (linelist)       markers for test functions
  empty_parameter_set_mark (string) default marker for empty parametersets
  norecursedirs (args)     directory patterns to avoid for recursion
  testpaths (args)         directories to search for tests when no files or directories are given in the command line.
  console_output_style (string) console output: classic or with additional progress information (classic|progress).
  usefixtures (args)       list of default fixtures to be used with this project
  python_files (args)      glob-style file patterns for Python test module discovery
  python_classes (args)    prefixes or glob names for Python test class discovery
  python_functions (args)  prefixes or glob names for Python test function and method discovery
  xfail_strict (bool)      default for the strict parameter of xfail markers when not given explicitly (default: False)
  junit_suite_name (string) Test suite name for JUnit report
  junit_logging (string)   Write captured log messages to JUnit report: one of no|system-out|system-err
  junit_duration_report (string) Duration time to report: one of total|call
  doctest_optionflags (args) option flags for doctests
  doctest_encoding (string) encoding used for doctest files
  cache_dir (string)       cache directory path.
  filterwarnings (linelist) Each line specifies a pattern for warnings.filterwarnings. Processed after -W and --pythonwarnings.
  log_print (bool)         default value for --no-print-logs
  log_level (string)       default value for --log-level
  log_format (string)      default value for --log-format
  log_date_format (string) default value for --log-date-format
  log_cli (bool)           enable log display during test run (also known as "live logging").
  log_cli_level (string)   default value for --log-cli-level
  log_cli_format (string)  default value for --log-cli-format
  log_cli_date_format (string) default value for --log-cli-date-format
  log_file (string)        default value for --log-file
  log_file_level (string)  default value for --log-file-level
  log_file_format (string) default value for --log-file-format
  log_file_date_format (string) default value for --log-file-date-format
  addopts (args)           extra command line options
  minversion (string)      minimally required pytest version
```

## pyetst の最低バージョンを指定する

minversion を使用する。

## pytest が間違った場所を調べないようにする

norecursedirs を使用する。

## テストディレクトリの場所を指定する。

testpaths を使用する。

この設定が使用されるのは、ディレクトリ、ファイル、または、nodeid が引数に指定されていない場合だけ。

設定は、ルートディレクトリを基準とした相対パスで指定する。

# テストディスカバリのルール

* 1 つ以上のディレクトリから開始する。コマンドラインにファイル名または、ディレクトリ名を指定できる。何指定しない場合は、現在のディレクトリが指定される。
* そのディレクトリと全てのサブディレクトリでテストモジュールを再帰的に調べる
* テストモジュールとは、test_*.py や *_test.py のような名前がついたファイルのことをさす。
* テストモジュールで、test_で始まる名前の関数を調べる
* Test で始まる名前のクラスを調べる。それらのうち、__init__ メソッドを持たないクラスで、test_ で始まるメソッドを調べる。

## python_classes
テストクラス名のルールを pytest_classes で変更できる。

```bash
[pytest]
python_classes = *Test Test* *Suite
```

## python_files
デフォルトのファイル検索ルールを変更できる。

```bash
[pytest]
python_files - test_* *_test check_*
```

## python_functions

テストメソッドのルールを変更する。

```bash
[pytest]
python_function = test_* check_*
```

## XPASS を許可しない
xfail_strict=true を設定すると @pytest.mark.xfail のマークがついたテsつ蘇我失敗しなかった場合、
エラーとして報告される。

## --markers

```pytest.ini
markers =
    smoke: All critical smoke tests
    body: All car body tests
    entertainment: All tests covering the entertainment system
```

```bash
$ pytest --markers
@pytest.mark.smoke: All critical smoke tests

@pytest.mark.body: All car body tests

@pytest.mark.entertainment: All tests covering the entertainment system

@pytest.mark.filterwarnings(warning): add a warning filter to the given test. see https://docs.pytest.org/en/latest/warnings.html#pytest-mark-filterwarnings 

@pytest.mark.skip(reason=None): skip the given test function with an optional reason. Example: skip(reason="no way of currently testing this") skips the test.

@pytest.mark.skipif(condition): skip the given test function if eval(condition) results in a True value.  Evaluation happens within the module global context. Example: skipif('sys.platform == "win32"') skips the test if we are on the win32 platform. see https://docs.pytest.org/en/latest/skipping.html

@pytest.mark.xfail(condition, reason=None, run=True, raises=None, strict=False): mark the test function as an expected failure if eval(condition) has a True value. Optionally specify a reason for better reporting and run=False if you don't even want to execute the test function. If only specific exception(s) are expected, you can list them in raises, and if the test fails in other ways, it will be reported as a true failure. See https://docs.pytest.org/en/latest/skipping.html

@pytest.mark.parametrize(argnames, argvalues): call a test function multiple times passing in different arguments in turn. argvalues generally needs to be a list of values if argnames specifies only one name or a list of tuples of values if argnames specifies multiple names. Example: @parametrize('arg1', [1,2]) would lead to two calls of the decorated test function, one with arg1=1 and another with arg1=2.see https://docs.pytest.org/en/latest/parametrize.html for more info and examples.

@pytest.mark.usefixtures(fixturename1, fixturename2, ...): mark tests as needing all of the specified fixtures. see https://docs.pytest.org/en/latest/fixture.html#usefixtures 

@pytest.mark.tryfirst: mark a hook implementation function such that the plugin machinery will try to call it first/as early as possible.

@pytest.mark.trylast: mark a hook implementation function such that the plugin machinery will try to call it last/as late as possible.
```

# pytest-html

```bash
pip install pytest-html

pytest --html"result.html"


pytest --junitxml="results.xml"
```

# pytest fixture

[pytest fixture](https://docs.pytest.org/en/latest/fixture.html)

# Customizing Test Runs with the Command Line and Configuration Files

* [Python argparse documentation](https://docs.python.org/3/library/argparse.html)
* [Git repo containing this lecutre's code](https://github.com/brandonblair/elegantframeworks/tree/config_recipe)

```bash
custom options:
  --env=ENV             Environment to run tests against
```

# pytest - Skip
[Ref](https://docs.pytest.org/en/latest/skipping.html)

```bash
@mark.skip(reason='Not a staging environment')
def test_environment_is_staging(app_config):
    base_url = app_config.base_url
    assert base_url == 'staging'
    
$ pytest --env dev -v -rs
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.2.0, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/pytest_code/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/custom_config, inifile: pytest.ini
collected 3 items                                                                                                                                                                                                                      

tests/test_environment.py::test_environment_is_qa SKIPPED                                                                                                                                                                        [ 33%]
tests/test_environment.py::test_environment_is_dev PASSED                                                                                                                                                                        [ 66%]
tests/test_environment.py::test_environment_is_staging SKIPPED                                                                                                                                                                   [100%]
======================================================================================================= short test summary info ========================================================================================================
SKIPPED [1] tests/test_environment.py:4: broken by deploy somenumber
SKIPPED [1] tests/test_environment.py:19: Not a staging environment
```

It is useful by using xfail.

```bash
@mark.xfail
def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80


def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydev-env.com'
    assert port == 8080

(venv) $ pytest --env dev -v -rs
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.2.0, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/pytest_code/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/custom_config, inifile: pytest.ini
collected 2 items                                                                                                                                                                                                                      

tests/test_environment.py::test_environment_is_qa XFAIL                                                                                                                                                                          [ 50%]
tests/test_environment.py::test_environment_is_dev PASSED                                                                                                                                                                        [100%]
```

# Cross-Browser and Data-driven testing with parametrize

* [Training Ground](https://techstepacademy.com/training-ground)
* [Parametrizing fixtures and test functions](https://docs.pytest.org/en/latest/parametrize.html)
* [Setting Up Selenium with Webdrivers](https://www.udemy.com/elegant-browser-automation-with-python-and-selenium/)
* [elegantframeworks](https://github.com/brandonblair/elegantframeworks/tree/parametrize)


```bash
from pytest import mark

@mark.parametrize('tv_brand', [
        ('Samsung'),
        ('Sony'),
        ('Vizio')
    ]
)
def test_television_turns_on(tv_brand):
    print(f'{tv_brand} turns on as expected')
    
pytest -v -s
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.2.0, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/pytest_code/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/elegantframeworks/tests, inifile:
collected 3 items                                                                                                                                                                                                                      

test_television.py::test_television_turns_on[Samsung] Samsung turns on as expected
PASSED
test_television.py::test_television_turns_on[Sony] Sony turns on as expected
PASSED
test_television.py::test_television_turns_on[Vizio] Vizio turns on as expected
PASSED
```

```bash
from pytest import fixture
from selenium import webdriver


@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()
```

## データを持たせる

test_data.json

```bash
[
  "Sony",
  "Samsung",
  "Vizio"
]
```

conftest.py

```bash
import json

from pytest import fixture

data_path = 'test_data.json'


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(params=[load_test_data(data_path)])
def tv_brand(request):
    data = request.param
    return data
```

test_television.py

```bash
from pytest import mark


def test_television_turns_on(tv_brand):
    print(f'{tv_brand} turns on as expected')

```

## Fast Testing with Pytest-xdist, and Parallel vs Concurrent

[Ref](https://github.com/BrandonBlair)  
[pytest-xdist](https://pypi.org/project/pytest-xdist/)

```bash
pip install pytest-xdist

# 並列実行(n => 実行数)
pytest -s -v -n4 test_chemistry_results.py 


pytest -s -v -nauto test_chemistry_results.py


```



