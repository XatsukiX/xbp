html = """<!DOCTYPE html>
<html lang="jp">
  <head>
      <title>授業名</title>
      <link rel="stylesheet" href="./css/class.css">
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Kiwi+Maru:wght@300&display=swap" rel="stylesheet">
      <style>
      body{
        background-color:lavenderblush;
      }
      </style>
      
  </head>
  <body>
    <main>

      <div>
        <div style="padding: 1rem; border-left: 6px double #263f1f; font-size: 20px;">
          <h2>授業名</h2>
        </div>
      
      </div>

    </main>
    

  </body>
</html>

"""




with open("class.html", "w", encoding="utf-8") as f:
    f.write(html)

