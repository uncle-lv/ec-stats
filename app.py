from ec_stats import create_app


app = create_app(dev=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1')
