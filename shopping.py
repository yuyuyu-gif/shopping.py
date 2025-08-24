# 必要なライブラリをインポート
import streamlit as st  # Webアプリ作成用
import random  # ランダム選択用

# ページ設定
st.set_page_config(
    page_title="オーストラリア食材買い物メモ",  # ブラウザのタブに表示されるタイトル
    page_icon="🦘",                            # ブラウザのタブに表示されるアイコン
    layout="wide"                              # レイアウトをワイドに設定
)

# タイトルと説明
st.title("🦘 オーストラリア食材買い物メモ")  # メインタイトル
st.markdown("---")  # 区切り線
st.markdown("### オーストラリアの美味しい食材や商品をリストアップしよう！")  # サブタイトル

# ===== オーストラリアの食材サンプル（リスト） =====
# リスト（list）：複数のデータを管理するデータ構造
# 角括弧[]で囲んで、カンマ区切りで要素を並べる
australian_foods = [
    "🍯 マヌカハニー",
    "🥩 ビーフジャーキー",
    "🍪 ティムタム",
    "🧀 ビタービター",
    "🍷 ワイン",
    "🦘 カンガルーミート",
    "🐊 クロコダイルミート",
    "🥜 マカダミアナッツ",
    "🍫 チョコレート",
    "☕ コーヒー豆",
    "🥛 ミルク",
    "🧈 バター",
    "🥖 食パン",
    "🍺 xxxx Gold (ビール）"
]

# ===== セッション状態の初期化 =====
# session_state：ページを更新してもデータを保持するStreamlitの機能
# 買い物リストを保存するための空のリストを作成
if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = []  # 空のリストで初期化

# 削除確認メッセージを表示するためのフラグ
if 'clear_clicked' not in st.session_state:
    st.session_state.clear_clicked = False  # Falseで初期化

# ===== 基本的な使用例 =====
# 辞書の場合
my_dict = {"name": "John", "age": 25}

# in演算子（存在するかチェック）
if "name" in my_dict:
    print(f"名前: {my_dict['name']}")  # 存在する場合の処理

# not in演算子（存在しないかチェック）
if "city" not in my_dict:
    my_dict["city"] = "Tokyo"  # 存在しない場合の処理

# リストの場合
my_list = ["apple", "banana", "orange"]

# in演算子（存在するかチェック）
if "apple" in my_list:
    print("りんごが見つかりました！")

# not in演算子（存在しないかチェック）
if "grape" not in my_list:
    my_list.append("grape")  # 存在しない場合の処理


# ===== サイドバーにオーストラリア情報 =====
with st.sidebar:  # サイドバーを作成
    st.header("🇦🇺 オーストラリア情報")  # サイドバーのヘッダー
    st.markdown("""
    **オーストラリアのおすすめ料理:**
    - 🥩 ビーフステーキ
    - 🦘 カンガルーグリル
    - 🦞 ロブスター
    - 🦪 オイスター
    - 🍖 ラムチョップ
    """)

    # ===== ランダムなオーストラリア情報を表示 =====
    # リスト：複数の文字列を格納
    australia_facts = [
        "オーストラリアには世界最大のサンゴ礁、グレートバリアリーフがあります！",
        "オーストラリアの国土は日本の約20倍の大きさです！",
        "オーストラリアには世界で最も毒の強いヘビ🐍がいます！",
        "オーストラリアの羊の数は人口の約3倍です！",
        "オーストラリアには世界で最も古い砂漠があります！",
        "「アバター」という映画のオープニングはケアンズにある世界最古の熱帯雨林です！",
        "ブリスベンの川にはサメが住んでいます🦈",
        "ケアンズの川やビーチには時々ワニがいます🐊"
    ]

    # ボタンが押された時の処理
    if st.button("🎲 オーストラリア豆知識"):
        # random.choice()関数：リストからランダムに1つの要素を選択
        st.info(random.choice(australia_facts))

# ===== メインコンテンツ =====
st.header("📝 買い物リスト管理")  # メインのヘッダー

# 新しいアイテムの入力
# st.text_input()：テキスト入力欄を作成
new_item = st.text_input("新しいアイテムを入力してください:", placeholder="例: マヌカハニー")

# ===== 追加ボタンの処理 =====
# st.button()：ボタンを作成
if st.button("➕ リストに追加"):
    # strip()メソッド：文字列の前後の空白を削除
    if new_item.strip():  # 空でない場合のみ追加
        # append()メソッド：リストの末尾に要素を追加
        # これが今回の学習ポイントの1つ！
        st.session_state.shopping_list.append(new_item.strip())
        st.success(f"✅ '{new_item}' をリストに追加しました！")
    else:
        st.warning("⚠️ アイテム名を入力してください。")

# ===== サンプルアイテムを追加するボタン =====
if st.button("🎯 サンプル食材を追加"):
    # random.choice()関数：リストからランダムに1つの要素を選択
    sample_item = random.choice(australian_foods)
    # append()メソッド：リストに要素を追加
    st.session_state.shopping_list.append(sample_item)
    st.success(f"✅ '{sample_item}' をリストに追加しました！")


# ===== クリアメッセージの表示 =====
# セッション状態を使ってメッセージを管理
# クリアボタンが押されたらメッセージを表示
if st.session_state.clear_clicked:
    st.success("✅ リストをクリアしました！")
    # メッセージを表示したらフラグをリセット（ボタンが押されていない状態にする）
    st.session_state.clear_clicked = False  # フラグをリセット

# ===== 買い物リストの表示 =====
st.markdown("---")  # 区切り線
# 2つのカラムを作成（3:1の比率）
col1, col2 = st.columns([3, 1])
with col1:
    st.header("🛒 現在の買い物リスト")  # リストのヘッダー
with col2:
    # len()関数：リストの要素数を取得
    st.metric("アイテム数", len(st.session_state.shopping_list))

# ===== リストが空の場合のメッセージ =====
if len(st.session_state.shopping_list) == 0:
    st.info("📝 まだアイテムがありません。上記の入力欄からアイテムを追加してみましょう！")
else:
    # ===== for文を使ってリストの中身を順番に表示 =====
    # enumerate()関数：リストの要素とインデックスを同時に取得
    # enumerate(st.session_state.shopping_list, 1)：インデックスを1から開始
    # これが今回の学習ポイントの1つ！
    for index, item in enumerate(st.session_state.shopping_list, 1):
        # 3つのカラムを作成（0.1:0.6:0.3の比率）
        col1, col2, col3 = st.columns([0.1, 0.6, 0.3])

        with col1:
            st.write(f"**{index}.**")  # 番号を表示

        with col2:
            st.write(item)  # アイテム名を表示

        with col3:
            # st.popover()：ポップオーバー（小さなポップアップ）を作成
            with st.popover("🗑️ 削除", help=f"「{item}」を削除"):
                st.write(f"「{item}」を削除しますか？")
                if st.button("はい", key=f"confirm_yes_{index}"):
                    # pop()メソッド：指定したインデックスの要素を削除
                    st.session_state.shopping_list.pop(index - 1)
                    st.rerun()  # ページを再読み込み


# ===== リストの操作ボタン =====
if len(st.session_state.shopping_list) > 0:
    st.markdown("---")  # 区切り線
    # 2つのカラムを作成
    col1, col2 = st.columns(2)

    with col1:
        # リストをクリアするボタン
        if st.button("🗑️ リストをクリア"):
            # clear()メソッド：リストの全要素を削除
            st.session_state.shopping_list.clear()
            st.session_state.clear_clicked = True  # メッセージ表示フラグを設定
            st.rerun()  # ページを再読み込み

    with col2:
        # リストをコピーするボタン
        if st.button("📋 リストをコピー"):
            # リストの要素を文字列に変換
            # enumerate()関数：インデックスと要素を同時に取得
            # join()メソッド：リストの要素を改行で結合
            list_text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(st.session_state.shopping_list)])
            st.code(list_text)  # コードブロックとして表示
            st.info("上記のリストをコピーして使用してください！")

