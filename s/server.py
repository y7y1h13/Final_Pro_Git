import uvicorn

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8443,
                reload=True,
                ssl_keyfile="/usr/bin/mkcert/key.pem", 
                ssl_certfile="/usr/bin/mkcert/cert.pem"
                )    