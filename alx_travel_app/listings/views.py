from django.http import HttpResponse

def home(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ALX Travel App</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #f0f4f8;
            }
            .container {
                text-align: center;
            }
            h1 {
                font-size: 2.5em;
                color: #333;
                margin-bottom: 20px;
            }
            .btn {
                background-color: #007bff;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 1em;
                cursor: pointer;
                text-decoration: none;
            }
            .btn:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the ALX Travel App!</h1>
            <a href="/admin/login/" class="btn">Sign in as Admin</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


