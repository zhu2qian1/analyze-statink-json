# analyze-statink

## 利用方法 Usage

```sh
./fetch "https://stat.ink/@zhu2113/salmon3.json?f%5Blobby%5D=normal&f%5Bmap%5D=donburako&f%5Bresult%5D=cleared"
./run
```

fetch 関数には stat.ink の左上の波括弧 `({})` を押下したときに表示される URL 文字列を渡してください。  
実行したら、 run 関数を実行してください。集計結果が出力されます。

Give fetch function the url of json (can be retrieved gray curly braces button on upper left).  
Then run `./run`.

## Todos

- [ ] pretty-print の実装。
- [ ] 集計項目をカスタマイズ可能にする。
- [ ] サーモンラン以外の集計にも対応する。
- [ ] Web アプリに乗せる (Django を検討)。
