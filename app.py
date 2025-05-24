from mesop import App

app = App()

@app.page("/")
def main():
    app.text("My Mesop App on AWS App Runner", variant="heading1")
    app.text("Hello from AWS!")
