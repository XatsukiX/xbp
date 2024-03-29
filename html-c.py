html = """<!DOCTYPE html>
<html lang="jp">
    <head>
        <meta charset="UTF-8">
        <title>my-page</title>
        <link rel="stylesheet" href="./css/my-page.css">
        <link rel="shortcut icon" href="./images/xbp.ico">
    </head>
    <body>
        <main>      
            <header>
                <nav>
                    <ul>
                        <li><a href="../index.html">XBP</a></li>
                        <li><a href="../de12/index.html">デザイン演習Ⅰ・Ⅱ</a></li>
                        <li><a href="../digi_fab/index.html">デジタルファブリケーション</a></li>
                        <li><a href="../digi_fab/Other object.html">その他</a></li>
                    </ul>
                </nav>
            </header>

            <h1>見出しを入力</h1>
            <p> 文章を入力</p>

            <br>
            <button class="button-030"><a href="./e3.html">TOPへ</a></button>
            <br>
            <footer>
                <p>Copy right 2023 Atsuki</p>
            </footer>
        </main>
    </body>
</html>
"""

CSS= """@charset "UTF-8";

header {
    background-color: #333; /* ヘッダーの背景色を設定 */
    color: white; /* ヘッダーテキストの色を設定 */
    padding: 20px; /* ヘッダー内の余白を設定 */
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

nav li {
    display: inline;
    margin-right: 20px;
}

nav a {
    text-decoration: none;
    color: white; /* ナビゲーションリンクのテキスト色を設定 */
}

main{
    background-color: #b4c1d1;
}

.quote-001 {
    max-width: 500px;
    background-color: #ffffff;
    padding: 1em 1.5em;
    border-left: 4px solid #d6dde3;
    color: #333333;
}

.quote-001:has(cite) {
    padding-bottom: .5em;
}

.quote-001 p {
    margin-top: 0;
}

.quote-001 p:last-of-type {
   margin-bottom: 0;
}

/* フッタースタイル */
footer {
    text-align: center; /* テキストを中央に配置 */
    background-color: #333; /* フッターの背景色を設定 */
    color: white; /* フッターテキストの色を設定 */
    padding: 10px; /* フッター内の余白を設定 */
}

.footer a{
    
    display: inline-block;
    justify-content: center;
    color: #ffffff;
    list-style: none;

}

.box{
    position: relative;
    background-color: #ffffff;
    margin: 1em auto;
    padding: 1em 1.5em;
    border: 2px solid #2589d0;
    border-radius: 3px;
    color: #333;
}

.box::before {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    border-radius: 3px;
    background-color: #2589d0;
    color: #fff;
    font-weight: 600;
    content: attr(data-number);
}

.sns-button {
    display: flex;
    justify-content: center;
    margin-top: 20px;
    }

.sns-button li {
    width: 30px;
    margin-left: 10px;
    margin-right: 10px;
    list-style: none;
    margin: 0 20px;
    }

    a{
        text-align: center;
        font-size: 20px;
        color: #000000;
    }

    .button-030 {
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        width: 250px;
        margin:0 auto;
        padding: .9em 2em;
        border: 1px solid #2589d0;
        border-radius: 25px;
        background-color: #2589d0;
        color: #2589d0;
        font-size: 1em;
    }
    
    .button-030:hover {
        animation: anima-button-030 1s;
    }
    
    @keyframes anima-button-030 {
        0% {
            box-shadow: 0 0 0 0 rgb(37 137 208 / 50%);
        }
        100% {
            box-shadow: 0 0 0 1.2em rgb(0 0 0 / 0%);
        }
    }


"""

with open("my-page.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("my-page.css", "w", encoding="utf=8") as f:
    f.write(CSS)
