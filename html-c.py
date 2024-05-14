html = """<!DOCTYPE html>
<html lang="jp">
<head>
    <meta charset="UTF-8">
    <title>XBP</title>
    <link rel="stylesheet" href="./css/index.css">
    <link rel="shortcut icon" href="https://xatsukix.github.io/xbp/images/icon2.jpg" type="image/x-icon">
</head>
<body>
    <main>
      <header>
        <ul id="nav">
          <li><a href="../index.html">XBP TOP</a></li>
          <li><a href="https://kuxbp.github.io/xbp/xbp2023/">XBP3期生</a></li>
          <li><a href="../de12/index.html">デザイン演習Ⅰ・Ⅱ</a></li>
          <li><a href="../digi_fab/index.html">デジタルファブリケーション</a></li>
          <li><a href="../de34/index.html">デザイン演習Ⅲ・Ⅳ</a></li>
          <li><a href="../digi_gra/index.html">デジタルグラフィックス</a></li>
          <li><a href="../de56/index.html">デザイン演習Ⅴ・Ⅵ</a></li>
          <li><a href="">ゼミ</a></li>
          <li><a href="../deploy/index.html">開発録</a></li>
          <li><a href="../diary/index.html">備忘録</a></li>
          <li><a href="../digi_fab/Other object.html">その他</a></li>
        </ul>
      </header>

        <div class = box>
            <h1>タイトル</h1>
            <p>
                本文
            </p>
        </div>


      <footer>
        <p>&copy All rights reserved Atsuki</p>
    </footer> 
    </main>
</body>
</html>

"""




with open("my-page.html", "w", encoding="utf-8") as f:
    f.write(html)


