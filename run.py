from app import app, db

app.debug = True

if __name__ == '__main__':
    db.create_all()
    app.run()
