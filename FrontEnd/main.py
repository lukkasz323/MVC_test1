import http.client


def main():
    print('[FrontEnd]')
    
    conn = http.client.HTTPConnection('127.0.0.1')
    conn.connect()
    conn.request('', '')

if __name__ == '__main__':
    main()