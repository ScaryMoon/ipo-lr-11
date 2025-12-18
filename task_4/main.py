# Ковалёв Стас Вариант 4
import json

def generate_html():
    with open("C:/Users/User/Desktop/ipo-lr-11/data.json", "r", encoding="utf-8") as f:
        quotes_data = json.load(f)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Quotes Collection</title>
        <style>
            body {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 20px;
            }}
            h1 {{
                text-align: center;
                background: linear-gradient(45deg, #ffffff 0%, #f0f0f0 100%);
                border-radius: 12px;
            }}
            table {{
                width: 80%;
                margin: 20px auto;
                border-collapse: collapse;
                border-radius: 12px;
                overflow: hidden;
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border-bottom: 2px solid rgba(255, 255, 255, 0.3);
            }}
            th {{
                color: white;
            }}
            a {{
                display: block;
                text-align: center;
                font-weight: bold;
                margin-top: 20px;
                color: #000000;
                text-decoration: underline;
                padding: 10px 20px;
                background: white;
                border-radius: 25px;
            }}
        </style>
    </head>
    <body>
        <h1>Quotes Collection</h1>
        <table>
            <thead>
                <tr>
                    <th>Quote</th>
                    <th>Author</th>
                </tr>
            </thead>
            <tbody>
    """

    for quote in quotes_data:
        html_content += f"""
                <tr>
                    <td>{quote['quote']}</td>
                    <td>{quote['author']}</td>
                </tr>
        """

    html_content += f"""
            </tbody>
        </table>
        <a href="https://quotes.toscrape.com/" target="_blank">Источник данных</a>
    </body>
    </html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("HTML-файл успешно сгенерирован: index.html")

if __name__ == "__main__":
    generate_html()