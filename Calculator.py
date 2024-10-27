<!DOCTYPE html>
<html>
    <head>
        <title>Load and Testing</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #e6f2ff;
            }
            .card {
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                padding: 20px;
                width: 300px;
                text-align: center;
            }
            h1 {
                color: #0066cc;
                margin-top: 0;
            }
            form {
                margin-top: 20px;
            }
            input[type="number"] {
                margin: 5px 0;
                padding: 10px;
                width: calc(100% - 20px);
                box-sizing: border-box;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            .operation-buttons {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 5px;
                margin: 10px 0;
            }
            .operation-button {
                background-color: #0066cc;
                color: white;
                border: none;
                padding: 10px;
                cursor: pointer;
                border-radius: 4px;
            }
            .operation-button:hover {
                background-color: #004080;
            }
            .action-buttons {
                display: flex;
                justify-content: space-between;
                margin-top: 10px;
            }
            .action-button {
                background-color: #0066cc;
                color: white;
                border: none;
                padding: 10px;
                cursor: pointer;
                width: calc(50% - 5px);
                border-radius: 4px;
            }
            .action-button:hover {
                background-color: #004080;
            }
            .result {
                font-size: 18px;
                margin-top: 20px;
                min-height: 27px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Load and Testing<br>[FastAPI] Calculator</h1>
            <form action="/calculate" method="post">
                <input type="number" name="firstDigit" required placeholder="Enter Number">
                <div class="operation-buttons">
                    <button type="button" class="operation-button" onclick="setOperation('+')">+</button>
                    <button type="button" class="operation-button" onclick="setOperation('-')">-</button>
                    <button type="button" class="operation-button" onclick="setOperation('*')">×</button>
                    <button type="button" class="operation-button" onclick="setOperation('/')">÷</button>
                </div>
                <input type="hidden" name="operation" id="operation" required>
                <input type="number" name="secondDigit" required placeholder="Enter Number">
                <div class="action-buttons">
                    <button type="submit" class="action-button">Calculate</button>
                    <button type="button" class="action-button" onclick="clearResult()">Reset</button>
                </div>
            </form>
            <div id="result" class="result">
                {% if error %}
                    <p>{{ error }}</p>
                {% elif result is not none %}
                    <p>{{ firstDigit }} {{ operation }} {{ secondDigit }} = {{ result }}</p>
                {% endif %}
            </div>
        </div>

        <script>
            function setOperation(op) {
                document.getElementById('operation').value = op;
                const buttons = document.querySelectorAll('.operation-button');
                buttons.forEach(button => {
                    button.style.backgroundColor = button.textContent === op ? '#004080' : '#0066cc';
                });
            }

            function clearResult() {
                document.getElementById('result').innerHTML = '';
                document.querySelector('form').reset();
                const buttons = document.querySelectorAll('.operation-button');
                buttons.forEach(button => {
                    button.style.backgroundColor = '#0066cc';
                });
            }
        </script>
    </body>
</html>
