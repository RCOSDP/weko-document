# クローラリストの変更

## 前提条件

従来のJAIRO Cloudクローラリスト（https://bitbucket.org/niijp/jairo-crawler-list)を
COUNTER Robots(https://github.com/atmire/COUNTER-Robots/tree/master)のような正規表現を含むリストに変更する。

IPアドレスリストは以下の様に正規表現で記述する。

```
^1\.1\.1\.1$
^11\.11\.11\.11$
```

新しいリストのURLは現状のリストとは異なるものと想定する。

以下手順では旧クローラリストを以下とする。

https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_ip_blacklist.txt
https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_useragent.txt


また、新クローラリストを以下とする。

https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_ip_blacklist_new.txt
https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_useragent_new.txt

また、RedisキーのTTLは 86400 秒とする。

## 事前作業

### Redisに事前にキーを設定する

新旧の環境がクローラリストを参照できるようにする。

まずはじめに、redisに新クローラリストの値を設定する。

値は正規表現をパイプ（|）でつなぎ合わせた文字列となる。

具体的なイメージとしては、以下のような正規表現があった場合、

```
^1\.1\.1\.1$
^11\.11\.11\.11$
```

以下のような文字列を作成する。

```
^1\.1\.1\.1$|^11\.11\.11\.11$
```

登録のイメージは以下の通りとなる。

```
SET "https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_ip_blacklist_new.txt" "^1\.1\.1\.1$|^11\.11\.11\.11$"
SET "https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_useragent_new.txt" "bot|googlebot"
```

また、あわせてTTLも設定する。

```
EXPIRE "https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_ip_blacklist_new.txt" 86400
EXPIRE "https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_useragent_new.txt" 86400
```

最後に旧クローラリストのTTLを延長する。

```
EXPIRE "https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_ip_blacklist.txt" 86400
EXPIRE "https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_useragent.txt" 86400
```

## 切り替え作業


### 設定を変更する

instance.cfg　に以下設定を追加する。

```
WEKO_ADMIN_USE_REGEX_IN_CRAWLER_LIST = True
```

### 再起動を行う


### クローラリストを新しいものに変更する

管理画面（/admin/loganalysissetting/）またはデータベースを直接書き換える。


データベース調節書き換える場合は、以下クエリを参考とする。

```
UPDATE loganalysis_restricted_crawler_list SET list_url='https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_ip_blacklist_new.txt' WHERE id = 1;
UPDATE loganalysis_restricted_crawler_list SET list_url='https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_useragent_new.txt' WHERE id = 2;
```

## 検証

ボットによるアイテムアクセスリクエストを再現する。

```
curl -k -I -H "User-Agent: alexa" "https://localhost/records/2000001"
```

イベントキューを処理する。


```
invenio stats events process
```

elasticsearch の```-events-stats-record-view```インデックスのドキュメントを確認し、
当該リクエストのis_restrictedがtrueとなっていることを確認する。

クローラリストおよびIP除外リストに該当するリクエストは、
is_restrictedがtrueとなる。

## 事後処理

旧クローラリストを参照する機関がなくなったら、旧クローラリストを削除する。

```
DEL "https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_ip_blacklist.txt"
DEL "https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_useragent.txt"
```



