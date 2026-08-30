# 制限公開機能切り替えスクリプト手順書
## 目次
* [概要](#概要)
* [前提](#前提)
* [制限公開機能有効化](#制限公開機能有効化)
    * [事前準備（有効）](#事前準備有効)
    * [実施手順（有効）](#実施手順有効)
    * [実施手順（有効）にて発生するエラー](#実施手順有効にて発生するエラー)
    * [切り戻し手順（有効）](#切り戻し手順有効)
* [制限公開機能無効化](#制限公開機能無効化)
    * [事前準備（無効）](#事前準備無効)
    * [実施手順（無効）](#実施手順無効)
    * [実施手順（無効）にて発生するエラー](#実施手順無効にて発生するエラー)
    * [切り戻し手順（無効）](#切り戻し手順無効)
* [補足資料](#補足資料)
    * [設定値一覧](#設定値一覧)
    * [SQL実行一覧](#sql実行一覧)
    * [設定値確認ツール説明](#設定値確認ツール説明)
    * [レコード確認ツール説明](#レコード確認ツール説明)

## 概要
本手順書は、制限公開機能を一括で有効/無効にする手順を示したものである。  
制限公開機能の有効/無効切り替えは以下の手順に従って実施される。  
**事前準備**
* 現在のDB状態の確認（機能有効時のみ）
* 登録されるレコードの期待結果の修正（機能有効時のみ）
* 変更する設定値の修正
* 実行するSQLファイルの修正（機能有効時のみ）
* スクリプトの設定値修正
* 修正ファイルの提供

**機能有効/無効**
* 機能有効/無効時に使用するファイルの確認・配置
* サービスの停止
* 設定値とDBのバックアップ
* スクリプトの実行
* 機能有効/無効化の確認・反映

手順の確認はそれぞれ以下の項目を参照すること。
* 事前準備
    * 有効時：[事前準備（有効）](#事前準備有効)
    * 無効時：[事前準備（無効）](#事前準備無効)
* 機能有効/無効
    * 有効時：[実施手順（有効）](#実施手順有効)
    * 無効時：[実施手順（無効）](#実施手順無効)

この切り替え処理の対象は[設定値一覧](#設定値一覧)に記載している。  
機能有効/無効時に登録・更新されるテーブルは[SQL実行一覧](#sql実行一覧)に記載してある。

なお、このスクリプトはサービスを停止した状態で実行されることを想定しているため、制限公開機能を有効/無効化する際はサービスを停止したうえで実行すること。

## 前提
本手順では以下のファイルを使用する。  
現在のWEKOのソースに含まれない、または最新でないものであるため、以下のコマンドを実行して事前に取得する必要がある。
```sh
# コンテナ外で実施する
curl -o scripts/demo/resticted_access.sql https://raw.githubusercontent.com/ivis-weko3-dev/weko/refs/heads/fix/issue59959/scripts/demo/resticted_access.sql
curl -o tools/switch_restricted_access/disable/get_target_table_hash.sql https://raw.githubusercontent.com/ivis-weko3-dev/weko/refs/heads/fix/issue59959/tools/switch_restricted_access/disable/get_target_table_hash.sql
curl -o tools/switch_restricted_access/disable/verify_table.json https://raw.githubusercontent.com/ivis-weko3-dev/weko/refs/heads/fix/issue59959/tools/switch_restricted_access/disable/verify_table.json
curl -o tools/switch_restricted_access/enable/get_target_table_hash.sql https://raw.githubusercontent.com/ivis-weko3-dev/weko/refs/heads/fix/issue59959/tools/switch_restricted_access/enable/get_target_table_hash.sql
curl -o tools/switch_restricted_access/enable/verify_table.json https://raw.githubusercontent.com/ivis-weko3-dev/weko/refs/heads/fix/issue59959/tools/switch_restricted_access/enable/verify_table.json
curl -o tools/disable_restricted_access.sh https://raw.githubusercontent.com/ivis-weko3-dev/weko/refs/heads/fix/issue59959/tools/disable_restricted_access.sh
curl -o tools/restricted_upadate.sh https://raw.githubusercontent.com/ivis-weko3-dev/weko/refs/heads/fix/issue59959/tools/restricted_upadate.sh
curl -o tools/update_restricted_access_property.py https://raw.githubusercontent.com/ivis-weko3-dev/weko/refs/heads/fix/issue59959/tools/update_restricted_access_property.py
curl -o tools/verify_restricted_records.py https://raw.githubusercontent.com/ivis-weko3-dev/weko/refs/heads/fix/issue59959/tools/verify_restricted_records.py
curl -o tools/verify_restricted_update.sh https://raw.githubusercontent.com/ivis-weko3-dev/weko/refs/heads/fix/issue59959/tools/verify_restricted_update.sh
```

## 制限公開機能有効化
### 事前準備（有効）
事前準備ではサービスの停止は不要。
#### 1. 現在のDB状態の確認
**本手順は運用担当者が行う**  
本手順で使用しているverify_table.jsonは`tools/switch_restricted_access/enable/verify_table.json`を指す。
1. 以下のコマンドを実行し、編集していない状態のverify_table.jsonと現在登録されているレコードとの状態を確認する。
    ```sh
    # コンテナ外で実施する
    docker compose exec web invenio shell tools/verify_restricted_records.py enable
    ```
    出力結果の見方は[レコード確認ツール説明](#レコード確認ツール説明)を参照すること。
1. ツールの出力結果と最終行の`Tables with all records correct`、`Table with some records correct`と`Table with no records correct`に表示されたテーブルの全レコード情報を取得し、NII担当者へ提供する。

#### 2. 登録されるレコードの期待結果の修正
**本手順はNII担当者が行う**    
本手順で使用しているverify_table.jsonは`tools/switch_restricted_access/enable/verify_table.json`を指す。
1. 運用担当者より提供されたツールの出力結果最終行にある`Table with some records correct`および`Table with no records correct`に記載されたテーブル1つずつに対し以下の手順を実施する。
    1. 出力結果より`Verifying <確認対象のテーブル> records...`と書かれた行を検索する。
    1. 1.1.でヒットした行から`Verifying <別のテーブル> records...`または`Verification completed.`が書かれた行までを1行ずつ確認する。
        1. `Record with id <レコードのID> not found.`と書かれていた場合、運用担当者より提供されたレコード情報を確認する。
            1. 確認対象のレコードが別IDで登録されていた場合、verify_table.jsonにて確認対象レコード情報のIDを登録されていたIDに修正する。  
                各テーブルの確認情報がどの行に記載されているかは本手順の末尾に記載する。
            1. 確認対象のレコードが別IDでも登録されていなかった場合、何も行わない。
        1. `Mismatch for id <レコードのID> on field '<カラム名>': expected: <期待結果>, got <実行結果>`と書かれていた場合、運用担当者より提供されたレコード情報を確認する。
            1. 確認対象のレコードが別IDで登録されていた場合、verify_table.jsonにて確認対象レコード情報のIDを登録されていたIDに修正する。
                各テーブルの確認情報がどの行に記載されているかは本手順の末尾に記載する。
            1. 確認対象のレコードが別IDでも登録されていなかった場合、verify_table.jsonにて確認対象レコード情報のIDと登録可能なIDに修正する。
            1. 確認対象のレコードが同じIDで登録されている場合、verify_table.jsonにて確認対象レコード情報の差分の生じていたカラムの値を出力された実行結果に修正する。
        1. `Record with id <レコードのID> verified successfully.`と書かれていた場合、何も行わない。

確認対象のテーブルは[SQL実行一覧](#sql実行一覧)に記載されている。  
verify_table.jsonに記載されている各テーブルの記載行は以下の通り。
|テーブル名|記載行|
|---|---|
|item_type_name|2~27|
|item_type|28~73|
|item_type_mapping|74~99|
|item_type_property|100~236|
|accounts_role|237~241|
|index|242~315|
|workflow_flow_define|316~361|
|workflow_flow_action|362~528|
|workflow_workflow|529~582|
|workflow_userrole|583~629|
|mail_template_genres|630~643|
|mail_templates|644~750|
|admin_settings|751~794|

#### 3. 変更する設定値の修正
**本手順はNII担当者が行う**
1. 設定ファイルに記載される設定値の修正を行う。
    1. 以下のコマンドを実行し、修正予定の設定値修正コマンドが記載されたスクリプトを開く。
        ```sh
        # コンテナ外で実施する
        vi tools/restricted_upadate.sh
        ```
    1. 1.1.で開いたファイルにて各設定値に登録する値と、下記表にある設定値のデフォルト値とを比較し、その結果に応じて以下の手順を実施する。
        |設定値名|モジュール名|デフォルト値|変更対象行
        |---|---|---|---|
        |WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG|weko-admin|False|12~17|
        |WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS|weko-admin|True|20~25|
        |WEKO_RECORDS_UI_RESTRICTED_API|weko-records-ui|False|28~33|
        |WEKO_ITEMS_UI_PROXY_POSTING|weko-items-ui|False|36~41|
        |WEKO_ITEMTYPES_UI_FORCED_IMPORT_ENABLED|weko-itemtypes-ui|False|44~49|
        |WEKO_INDEX_TREE_SHOW_MODAL|weko-index-tree|False|52~57|
        |WEKO_USERPROFILES_CUSTOMIZE_ENABLED|weko-user-profiles|False|60~65|
        |INVENIO_MAIL_ADDITIONAL_RECIPIENTS_ENABLED|invenio-mail|False|68~73|
        1. 2つの値が一致している場合、設定ファイル（デフォルト名：instance.cfg）より削除するため、上記表にある変更対象行の部分を以下コマンドに置き換える。
            ```sh
            grep -E "^<設定値名> *= *.*$" $SETTING_FILE
            if [ $? -eq 0 ]; then
                sed -i.bak '/<設定値名> *= *.*/d' $SETTING_FILE
            fi
            ```
            例：WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG に対して行うとき、12行目から17行目を以下のコマンドに置き換える。
            ```sh
            grep -E "^WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG *= *.*$" $SETTING_FILE
            if [ $? -eq 0 ]; then
                sed -i.bak '/WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG *= *.*/d' $SETTING_FILE
            fi
            ```
        1. 2つの値が異なっている場合、設定ファイル（デフォルト名：instance.cfg）にて設定を追加するため、上記表にある変更対象行の部分を以下コマンドに置き換える。
            ```sh
            grep -E "^<設定値名> *= *.*$" $SETTING_FILE
            if [ $? -ne 0 ]; then
                echo '<設定値名> = <設定したい値>' >> $SETTING_FILE
            else
                sed -i.bak 's/<設定値名> *= *.*/<設定値名> = <設定したい値>/' $SETTING_FILE
            fi
            ```
            例：WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG を True で設定するとき、12行目から17行目を以下のコマンドに置き換える。
            ```sh
            grep -E "^WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG *= *.*$" $SETTING_FILE
            if [ $? -ne 0 ]; then
                echo 'WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG = True' >> $SETTING_FILE
            else
                sed -i.bak 's/WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG *= *.*/WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG = True/' $SETTING_FILE
            fi
            ```
            例：WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG を False で設定するとき、12行目から17行目を以下のコマンドに置き換える。
            ```sh
            grep -E "^WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG *= *.*$" $SETTING_FILE
            if [ $? -ne 0 ]; then
                echo 'WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG = False' >> $SETTING_FILE
            else
                sed -i.bak 's/WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG *= *.*/WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG = False/' $SETTING_FILE
            fi
            ```
1. SQLファイルに記載されている設定値の修正を行う。
    1. 以下のコマンドを実行し、修正予定の設定値が記載されたSQLファイルを開く。
        ```sh
        # コンテナ外で実施する
        vi scripts/demo/resticted_access.sql
        ```
    1. 2.1.で開いたファイルにて各設定値に登録する値を確認し、下記表の変更対象行に記載されている行にある`true`という文字を設定する値に変更する。
        |設定値名|変更対象行|
        |---|---|
        |password_enable|1607, 1619|
        |item_application.item_application_enable|1607, 1622|
        |display_request_form|1607, 1625|
        |secret_URL_file_download.secret_enable|1607, 1628|
        |edit_mail_templates_enable|1607, 1631|
        |preview_workflow_approval_enable|1607, 1634|
        ```
        例：password_enable を False で設定する場合
            1.3.で開いたファイルの1619行目を以下のように修正する。
                                        , 'false'::jsonb
            また、1607行目の"password_enable"というキーに対応する値をfalseに修正する。
        ```

#### 4. 実行するSQLファイルの修正
**本手順はNII担当者が行う**  
本手順は[登録されるレコードの期待結果の修正](#2-登録されるレコードの期待結果の修正)にて`tools/switch_restricted_access/enable/verify_table.json`を修正した場合のみ実行する。
1. 以下のコマンドを実行し、修正対象のSQLが書かれたSQLファイルを開く。
    ```sh
    # コンテナ外で実施する
    vi scripts/demo/resticted_access.sql
    ```
1. `tools/switch_restricted_access/enable/verify_table.json`について、編集前との差分を取得する。
1. 取得した差分を1.で開いたファイルに反映させる。  
    修正対象のテーブルは[SQL実行一覧](#sql実行一覧)に記載されている。  
    各テーブルのSQL文の記載箇所は以下の表の通り。
    |テーブル名|変更対象SQL文記載行|
    |---|---|
    |item_type_name|18~23|
    |item_type|29~82|
    |item_type_mapping|88~121|
    |item_type_property|127~293|
    |accounts_role|299~301|
    |index|311~388|
    |workflow_flow_define|394~447|
    |workflow_flow_action|453~664|
    |workflow_workflow|670~731|
    |workflow_userrole|736~746|
    |mail_template_genres|758~762|
    |mail_templates|774~1591|
    |admin_settings|1603~1635|

#### 5. スクリプトの設定値修正（有効）
**本手順はNII担当者が行う** 
1. 以下のコマンドを実行し、変更予定の設定値が記載されたスクリプトファイルを開く。
    ```sh
    # コンテナ外で実施する
    vi tools/restricted_upadate.sh
    ```
1. 1.で開いたファイルの5行目の`SETTING_FILE`を設定ファイル（デフォルト名：instance.cfg、環境差異あり）が置かれたパスに書き換える。
1. 同様に6行目の`RESTRICTED_ACCESS_PROPERTY`を`scripts/demo/resticted_access.sql`の285行目の値に書き換える。

#### 6. 修正ファイルの提供（有効）
**本手順はNII担当者が行う**
1. [登録されるレコードの期待結果の修正](#2-登録されるレコードの期待結果の修正)、[変更する設定値の修正](#3-変更する設定値の修正)、[実行するSQLファイルの修正](#4-実行するsqlファイルの修正)、[スクリプトの設定値修正（有効）](#5-スクリプトの設定値修正有効)にて修正した以下のファイルを運用担当者に提供する。
    * tools/switch_restricted_access/enable/verify_table.json
    * tools/restricted_upadate.sh
    * scripts/demo/resticted_access.sql

### 実施手順（有効）
#### 1. 機能有効時に使用するファイルの確認・配置
1. 制限公開機能を有効化する際に以下の表に書かれたファイルを使用している。  
    そのため、ファイルが参照先パスへ配置されているか確認を行い、配置されていない場合はそれぞれ指定されているファイルを参照先パスへ配置する。  
    また、[修正ファイルの提供（有効）](#6-修正ファイルの提供有効)にて渡されたファイルはそのファイルを正として参照先パスへ配置する。
    |ファイル名|説明|参照先パス|
    |---|---|---|
    |instance.cfg（デフォルト値、環境差異あり）|WEKOで使用する設定値が記載されたファイル|scripts/instance.cfg|
    |resticted_access.sql|制限公開機能の有効化クエリおよび制限公開で使用するレコードの追加クエリが書かれたファイル|scripts/demo/resticted_access.sql|
    |update_restricted_access_property.py|制限公開用プロパティにアクセスに「制限公開」を追加するファイル|tools/update_restricted_access_property.py|
    |schema.json|item_type_propertyテーブルの制限公開用プロパティのschemaカラムに登録する制限公開機能有効時の値が書かれたファイル|tools/switch_restricted_access/enable/schema.json|
    |form.json|item_type_propertyテーブルの制限公開用プロパティのformカラムに登録する制限公開機能有効時の値が書かれたファイル|tools/switch_restricted_access/enable/form.json|
    |forms.json|item_type_propertyテーブルの制限公開用プロパティのformsカラムに登録する制限公開機能有効時の値が書かれたファイル|tools/switch_restricted_access/enable/forms.json|
    |verify_restricted_update.sh|制限公開機能の設定が有効化されたかを確認するファイル|tools/verify_restricted_update.sh|
    |verify_restricted_records.py|制限公開機能で使用するレコードが正しく反映されたかを確認するファイル|tools/verify_restricted_records.py|
    |verify_table.json|制限公開機能有効時のレコード検証に使用するファイル|tools/switch_restricted_access/enable/verify_table.json|
    |get_target_table_hash.sql|制限公開機能有効時の切り戻しの検証に使用するファイル|tools/switch_restricted_access/enable/get_target_table_hash.sql|

#### 2. サービスの停止
1. 本スクリプトはサービス停止した状態で実行されることが前提であるため、WEKOのサービスを停止する。

#### 3. 設定値とDBのバックアップ（有効）
1. instance.cfg（デフォルト値、環境差異あり）をコピーして、現在の設定値のバックアップを取得する。
1. 以下コマンドを実行し、[SQL実行一覧](#sql実行一覧)に記載されているテーブルとそれらに紐づくテーブルのバックアップを取得する。
    ```sh
    # コンテナ外で実施する
    docker compose exec postgresql pg_dump -d invenio -U invenio -t 'item_type_name' -t 'item_type' -t 'item_type_mapping' -t 'item_type_property' -t 'accounts_role' -t 'index' -t 'workflow_flow_define' -t 'workflow_flow_action' -t 'workflow_workflow' -t 'workflow_userrole' -t 'mail_template_genres' -t 'mail_templates' -t 'admin_settings' -t 'item_type_edit_history' -t 'jsonld_mappings' -t 'rocrate_mapping' -t 'access_actionsroles' -t 'accounts_userrole' -t 'communities_community' -t 'shibboleth_userrole' -t 'workflow_flow_action_role' -t 'harvest_settings' -t 'journal' -t 'resync_indexes' -t 'workflow_activity' -t 'sword_clients' -t 'mail_template_users' -t 'author_affiliation_community_relations' -t 'author_community_relations' -t 'author_prefix_community_relations' -t 'communities_community_record' -t 'communities_featured_community' -t 'user_activity_logs' -t 'resync_logs' -t 'workflow_activity_action' -f enable_dump.sql --clean
    ```
1. 以下コマンドを実行し、切り戻し対応した場合の検証に用いるファイルを作成する。
    ```sh
    # コンテナ外で実施する
    docker cp tools/switch_restricted_access/enable/get_target_table_hash.sql $(docker compose ps -q postgresql):/tmp/get_target_table_hash.sql
    docker compose exec postgresql psql -d invenio -U invenio -f /tmp/get_target_table_hash.sql > dump_hash.txt
    ```

#### 4. スクリプトの実行（有効）
1. 以下コマンドを実行し、設定の更新およびレコードの登録を行う。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
    このスクリプトでは以下の処理を行っている。  
    a. [設定値一覧](#設定値一覧)のすべての設定値を有効（True）にする。  
    b. 制限公開用のレコードが存在しない場合はレコードを追加する。  
    c. 制限公開用プロパティのアクセスに「制限公開」を追加する。  
    d. [設定値一覧](#設定値一覧)のすべての設定値が有効（True）となっているか確認する。  
    e. 制限公開用のレコードがすべて反映されているかを確認する。  
    本スクリプトは、エラーが発生した箇所にて処理が停止するよう設計されている。
1. ツール実行時にコンソール上へエラーが出力された場合には、[実施手順（有効）にて発生するエラー](#実施手順有効にて発生するエラー)を確認し、発生したエラーに応じた項番の対処方法を実施する。
    1. 再実行後成功した場合は[5.](#5-機能有効化の確認反映)の手順を実施する。
    1. 再実行しても失敗する場合はエラーログを取得したうえで[切り戻し手順（有効）](#切り戻し手順有効)を実施する。 
 
#### 5. 機能有効化の確認・反映
1.  設定値が期待通り変更されたか確認する。
    1. [4.](#4-スクリプトの実行有効)の1.のd.で出力された結果を1行ずつ確認する。  
        出力結果の見方は[設定値確認ツール説明](#設定値確認ツール説明)に記載されている。
    1. `FAIL`と出力された設定値がある場合、以下コマンドでその設定値の記載箇所を検索する。
        ```sh
        # コンテナ外で実施する
        grep -F '<設定値>' tools/restricted_upadate.sh
        ```
        1. `echo '<設定値> = True' >> $SETTING_FILE`が出力された場合、適切に設定値の設定ができていないため、instance.cfg（デフォルト値、環境差異あり）に対し、`<設定値> = True`を直接追加する。
        1. 以下が出力された場合、または何も出力されなかった場合は正常であるため、次の設定値の確認を行う。
            * `echo '<設定値> = False' >> $SETTING_FILE`
            * `sed -i.bak '/<設定値> *= *.*/d' $SETTING_FILE`
    1. すべての設定値が確認完了、かつ失敗した設定値の修正が完了したら、以下のコマンドを実行してレコードが正常に登録されたかを確認する。
        ```sh
        # コンテナ外で実施する
        docker compose exec web invenio shell tools/verify_restricted_records.py enable
        ```
        コマンド実行後、2.の手順へ移る。
1. レコードが期待通り登録されたかを確認する。
    1. [4.](#4-スクリプトの実行有効)の1.のe.で出力された結果の最終行に出力される`Table with some records correct`と`Table with no records correct`にテーブル名が出力されていないか確認する。
        1. 1つでもテーブル名が出力されていた場合、ツールの出力結果と2.1.で表示されたテーブルの追加対象レコードの全カラムを取得し、NII担当者へ報告する。  
            追加対象レコードは、`tools/switch_restricted_access/enable/verify_table.json`に書かれているレコード情報を下記表の検索条件をもとに取得する。。  
            verify_table.jsonに記載されている各テーブルの記載行は以下の通り。
            |テーブル名|記載行|検索条件|検索条件記載行|デフォルト|
            |---|---|---|---|---|
            |item_type_name|2~27|id|4,10,16,22|31001~31004|
            |item_type|28~73|id|30,41,52,63|31001~31004|
            |item_type_mapping|74~99|id|76,82,88,94|31001~31004|
            |item_type_property|100~236|id|102,111,120,129,138,147,156,165,174,183,192,201,210,219,228|30001~30015|
            |accounts_role|237~241|name|239|General|
            |index|242~315|id|244,280|1616224532673,1703552310404|
            |workflow_flow_define|316~361|id|319,330,341,352|31001~31004|
            |workflow_flow_action|362~528|id|365,376,387,398|31001~31004|
            |workflow_workflow|529~582|id|532,545,558,571|31001~31004|
            |workflow_userrole|583~629|workflow_id,role_id|586,587,591,592,596,597,601,602,606,607,611,612,616,617,621,622,626,627|31002~31004,(3,4,"Generalのid")|
            |mail_template_genres|630~643|id|632,636,640|1~3|
            |mail_templates|644~750|id|646,653,660,667,674,681,688,695,702,709,716,723,730,737,744|1~15|
            |admin_settings|751~794|name|752|restricted_access|
        1. [切り戻し手順（有効）](#切り戻し手順有効)を実施する。  
1. 設定値、レコードの確認が正常に完了したら、バックアップファイルを削除する。
    1. [3.](#3-設定値とdbのバックアップ有効)1.でコピーしたinstance.cfg（デフォルト値、環境差異あり）を削除する。
    1. 以下のコマンドを実行し、SQLファイルのバックアップおよびコンテナにコピーしたファイルを削除する。
        ```sh
        # コンテナ外で実施する
        docker compose exec postgresql rm -f enable_dump.sql /tmp/get_target_table_hash.sql /tmp/resticted_access.sql
        ```
    1. 以下のコマンドを実行し、切り戻し検証用ファイルを削除する。
        ```sh
        # コンテナ外で実施する
        rm -f dump_hash.txt
        ```
1. 設定値を環境に反映させ、サービスを開始する。

### 実施手順（有効）にて発生するエラー
[実施手順（有効）](#実施手順有効)にて発生しうるエラーは以下の通りである。
|No.|エラー文（例）|原因|
|---|---|---|
|1|grep: <SETTING_FILE>: No such file or directory<br>Error: grep -E "^<WEKOの設定値> \*= \*.\*$" $SETTING_FILE (line 12) exited with 2|[実施手順（有効）の4.](#4-スクリプトの実行有効)1-a.で発生。<br>スクリプトファイル内のSETTING_FILEに記載されたパスが存在しない。|
|2|lstat <指定したSQLファイルのパス>: no such file or directory<br>Error: docker cp <指定したSQLファイルのパス> $(docker compose ps -q postgresql):/tmp/resticted_access.sql (line 75) exited with 1|[実施手順（有効）の4.](#4-スクリプトの実行有効)1-a.およびb.で発生。<br>SQLファイルが指定したパスに存在しない。|
|3|psql: could not connect to server: Connection refused<br>Error: docker-compose exec postgresql psql -U invenio -d invenio -v ON_ERROR_STOP=1 -f /tmp/resticted_access.sql (line 76) exited with 3|[実施手順（有効）の4.](#4-スクリプトの実行有効)1-a.およびb.で発生。<br>SQLファイル内のクエリ実行時にDBに接続できない。|
|4|[TerminalIPythonApp] WARNING \| File not found: '<指定したPythonファイルのパス>'|[実施手順（有効）の4.](#4-スクリプトの実行有効)1.-c.で発生。<br>Pythonファイルが指定したパスに存在しない。|
|5|ERROR in update_restricted_access_property: (psycopg2.OperationalError) could not connect to server: Connection refused<br>ERROR in update_restricted_access_property: Failed to update restricted access property.<br>ERROR in update_restricted_access_property: Traceback (most recent call last):<br><エラー内容><br>Error: docker-compose exec web invenio shell tools/update_restricted_access_property.py $RESTRICTED_ACCESS_PROPERTY enable (line 78) exited with 1|[実施手順（有効）の4.](#4-スクリプトの実行有効)1.-c.で発生。<br>Pythonファイル内の処理でDBに接続できない。|
|6|ERROR in update_restricted_access_property: [Errno 2] No such file or directory: <ファイルパス><br>ERROR in update_restricted_access_property: Failed to update restricted access property.<br>ERROR in update_restricted_access_property: Traceback (most recent call last):<br><エラー内容><br>Error: docker-compose exec web invenio shell tools/update_restricted_access_property.py $RESTRICTED_ACCESS_PROPERTY enable (line 78) exited with 1|[実施手順（有効）の4.](#4-スクリプトの実行有効)1-c.で発生。<br>Pythonファイル内で使用するファイルが見つからない。|
|7|tools/restricted_upadate.sh: line 81: <検証用スクリプトファイルのパス>: No such file or directory<br>Error: <検証用スクリプトファイルのパス> $SETTING_FILE True (line 81) exited with 127|[実施手順（有効）の4.](#4-スクリプトの実行有効)1-d.で発生。<br>検証用スクリプトファイルが指定したパスに存在しない。|
|8|Error: <SETTING_FILE> not found<br>Error: tools/verify_restricted_update.sh $SETTING_FILE True (line 81) exited with 2|[実施手順（有効）の4.](#4-スクリプトの実行有効)1-d.で発生。<br>スクリプトファイル内のSETTING_FILEに記載されたパスが存在しない。|
|9|ERROR in verify_restricted_records: [Errno 2] No such file or directory: <ファイルパス><br>ERROR in verify_restricted_records: Error while verifying '<テーブル名>'<br>ERROR in verify_restricted_records: Traceback (most recent call last):<br><エラー内容>|[実施手順（有効）の4.](#4-スクリプトの実行有効)1-e.で発生。<br>検証用Pythonファイル内で使用するファイルが見つからない。|
|10|ERROR in verify_restricted_records: (psycopg2.OperationalError) could not connect to server: Connection refused<br>ERROR in verify_restricted_records: Error while verifying '<テーブル名>'<br>ERROR in verify_restricted_records: Traceback (most recent call last):<br><エラー内容>|[実施手順（有効）の4.](#4-スクリプトの実行有効)1-e.で発生。<br>検証用Pythonファイル内の処理でDBに接続できない。|
|11|上記以外のエラー|制限公開有効化スクリプトにて想定されていないエラーが発生。|

各エラーに対する対処方法は以下に示す。
#### 1. No.1のエラーの対処方法
1. 以下のコマンドを実行し、設定値の記載内容を確認する。
    ```sh
    # コンテナ外で実施する
    cat tools/restricted_upadate.sh
    ```
1. 1.で開いたファイルの5行目に書かれている`SETTING_FILE`に書かれているパスを確認する。
1. 2.で確認したパスに設定値のファイル（instance.cfg（デフォルト値、環境差異あり））を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
#### 2. No.2のエラーの対処方法
1. エラーログに出力された<指定したSQLファイルのパス>を確認する。
1. 1.で確認したパスに実行するSQLファイル（resticted_access.sql）を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
#### 3. No.3のエラーの対処方法
1. PostgreSQLに関するインフラの設定を確認する。
1. 問題がある場合は修正してから以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
1. 問題がない場合は時間をおいて以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
#### 4. No.4のエラーの対処方法
1. エラーログに出力された<指定したPythonファイルのパス>を確認する。
1. 1.で確認したパスに実行するPythonファイル（update_restricted_access_property.py）を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
#### 5. No.5のエラーの対処方法
1. PostgreSQLに関するインフラの設定を確認する。
1. 問題がある場合は設定を修正してから以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
1. 問題がない場合は時間をおいて以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
#### 6. No.6のエラーの対処方法
1. `tools/switch_restricted_access/enable`配下にプロパティの変更に使用するJSONファイル（schema.json, form.json, forms.json）を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
#### 7. No.7のエラーの対処方法
1. エラーログに出力された<検証用スクリプトファイルのパス>を確認する。
1. 1.で確認したパスに実行する検証用スクリプトファイル（verify_restricted_update.sh）を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
#### 8. No.8のエラーの対処方法
**No.1と同様のエラーとなるため、通常このエラーは発生しない**
1. 以下のコマンドを実行し、設定値の記載内容を確認する。
    ```sh
    # コンテナ外で実施する
    cat tools/restricted_upadate.sh
    ```
1. 1.で開いたファイルの5行目に書かれている`SETTING_FILE`に書かれているパスを確認する。
1. 2.で確認したパスに設定値のファイル（instance.cfg（デフォルト値、環境差異あり））を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
#### 9. No.9のエラーの対処方法
1. `tools/switch_restricted_access/enable`配下にレコード確認用JSONファイル（verify_table.json）を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
#### 10. No.10のエラーの対処方法
1. PostgreSQLに関するインフラの設定を確認する。
1. 問題がある場合は設定を修正してから以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
1. 問題がない場合は時間をおいて以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/restricted_upadate.sh
    ```
#### 11. No.11のエラーの対処方法
1. エラーログを取得したうえで開発業者へ問い合わせを行う。
1. 制限公開機能を無効化する場合、[実施手順（無効）](#実施手順無効)を実施する。
1. 制限公開機能の無効化も失敗した場合は、[切り戻し手順（有効）](#切り戻し手順有効)を実行する。

### 切り戻し手順（有効）
#### 1. 設定値の切り戻し
1. [事前準備（有効）](#事前準備有効)でコピーしたinstance.cfg（デフォルト値、環境差異あり）を`tools/restricted_upadate.sh`に設定したSETTING_FILEのパスに上書きする。

#### 2. DBの切り戻し
1. 以下のコマンドを実行し、バックアップした値を復元する。
    ```sh
    # コンテナ外で実施する
    docker compose exec postgresql psql -d invenio -U invenio -f enable_dump.sql
    ```
1. 以下のコマンドを実行し、復元後の検証用ファイルを作成する。
    ```sh
    # コンテナ外で実施する
    docker cp tools/switch_restricted_access/enable/get_target_table_hash.sql $(docker compose ps -q postgresql):/tmp/get_target_table_hash.sql
    docker compose exec postgresql psql -d invenio -U invenio -f /tmp/get_target_table_hash.sql > restore_hash.txt
    ```
1. 以下のコマンドを実行し、正常に復元できたかを確認する。
    ```sh
    # コンテナ外で実施する
    diff dump_hash.txt restore_hash.txt
    ```
1. 差分があり正常に復元できていない場合、1.よりやり直す。
1. 差分がなく正常に復元できた場合、以下のコマンドを実行してバックアップファイルを削除する。
    ```sh
    # コンテナ外で実施する
    docker compose exec postgresql rm -f enable_dump.sql /tmp/get_target_table_hash.sql /tmp/resticted_access.sql
    ```
1. 以下のコマンドを実行し、切り戻し検証用ファイルを削除する。
    ```sh
    # コンテナ外で実施する
    rm -f dump_hash.txt restore_hash.txt
    ```

## 制限公開機能無効化
### 事前準備（無効）
#### 1. 変更する設定値の修正
**本手順はNII担当者が行う**
1. 設定ファイルに記載される設定値の修正を行う。
    1. 以下のコマンドを実行し、修正予定の設定値修正コマンドが記載されたスクリプトを開く。
        ```sh
        # コンテナ外で実施する
        vi tools/disable_restricted_access.sh
        ```
    1. 1.1.で開いたファイルにて各設定値に登録する値と、下記表にある設定値のデフォルト値とを比較し、その結果に応じて以下の手順を実施する。
        |設定値名|モジュール名|デフォルト値|変更対象行
        |---|---|---|---|
        |WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG|weko-admin|False|12~17|
        |WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS|weko-admin|True|20~25|
        |WEKO_RECORDS_UI_RESTRICTED_API|weko-records-ui|False|28~33|
        |WEKO_ITEMS_UI_PROXY_POSTING|weko-items-ui|False|36~41|
        |WEKO_ITEMTYPES_UI_FORCED_IMPORT_ENABLED|weko-itemtypes-ui|False|44~49|
        |WEKO_INDEX_TREE_SHOW_MODAL|weko-index-tree|False|52~57|
        |WEKO_USERPROFILES_CUSTOMIZE_ENABLED|weko-user-profiles|False|60~65|
        |INVENIO_MAIL_ADDITIONAL_RECIPIENTS_ENABLED|invenio-mail|False|68~73|
        1. 2つの値が一致している場合、設定ファイル（デフォルト名：instance.cfg）より削除するため、上記表にある変更対象行の部分を以下コマンドに置き換える。
            ```sh
            grep -E "^<設定値名> *= *.*$" $SETTING_FILE
            if [ $? -eq 0 ]; then
                sed -i.bak '/<設定値名> *= *.*/d' $SETTING_FILE
            fi
            ```
            例：WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG に対して行うとき、12行目から17行目を以下のコマンドに置き換える。
            ```sh
            grep -E "^WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG *= *.*$" $SETTING_FILE
            if [ $? -eq 0 ]; then
                sed -i.bak '/WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG *= *.*/d' $SETTING_FILE
            fi
            ```
        1. 2つの値が異なっている場合、設定ファイル（デフォルト名：instance.cfg）にて設定を追加するため、上記表にある変更対象行の部分を以下コマンドに置き換える。
            ```sh
            grep -E "^<設定値名> *= *.*$" $SETTING_FILE
            if [ $? -ne 0 ]; then
                echo '<設定値名> = <設定したい値>' >> $SETTING_FILE
            else
                sed -i.bak 's/<設定値名> *= *.*/<設定値名> = <設定したい値>/' $SETTING_FILE
            fi
            ```
            例：WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG を True で設定するとき、12行目から17行目を以下のコマンドに置き換える。
            ```sh
            grep -E "^WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG *= *.*$" $SETTING_FILE
            if [ $? -ne 0 ]; then
                echo 'WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG = True' >> $SETTING_FILE
            else
                sed -i.bak 's/WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG *= *.*/WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG = True/' $SETTING_FILE
            fi
            ```
            例：WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG を False で設定するとき、12行目から17行目を以下のコマンドに置き換える。
            ```sh
            grep -E "^WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG *= *.*$" $SETTING_FILE
            if [ $? -ne 0 ]; then
                echo 'WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG = False' >> $SETTING_FILE
            else
                sed -i.bak 's/WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG *= *.*/WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG = False/' $SETTING_FILE
            fi
            ```
1. SQLファイルに記載されている設定値の修正を行う。
    1. 以下のコマンドを実行し、修正予定の設定値が記載されたSQLファイルを開く。
        ```sh
        # コンテナ外で実施する
        vi scripts/demo/disable_restricted_access.sql
        ```
    1. 2.1.で開いたファイルにて各設定値に登録する値を確認し、下記表の変更対象行に記載されている行にある`false`という文字を設定する値に変更する。
        |設定値名|変更対象行|
        |---|---|
        |password_enable|15|
        |item_application.item_application_enable|18|
        |display_request_form|21|
        |secret_URL_file_download.secret_enable|24|
        |edit_mail_templates_enable|27|
        |preview_workflow_approval_enable|30|
        ```
        例：password_enable を True で設定する場合
            1.3.で開いたファイルの15行目を以下のように修正する。
                            , 'true'::jsonb
        ```

#### 2. スクリプトの設定値修正（無効）
**本手順はNII担当者が行う** 
1. 以下のコマンドを実行し、変更予定の設定値が記載されたスクリプトファイルを開く。
    ```sh
    # コンテナ外で実施する
    vi tools/disable_restricted_access.sh
    ```
1. 1.で開いたファイルの5行目の`SETTING_FILE`を設定ファイル（デフォルト名：instance.cfg、環境差異あり）が置かれたパスに書き換える。
1. 同様に6行目の`RESTRICTED_ACCESS_PROPERTY`を`scripts/demo/resticted_access.sql`の285行目の値に書き換える。

#### 3. 修正ファイルの提供（無効）
**本手順はNII担当者が行う**
1. [変更する設定値の修正](#1-変更する設定値の修正)、[スクリプトの設定値修正（無効）](#2-スクリプトの設定値修正無効)にて修正した以下のファイルを運用担当者に提供する。
    * tools/disable_restricted_access.sh
    * scripts/demo/disable_restricted_access.sql

### 実施手順（無効）
#### 1. 機能無効時に使用するファイルの確認・配置
1. 制限公開機能を無効化する際に以下の表に書かれたファイルを使用している。
    そのため、ファイルが参照先パスへ配置されているか確認を行い、配置されていない場合はそれぞれ指定されているファイルを参照先パスへ配置する。  
    また、[修正ファイルの提供（無効）](#3-修正ファイルの提供無効)にて渡されたファイルはそのファイルを正として参照先パスへ配置する。
    |ファイル名|説明|参照先パス|
    |---|---|---|
    |instance.cfg（デフォルト値、環境差異あり）|WEKOで使用する設定値が記載されたファイル|scripts/instance.cfg|
    |disable_restricted_access.sql|制限公開機能の無効化クエリが書かれたファイル|scripts/demo/disable_restricted_access.sql|
    |update_restricted_access_property.py|制限公開用プロパティのアクセスから「制限公開」を取り除くファイル|tools/update_restricted_access_property.py|
    |schema.json|item_type_propertyテーブルの制限公開用プロパティのschemaカラムに登録する制限公開機能無効時の値が書かれたファイル|tools/switch_restricted_access/disable/schema.json|
    |form.json|item_type_propertyテーブルの制限公開用プロパティのformカラムに登録する制限公開機能無効時の値が書かれたファイル|tools/switch_restricted_access/disable/form.json|
    |forms.json|item_type_propertyテーブルの制限公開用プロパティのformsカラムに登録する制限公開機能無効時の値が書かれたファイル|tools/switch_restricted_access/disable/forms.json|
    |verify_restricted_update.sh|制限公開機能の設定が無効化されたかを確認するファイル|tools/verify_restricted_update.sh|
    |verify_restricted_records.py|制限公開機能で使用するレコードが正しく反映されたかを確認するファイル|tools/verify_restricted_records.py|
    |verify_table.json|制限公開機能無効時のレコード検証に使用するファイル|tools/switch_restricted_access/disable/verify_table.json|
    |get_target_table_hash.sql|制限公開機能無効時の切り戻しの検証に使用するファイル|tools/switch_restricted_access/disable/get_target_table_hash.sql|

#### 2. サービスの停止
1. 本スクリプトはサービス停止した状態で実行されることが前提であるため、WEKOのサービスを停止する。

#### 3. 設定値とDBのバックアップ（無効）
1. instance.cfg（デフォルト値、環境差異あり）をコピーして、現在の設定値のバックアップを取得する。
1. 以下コマンドを実行し、機能無効時に編集するテーブルとそれらに紐づくテーブルのバックアップを取得する。
    ```sh
    # コンテナ外で実施する
    docker compose exec postgresql pg_dump -d invenio -U invenio -t 'item_type' -t 'item_type_property' -t 'admin_settings' -t 'item_type_edit_history' -t 'jsonld_mappings' -t 'rocrate_mapping' -t 'workflow_workflow' -t 'sword_clients' -t 'workflow_activity' -t 'workflow_userrole' -t 'workflow_activity_action' -f disable_dump.sql --clean
    ```
1. 以下コマンドを実行し、切り戻し対応した場合の検証に用いるファイルを作成する。
    ```sh
    # コンテナ外で実施する
    docker cp tools/switch_restricted_access/disable/get_target_table_hash.sql $(docker compose ps -q postgresql):/tmp/get_target_table_hash.sql
    docker compose exec postgresql psql -d invenio -U invenio -f /tmp/get_target_table_hash.sql > dump_hash.txt
    ```

#### 4. スクリプトの実行（無効）
1. 以下コマンドを実行し、設定およびレコードの更新を行う。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
    このスクリプトでは以下の処理を行っている。  
    a. [設定値一覧](#設定値一覧)のすべての設定値を無効（False）にする。  
    b. 制限公開用プロパティのアクセスから「制限公開」を削除する。  
    c. [設定値一覧](#設定値一覧)のすべての設定値が無効（False）となっているか確認する。  
    d. 制限公開用プロパティへの変更が反映されているか確認する。  
    本スクリプトは、エラーが発生した箇所にて処理が停止するよう設計されている。
1. ツール実行時にコンソール上へエラーが出力された場合には、[実施手順（無効）にて発生するエラー](#実施手順無効にて発生するエラー)を確認し、発生したエラーに応じた項番の対処方法を実施する。
    1. 再実行後成功した場合は[5.](#5-機能無効化の確認反映)の手順を実施する。
    1. 再実行しても失敗する場合はエラーログを取得したうえで[切り戻し手順（無効）](#切り戻し手順無効)を実施する。

#### 5. 機能無効化の確認・反映
1.  設定値が期待通り変更されたか確認する。
    1. [4.](#4-スクリプトの実行無効)の1.のc.で出力された結果を1行ずつ確認する。  
        出力結果の見方は[設定値確認ツール説明](#設定値確認ツール説明)に記載されている。
    1. `FAIL`と出力された設定値がある場合、以下コマンドでその設定値の記載箇所を検索する。
        ```sh
        # コンテナ外で実施する
        grep -F '<設定値>' tools/disable_restricted_access.sh
        ```
        1. `echo '<設定値> = False' >> $SETTING_FILE`が出力された場合、適切に設定値の設定ができていないため、instance.cfg（デフォルト値、環境差異あり）に対し、`<設定値> = False`を直接追加する。
        1. 以下が出力された場合、または何も出力されなかった場合は正常であるため、次の設定値の確認を行う。
            * `echo '<設定値> = True' >> $SETTING_FILE`
            * `sed -i.bak '/<設定値> *= *.*/d' $SETTING_FILE`
    1. すべての設定値が確認完了、かつ失敗した設定値の修正が完了したら、以下のコマンドを実行してレコードが正常に登録されたかを確認する。
        ```sh
        # コンテナ外で実施する
        docker compose exec web invenio shell tools/verify_restricted_records.py disable
        ```
        コマンド実行後、2.の手順へ移る。
1. レコードが期待通り登録されたかを確認する。
    1. [4.](#4-スクリプトの実行無効)の1.のd.で出力された結果の最終行に出力される`Table with some records correct`と`Table with no records correct`にテーブル名が出力されていないか確認する。
        1. 1つでもテーブル名が出力されていた場合、ツールの出力結果と2.1.で表示されたテーブルの追加対象レコードの全カラムを取得し、NII担当者へ報告する。  
            追加対象レコードは、`tools/switch_restricted_access/disable/verify_table.json`に書かれているレコード情報を下記表の検索条件をもとに取得する。  
            verify_table.jsonに記載されている各テーブルの記載行は以下の通り。
            |テーブル名|記載行|検索条件|検索条件記載行|デフォルト|
            |---|---|---|---|---|
            |item_type|2~14|id|4|31004|
            |item_type_property|15~25|id|17|30015|
            |admin_settings|26~40|name|27|restricted_access|
        1. [切り戻し手順（無効）](#切り戻し手順無効)を実施する。
1. 設定値、レコードの確認が正常に完了したら、バックアップファイルを削除する。
    1. [3.](#3-設定値とdbのバックアップ無効)1.でコピーしたinstance.cfg（デフォルト値、環境差異あり）を削除する。
    1. 以下のコマンドを実行し、SQLファイルのバックアップを削除する。
        ```sh
        # コンテナ外で実施する
        docker compose exec postgresql rm -f disable_dump.sql /tmp/get_target_table_hash.sql /tmp/disable_restricted_access.sql
        ```
    1. 以下のコマンドを実行し、切り戻し検証用ファイルを削除する。
        ```sh
        # コンテナ外で実施する
        rm -f dump_hash.txt
        ```
1. 設定値を環境に反映させ、サービスを開始する。

### 実施手順（無効）にて発生するエラー
[実施手順（無効）](#実施手順無効)にて発生しうるエラーは以下の通りである。
|No.|エラー文（例）|原因|
|---|---|---|
|1|grep: <SETTING_FILE>: No such file or directory<br>Error: grep -E "^<WEKOの設定値> \*= \*.\*$" $SETTING_FILE (line 12) exited with 2|[実施手順（無効）の4.](#4-スクリプトの実行無効)1-a.で発生。<br>スクリプトファイル内のSETTING_FILEに記載されたパスが存在しない。|
|2|lstat <指定したSQLファイルのパス>: no such file or directory<br>Error: docker cp <指定したSQLファイルのパス> $(docker compose ps -q postgresql):/tmp/disable_restricted_access.sql (line 75) exited with 1|[実施手順（無効）の4.](#4-スクリプトの実行無効)1-a.で発生。<br>SQLファイルが指定したパスに存在しない。|
|3|psql: could not connect to server: Connection refused<br>Error: docker-compose exec postgresql psql -U invenio -d invenio -v ON_ERROR_STOP=1 -f /tmp/disable_restricted_access.sql (line 76) exited with 3|[実施手順（無効）の4.](#4-スクリプトの実行無効)1-a.で発生。<br>SQLファイル内のクエリ実行時にDBに接続できない。|
|4|[TerminalIPythonApp] WARNING \| File not found: '<指定したPythonファイルのパス>'|[実施手順（無効）の4.](#4-スクリプトの実行無効)1-b.で発生。<br>Pythonファイルが指定したパスに存在しない。|
|5|ERROR in update_restricted_access_property: (psycopg2.OperationalError) could not connect to server: Connection refused<br>ERROR in update_restricted_access_property: Failed to update restricted access property.<br>ERROR in update_restricted_access_property: Traceback (most recent call last):<br><エラー内容><br>Error: docker-compose exec web invenio shell tools/update_restricted_access_property.py $RESTRICTED_ACCESS_PROPERTY disable (line 78) exited with 1|[実施手順（無効）の4.](#4-スクリプトの実行無効)1-b.で発生。<br>Pythonファイル内の処理でDBに接続できない。|
|6|ERROR in update_restricted_access_property: [Errno 2] No such file or directory: <ファイルパス><br>ERROR in update_restricted_access_property: Failed to update restricted access property.<br>ERROR in update_restricted_access_property: Traceback (most recent call last):<br><エラー内容><br>Error: docker-compose exec web invenio shell tools/update_restricted_access_property.py $RESTRICTED_ACCESS_PROPERTY disable (line 78) exited with 1|[実施手順（無効）の4.](#4-スクリプトの実行無効)1-b.で発生。<br>Pythonファイル内で使用するファイルが見つからない。|
|7|tools/disable_restricted_access.sh: line 81: <検証用スクリプトファイルのパス>: No such file or directory<br>Error: <検証用スクリプトファイルのパス> $SETTING_FILE True (line 81) exited with 127|[実施手順（無効）の4.](#4-スクリプトの実行無効)1-c.で発生。<br>検証用スクリプトファイルが指定したパスに存在しない。|
|8|Error: <SETTING_FILE> not found<br>Error: tools/verify_restricted_update.sh $SETTING_FILE True (line 81) exited with 2|[実施手順（無効）の4.](#4-スクリプトの実行無効)1-c.で発生。<br>スクリプトファイル内のSETTING_FILEに記載されたパスが存在しない。|
|9|ERROR in verify_restricted_records: [Errno 2] No such file or directory: <ファイルパス><br>ERROR in verify_restricted_records: Error while verifying '<テーブル名>'<br>ERROR in verify_restricted_records: Traceback (most recent call last):<br><エラー内容>|[実施手順（無効）の4.](#4-スクリプトの実行無効)1-d.で発生。<br>検証用Pythonファイル内で使用するファイルが見つからない。|
|10|ERROR in verify_restricted_records: (psycopg2.OperationalError) could not connect to server: Connection refused<br>ERROR in verify_restricted_records: Error while verifying '<テーブル名>'<br>ERROR in verify_restricted_records: Traceback (most recent call last):<br><エラー内容>|[実施手順（無効）の4.](#4-スクリプトの実行無効)1-d.で発生。<br>検証用Pythonファイル内の処理でDBに接続できない。|
|11|上記以外のエラー|制限公開無効化スクリプトにて想定されていないエラーが発生。|

各エラーに対する対処方法は以下に示す。
#### 1. No.1のエラー対処方法
1. 以下のコマンドを実行し、設定値の記載内容を確認する。
    ```sh
    # コンテナ外で実施する
    cat tools/disable_restricted_access.sh
    ```
1. 1.で開いたファイルの5行目に書かれている`SETTING_FILE`に書かれているパスを確認する。
1. 2.で確認したパスに設定値のファイル（instance.cfg（デフォルト値、環境差異あり））を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
#### 2. No.2のエラーの対処方法
1. エラーログに出力された<指定したSQLファイルのパス>を確認する。
1. 1.で確認したパスに実行するSQLファイル（disable_restricted_access.sql）を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
#### 3. No.3のエラーの対処方法
1. PostgreSQLに関するインフラの設定を確認する。
1. 問題がある場合は修正してから以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
1. 問題がない場合は時間をおいて以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
#### 4. No.4のエラーの対処方法
1. エラーログに出力された<指定したPythonファイルのパス>を確認する。
1. 1.で確認したパスに実行するPythonファイル（update_restricted_access_property.py）を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
#### 5. No.5のエラーの対処方法
1. PostgreSQLに関するインフラの設定を確認する。
1. 問題がある場合は設定を修正してから以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
1. 問題がない場合は時間をおいて以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
#### 6. No.6のエラーの対処方法
1. `tools/switch_restricted_access/disable`配下にプロパティの変更に使用するJSONファイル（schema.json, form.json, forms.json）を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
#### 7. No.7のエラーの対処方法
1. エラーログに出力された<検証用スクリプトファイルのパス>を確認する。
1. 1.で確認したパスに実行する検証用スクリプトファイル（verify_restricted_update.sh）を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
#### 8. No.8のエラーの対処方法
**No.1と同様のエラーとなるため、通常このエラーは発生しない**
1. 以下のコマンドを実行し、設定値の記載内容を確認する。
    ```sh
    # コンテナ外で実施する
    cat tools/disable_restricted_access.sh
    ```
1. 1.で開いたファイルの5行目に書かれている`SETTING_FILE`に書かれているパスを確認する。
1. 2.で確認したパスに設定値のファイル（instance.cfg（デフォルト値、環境差異あり））を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
#### 9. No.9のエラーの対処方法
1. `tools/switch_restricted_access/disable`配下にレコード確認用JSONファイル（verify_table.json）を配置する。
1. 以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
#### 10. No.10のエラーの対処方法
1. PostgreSQLに関するインフラの設定を確認する。
1. 問題がある場合は設定を修正してから以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
1. 問題がない場合は時間をおいて以下のコマンドを再実行し、切り替え処理をやり直す。
    ```sh
    # コンテナ外で実施する
    source tools/disable_restricted_access.sh
    ```
#### 11. No.11のエラーの対処方法
1. エラーログを取得したうえで開発業者へ問い合わせを行う。
1. 制限公開機能を有効化する場合、[実施手順（有効）](#実施手順有効)を実施する。
1. 制限公開機能の有効化も失敗した場合は、[切り戻し手順（無効）](#切り戻し手順無効)を実行する。

### 切り戻し手順（無効）
#### 1. 設定値の切り戻し
1. [事前準備（無効）](#事前準備無効)でコピーしたinstance.cfg（デフォルト値、環境差異あり）を`tools/disable_restricted_access.sh`に設定したSETTING_FILEのパスに上書きする。

### 2. DBの切り戻し
1. 以下のコマンドを実行し、バックアップした値を復元する。
    ```sh
    # コンテナ外で実施する
    docker compose exec postgresql psql -d invenio -U invenio -f disable_dump.sql
    ```
1. 以下のコマンドを実行し、復元後の検証用ファイルを作成する。
    ```sh
    # コンテナ外で実施する
    docker cp tools/switch_restricted_access/disable/get_target_table_hash.sql $(docker compose ps -q postgresql):/tmp/get_target_table_hash.sql
    docker compose exec postgresql psql -d invenio -U invenio -f /tmp/get_target_table_hash.sql > restore_hash.txt
    ```
1. 以下のコマンドを実行し、正常に復元できたかを確認する。
    ```sh
    # コンテナ外で実施する
    diff dump_hash.txt restore_hash.txt
    ```
1. 差分があり正常に復元できていない場合、1.よりやり直す。
1. 差分がなく正常に復元できた場合、以下のコマンドを実行してバックアップファイルを削除する。
    ```sh
    # コンテナ外で実施する
    docker compose exec postgresql rm -f disable_dump.sql /tmp/get_target_table_hash.sql /tmp/disable_restricted_access.sql
    ```
1. 以下のコマンドを実行し、切り戻し検証用ファイルを削除する。
    ```sh
    # コンテナ外で実施する
    rm -f dump_hash.txt restore_hash.txt
    ```

## 補足資料
### 設定値一覧
<table>
    <thead>
        <tr>
            <th>種別</th>
            <th>名前</th>
            <th>対象機能</th>
            <th>True</th>
            <th>False</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="4">config</td>
            <td rowspan="4">WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG</td>
            <td>管理画面「制限公開」における制限公開機能の表示切替</td>
            <td>全制限公開機能を表示</td>
            <td>シークレットURLダウンロード機能のみ表示</td>
        </tr>
        <tr>
            <td>制限公開アイテムのアクセス方法切替</td>
            <td>「制限公開」として機能</td>
            <td>「非公開」として機能</td>
        </tr>
        <tr>
            <td>利用申請後のアクセス権限付与機能の有効切替</td>
            <td>利用申請したユーザへアクセス権限を付与する</td>
            <td>利用申請したユーザへアクセス権限を付与しない</td>
        </tr>
        <tr>
            <td>利用申請系ワークフローの編集権限切替</td>
            <td>システム管理者のみアクセス可能</td>
            <td>システム管理者以外もアクセス可能</td>
        </tr>
        <tr>
            <td>config</td>
            <td>WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS</td>
            <td>ワークフローの利用申請フラグの表示切替</td>
            <td>利用申請フラグチェックボックスの表示（システム管理者のみ）</td>
            <td>利用申請フラグチェックボックスの非表示</td>
        </tr>
        <tr>
            <td>config</td>
            <td>WEKO_RECORDS_UI_RESTRICTED_API</td>
            <td>利用規約取得API、利用申請開始API、利用申請APIの有効切替</td>
            <td>API実行可能</td>
            <td>API実行不可能</td>
        </tr>
        <tr>
            <td rowspan="2">config</td>
            <td rowspan="2">WEKO_ITEMS_UI_PROXY_POSTING</td>
            <td rowspan="2">代理投稿機能の複数選択機能の有効切替</td>
            <td>複数選択可能</td>
            <td>複数選択不可</td>
        </tr>
        <tr>
            <td>Owner, Contributor に設定したユーザへの編集権限付与</td>
            <td>Owner に設定したユーザにのみ編集権限付与</td>
        </tr>
        <tr>
            <td>config</td>
            <td>WEKO_ITEMTYPES_UI_FORCED_IMPORT_ENABLED</td>
            <td>アイテムタイプのプロパティの強制インポート機能の有効切替</td>
            <td>未登録プロパティを含むアイテムタイプのインポート可</td>
            <td>未登録プロパティを含むアイテムタイプのインポート不可</td>
        </tr>
        <tr>
            <td>config</td>
            <td>WEKO_INDEX_TREE_SHOW_MODAL</td>
            <td>インデックス公開ロック機能の有効切替</td>
            <td>インデックスの公開・ハーベスト公開時にダイアログを表示する</td>
            <td>インデックスの公開・ハーベスト公開時にダイアログを表示しない</td>
        </tr>
        <tr>
            <td rowspan="2">config</td>
            <td rowspan="2">WEKO_USERPROFILES_CUSTOMIZE_ENABLED</td>
            <td rowspan="2">プロフィールのカスタム属性の有効切替</td>
            <td>プロフィールのカスタム属性設定画面表示</td>
            <td>プロフィールのカスタム属性設定画面非表示</td>
        </tr>
        <tr>
            <td>プロフィール画面へのカスタム属性表示</td>
            <td>プロフィール画面へのカスタム属性非表示</td>
        </tr>
        <tr>
            <td>config</td>
            <td>INVENIO_MAIL_ADDITIONAL_RECIPIENTS_ENABLED</td>
            <td>送信先、CC、BCCの有効切替</td>
            <td>送信先、CC、BCCの表示・設定が有効</td>
            <td>送信先、CC、BCCの表示・設定が無効</td>
        </tr>
        <tr>
            <td>admin_settings</td>
            <td>password_enable</td>
            <td>非ログインユーザーのDLにおけるパスワードチェック機能の有効切替</td>
            <td>パスワードチェック機能が有効</td>
            <td>パスワードチェック機能が無効</td>
        </tr>
        <tr>
            <td>admin_settings</td>
            <td>item_application.item_application_enable</td>
            <td>コンテンツ未登録アイテムの利用申請機能の有効切替</td>
            <td>コンテンツ未登録アイテムの利用申請機能が有効</td>
            <td>コンテンツ未登録アイテムの利用申請機能が無効</td>
        </tr>
        <tr>
            <td>admin_settings</td>
            <td>display_request_form</td>
            <td>リクエストフォーム機能の有効切替</td>
            <td>リクエストフォーム機能が有効</td>
            <td>リクエストフォーム機能が無効</td>
        </tr>
        <tr>
            <td>admin_settings</td>
            <td>secret_URL_file_download.secret_enable</td>
            <td>シークレットURLダウンロード機能の有効切替</td>
            <td>シークレットURLダウンロード機能が有効</td>
            <td>シークレットURLダウンロード機能が無効</td>
        </tr>
        <tr>
            <td>admin_settings</td>
            <td>edit_mail_templates_enable</td>
            <td>メールテンプレート編集機能の有効切替</td>
            <td>メールテンプレート編集機能が有効</td>
            <td>メールテンプレート編集機能が無効</td>
        </tr>
        <tr>
            <td>admin_settings</td>
            <td>preview_workflow_approval_enable</td>
            <td>承認アクションにおけるファイルプレビュー機能の有効切替</td>
            <td>承認アクションにおけるファイルプレビュー機能が有効</td>
            <td>承認アクションにおけるファイルプレビュー機能が無効</td>
        </tr>
    </tbody>
</table>

### SQL実行一覧
#### 機能有効時
|対象テーブル|操作|重複対象|重複時|内容|対象テーブル内の関連キー|
|---|---|---|---|---|---|
|item_type_name|登録|id|登録しない|制限公開で使用するアイテムタイプ名の登録|-|
|item_type|登録|id|登録しない|制限公開で使用するアイテムタイプの登録|name_id(item_type_name.id)
|item_type_mapping|登録|id|登録しない|制限公開で使用するアイテムタイプマッピングの登録|item_type_id(item_type.id)
|item_type_property|登録|id|登録しない|制限公開で使用するアイテムタイププロパティの登録|-|
|accounts_role|登録|name|登録しない|General ロールの登録|-|
|index|登録|id|登録しない|利用申請・利用報告で使用するインデックスの登録|-|
|workflow_flow_define|登録|id|登録しない|利用申請・利用報告で使用するフローの登録|-|
|workflow_flow_action|登録|id|登録しない|利用申請・利用報告で使用するフローアクションの登録|flow_id(workflow_flow_define.flow_id)
|workflow_workflow|登録|id|登録しない|利用申請・利用報告で使用するワークフローの登録|itemtype_id(item_type.id)<br>flow_id(workflow_flow_define.id)<br>delete_flow_id(workflow_flow_define.id)
|workflow_userrole|登録|workflow_id, role_id|登録しない|利用申請・利用報告で使用するワークフローの権限設定の登録|workflow_id(workflow_workflow.id)<br>role_id(accounts_role.id)
|mail_template_genres|登録|id|登録しない|メールテンプレートジャンルの登録|-|
|mail_templates|登録|id|id=11のみ更新する|メールテンプレートの登録（id=11(secret_url)のテンプレートのみ重複時更新）|genre_id(mail_template_genres.id)
|admin_settings|登録|name|更新する|制限公開用設定の登録（重複時全機能有効にする）|-|
|admin_settings|更新|-|-|シークレットURL、コンテンツダウンロードの最大数の設定|-|

※対象テーブル内の関連キーは、かっこ内の`テーブル.カラム`を記載行のテーブルのかっこ前に書かれているカラムで保持していることを指す。

#### 機能無効時
|対象テーブル|操作|重複対象|重複時|内容|
|---|---|---|---|---|
|admin_settings|更新|-|-|制限公開機能をすべて無効にする|

### 設定値確認ツール説明
#### 成功時の出力
```
Checking scripts/instance.cfg
OK: WEKO_ITEMTYPES_UI_FORCED_IMPORT_ENABLED = True in scripts/instance.cfg --- 1
OK: WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG = True in scripts/instance.cfg
OK: WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS = True in scripts/instance.cfg
OK: WEKO_INDEX_TREE_SHOW_MODAL = True in scripts/instance.cfg
OK: WEKO_USERPROFILES_CUSTOMIZE_ENABLED = True in scripts/instance.cfg
OK: INVENIO_MAIL_ADDITIONAL_RECIPIENTS_ENABLED = True in scripts/instance.cfg
OK: WEKO_RECORDS_UI_RESTRICTED_API = True in scripts/instance.cfg
OK: WEKO_ITEMS_UI_PROXY_POSTING = True in scripts/instance.cfg
All checks passed --- 2
```
|No.|出力内容|概要|
|---|---|---|
|1|OK: <設定値> = True/False in <設定値のファイルパス>|<設定値のファイルパス>に書かれている<設定値>が期待通り有効/無効設定となっている。<br>有効時はTrueが表示され、無効時はFalseが表示される。|
|2|All checks passed|すべての設定値が正常に有効/無効化された。|

#### 失敗時の出力
```
Checking scripts/instance.cfg
FAIL: WEKO_ITEMTYPES_UI_FORCED_IMPORT_ENABLED != True in scripts/instance.cfg --- 1
OK: WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG = True in scripts/instance.cfg
OK: WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS = True in scripts/instance.cfg
OK: WEKO_INDEX_TREE_SHOW_MODAL = True in scripts/instance.cfg
OK: WEKO_USERPROFILES_CUSTOMIZE_ENABLED = True in scripts/instance.cfg
OK: INVENIO_MAIL_ADDITIONAL_RECIPIENTS_ENABLED = True in scripts/instance.cfg
OK: WEKO_RECORDS_UI_RESTRICTED_API = True in scripts/instance.cfg
OK: WEKO_ITEMS_UI_PROXY_POSTING = True in scripts/instance.cfg
Verification failed --- 2
```
|No.|出力内容|概要|
|---|---|---|
|1|FAIL: <設定値> != True/False in <設定値のファイルパス>|<設定値のファイルパス>に書かれている<設定値>が期待通りでない有効/無効設定となっている。<br>有効時はTrueが表示され、無効時はFalseが表示される。|
|2|Verification failed|一部設定値が正常に有効/無効化されていない。|

### レコード確認ツール説明
`tools/verify_restricted_records.py`は期待結果であるverify_table.jsonとそのファイルに記載されたテーブルのレコードとを比較し、その差分をカラム単位で出力するものである。   
期待結果であるverify_table.jsonは制限公開機能有効時と無効時とで別のファイルを参照している。  
有効時：tools/switch_restricted_access/**enable**/verify_table.json  
無効時：tools/switch_restricted_access/**disable**/verify_table.json  
上記ファイル内にて記載されている`xxx`はaccounts_roleテーブルに登録される`General`のidでツール内で変換する。  
本ツールでは、以下のルールに従って出力が行われる。
```
verify_table.jsonに記載されたテーブルに対し、1つずつ以下の情報が出力される。
    比較開始 ---1
    verify_table.jsonに記載されたテーブル内にあるレコード情報に対し、以下のいずれかが出力される。
        全カラム一致 ---2
        カラム不一致（不一致数分出力） ---3
        レコード未存在 ---4
全テーブル比較終了 ---5
全レコード完全一致テーブル一覧 ---6
一部レコード一致テーブル一覧 ---7
全レコード不一致テーブル一覧 ---8
```
上記文言はそれぞれ以下の形で出力される。
|No.|出力内容|概要|
|---|---|---|
|1|Verifying <テーブル名> records…|verify_table.json に書かれているテーブルのうち、<テーブル名>のチェックを開始するINFO文。|
|2|Record with id <レコードのID> verified successfully.|1.で出力されたテーブルにあるidが<レコードのID>であるレコードで、verify_table.jsonに書かれている期待結果とDBに登録されている実行結果がすべてのカラムで一致していることを示すINFO文。|
|3|Mismatch for id <レコードのID> on field '<カラム名>': expected: <期待結果>, got <実行結果>|1.で出力されたテーブルにあるidが<レコードのID>であるレコードで、verify_table.jsonに書かれている期待結果とDBに登録されている実行結果とで、<カラム名>の値が一致していないことを示すWARNING文。|
|4|Record with id <レコードのID> not found.|1.で出力されたテーブルにidが<レコードのID>のレコードが存在しないことを示すWARNING文。|
|5|Verification completed.|すべてのテーブルの比較が完了したことを示すINFO文。|
|6|Tables with all records correct: [<テーブル名>…]|すべてのレコードが期待結果通りとなっているテーブルの一覧。|
|7|Tables with some records correct: [<テーブル名>…]|一部のレコードが期待通りとなっているテーブルの一覧。|
|8|Tables with no records correct: [<テーブル名>…]|すべてのレコードが期待結果通りとなっていないテーブルの一覧。|

以下パターンに応じた例を記載する。
* すべてのテーブルが期待通りとなっている場合
    ```
    Verifying item_type_name records...
    Record with id 31001 verified successfully.
    Record with id 31002 verified successfully.
    Record with id 31003 verified successfully.
    Record with id 31004 verified successfully.
    Verifying item_type records...
    Record with id 31001 verified successfully.
    Record with id 31002 verified successfully.
    Record with id 31003 verified successfully.
    Record with id 31004 verified successfully.
    Verifying index records...
    Record with id 1703552310404 verified successfully.
    Record with id 1616224532673 verified successfully.
    Verification completed.
    Tables with all records correct: ['item_type_name', 'item_type', 'index'], 
    Tables with some records correct: [], 
    Tables with no records correct: [].
    ```
    * 各レコードの確認結果がすべて`Record with id <レコードのID> verified successfully.`となっている。  
        →各テーブルの確認対象のレコードがすべて期待結果と一致している。  
        * `Tables with all records correct`にテーブル名が記載される。
* 期待通りのテーブルと期待通りでないテーブルが混在している場合
    ```
    Verifying item_type_name records...
    Record with id 31001 verified successfully.
    Record with id 31002 verified successfully.
    Record with id 31003 verified successfully.
    Mismatch for id 31004 on field 'has_site_license': expected: false, got true
    Mismatch for id 31004 on field 'is_active': expected: true, got false
    Verifying item_type records...
    Record with id 31001 verified successfully.
    Record with id 31002 verified successfully.
    Record with id 31003 verified successfully.
    Record with id 31004 verified successfully.
    Verifying index records...
    Record with id 1703552310404 not found.
    Record with id 1616224532673 not found.
    Verification completed.
    Tables with all records correct: ['item_type'], 
    Tables with some records correct: ['item_type_name'], 
    Tables with no records correct: ['index'].
    ```
    * レコードの確認結果に`Mismatch for id 31004 on field 'has_site_license': expected: false, got true`が出力される。  
        →item_type_nameテーブルのidが31004のレコードにおいて、has_site_licenseの期待結果はfalseであったが、実行結果はtrueとなっており、期待通りに登録できていない。
        * item_type_nameテーブルの他のレコードは`Record with id <レコードのID> verified successfully.`が出力されているため、`Tables with some records correct`に記載される。  
    * レコードの確認結果に`Record with id 1703552310404 not found.`が出力される。  
        →indexテーブルのidが1703552310404のレコードが登録されていない。
        * indexテーブルの他のレコードに`Record with id <レコードのID> verified successfully.`が出力されていないため、`Tables with no records correct`に記載される。
* すべてのテーブルが期待通りとなっていない場合
    ```
    Verifying item_type_name records...
    Record with id 31001 verified successfully.
    Record with id 31002 verified successfully.
    Record with id 31003 verified successfully.
    Mismatch for id 31004 on field 'has_site_license': expected: false, got true
    Mismatch for id 31004 on field 'is_active': expected: true, got false
    Verifying item_type records...
    Mismatch for id 31001 on field 'harvesting_type': expected: false, got true
    Mismatch for id 31002 on field 'harvesting_type': expected: false, got true
    Mismatch for id 31003 on field 'harvesting_type': expected: false, got true
    Mismatch for id 31004 on field 'harvesting_type': expected: false, got true
    Verifying index records...
    Record with id 1703552310404 not found.
    Record with id 1616224532673 not found.
    Verification completed.
    Tables with all records correct: [], 
    Tables with some records correct: ['item_type_name'], 
    Tables with no records correct: ['item_type', 'index'].
    ```
    * レコードの確認結果に`Mismatch for id 31004 on field 'has_site_license': expected: false, got true`が出力される。  
        →item_type_nameテーブルのidが31004のレコードにおいて、has_site_licenseの期待結果はfalseであったが、実行結果はtrueとなっており、期待通りに登録できていない。
        * item_type_nameテーブルの他のレコードは`Record with id <レコードのID> verified successfully.`が出力されているため、`Tables with some records correct`に記載される。  
    * レコードの確認結果に`Mismatch for id 31001 on field 'harvesting_type': expected: false, got true`が出力される。  
        →item_typeテーブルのidが31001のレコードにおいて、harvesting_typeの期待結果はfalseであったが、実行結果はtrueとなっており、期待通りに登録できていない。
        * item_typeテーブルの他のレコードに`Record with id <レコードのID> verified successfully.`が出力されていないため、`Tables with no records correct`に記載される。
    * レコードの確認結果に`Record with id 1703552310404 not found.`が出力される。  
        →indexテーブルのidが1703552310404のレコードが登録されていない。
        * indexテーブルの他のレコードに`Record with id <レコードのID> verified successfully.`が出力されていないため、`Tables with no records correct`に記載される。
