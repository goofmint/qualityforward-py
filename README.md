# QualityForward用Pythonライブラリ

## 使い方

```py
from qualityforward.QualityForward import QualityForward

if __name__ == '__main__':
    q = QualityForward("0aa...340") # APIキー
    print(q.get_current_project().name) # -> サンプルプロジェクト
```

## テストスイート

### 取得

```py
q.get_test_suites()
```

### 作成

```py
ts = q.TestSuite()
ts.project_id = 748
ts.name = 'Test test suite'
ts.label_category1 = '機能カテゴリ';
ts.use_category1 = True;
ts.label_content1 = '環境';

v = ts.version()
v.set('name', 'バージョン1')
ts.set_version(v)

ts.save()
```

### 削除

```py
ts.destroy
```

## LICENSE

MIT
