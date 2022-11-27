import requests

cookie = '__LOCALE__null=ID; SPC_F=sWOTBG2425bU5a0ElZH3UYo23XPteklY; REC_T_ID=2fbee491-6dcb-11ed-8692-b47af14ab854; csrftoken=tlh4nNdukpMz84vk0wKyuzSAZgxzQd3m; _QPWSDCXHZQA=ef1ea53a-ba1c-4e1c-9b8d-68acb8728921; G_ENABLED_IDPS=google; SPC_P_V=EbJgeD8MPXfeqjsddAy7Jmsr/R4imJGCpTupIXKqZnzEvyF1eakktgvAZLhejEWnVouCq7GltJ80c5fUQb8oNIACq+lchMiLgiAL50j+R36k2DUaP0/cGsw1woJb/9Da7WT6FdtuLmD6Ft32+CnOXsnivmnzI8hIpt3f6MiwiJ0=; SPC_CLIENTID=c1dPVEJHMjQyNWJVjsbgwhyzrgucphtt; SPC_ST=.aENsRVR0bFJ0SkR6WVp4UW800v7/mCaTIqUOg9YdOTb15Mrfgl7k+r9LTPj2Vu7E7VgIwmUYW96O/zSsncPdOzmVvcJLm65BoJi2yI3LQiwUCjAEfsygwTOIyu7tDzdDWAnys582XPJ/B7x7f5jAs6e3bQpBSN40d9ZLE0QQy6nwv/r1X92Ab79jov4IbhgFJywWPlVdt9ENoO3txaJh8Q==; SPC_U=233744366; SPC_T_ID=cYhxeBo7t8pH7oADH/Do5YktIsrW7AHAA0hQqLq4ljTn/WRluCVbTqV835FK6ZAusW+5IDL4pIkkODdSL5JTzz9eckWkObtyN8dpAcv31sDujQc4VNQEdmqSvWd3bkeOc6cI+gii4hjXQ6hIdIOk4geoYhUcW9/mrZ8gRrdt9pQ=; SPC_T_IV=NTJESXhJcmVkUk5MdkVFWQ==; SPC_IA=1; HAS_BEEN_REDIRECTED=true; SPC_T_IV="NTJESXhJcmVkUk5MdkVFWQ=="; SPC_T_ID="cYhxeBo7t8pH7oADH/Do5YktIsrW7AHAA0hQqLq4ljTn/WRluCVbTqV835FK6ZAusW+5IDL4pIkkODdSL5JTzz9eckWkObtyN8dpAcv31sDujQc4VNQEdmqSvWd3bkeOc6cI+gii4hjXQ6hIdIOk4geoYhUcW9/mrZ8gRrdt9pQ="; shopee_webUnique_ccd=2KRPUvy2hYZR0Jsj00sKWQ%3D%3D%7CPEFICqe%2FssRmYMBYC5%2BK3nwAogOe46WpnEFGNcFr5Eqp4jumVbJYN6UtVKV%2BijqVXk%2FTrXIryi3Go41MY%2B8ZIUWzXUnOmijVPXk%3D%7C%2FEkfg5W2yf9lATbp%7C06%7C3; ds=2d7e42c5d6903f743f455af924dc6082; SPC_EC=MFdaY2FmWDdKOEpINkxBdLEuv1y6zjFtrOF1GMxLqGPR3vnUqVAXjD6IHLA1KOsv6CrsU/GE06X3hSfKg0WzqCHz5U2i4bq+rx81Hcb8/A6q4SGbr/g2m3qF0nTwAjBo4dVRMHPD57eIj23thzn1VdVDmDLz72QGgFCYDFhvTnk=; SPC_R_T_ID="cYhxeBo7t8pH7oADH/Do5YktIsrW7AHAA0hQqLq4ljTn/WRluCVbTqV835FK6ZAusW+5IDL4pIkkODdSL5JTzz9eckWkObtyN8dpAcv31sDujQc4VNQEdmqSvWd3bkeOc6cI+gii4hjXQ6hIdIOk4geoYhUcW9/mrZ8gRrdt9pQ="; SPC_R_T_IV="NTJESXhJcmVkUk5MdkVFWQ=="; SPC_SI=Jbh0YwAAAABkNExOQ2dET6s1AQEAAAAAT0hQSjVzZ1k='
def main():
    asu = requests.get("https://shopee.co.id/api/v4/item/get?itemid=7925814033&shopid=173666539", headers={
        "Host":"shopee.co.id",
        "X-Shopee-Language": "id",
        "If-None-Match-": "8001",
        "accept": "application/json",
        "Sec-Ch-U":"\"; Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "X-API-SOURCE": "pc",
        "Accept": "application/json",
        "Origin": "https://shopee.co.id",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer":"https://shopee.co.id",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "af-ac-enc-dat": "AAYyLjIuMTEAAAGC8gGVGAAAAAABvQAAAAAAAAAABu4eZq0lL7h52o9f7CuwF3A5g75rqgouK+loN/v/p3MxkDpFZT2P2hfqZEDmHHFAmmlMQ+JYTMHF6kF68iRD85aWYi9ro3Wl9b3oSySuEOrgGKGQQJ836vmwS4evtiSZF+8hpeeDkMDl0WXkPHJxWSHdJSL2V2RgO7ZTdl2PzKj1IdJtmTKSF/iVRik4qQPHpZahF4xX9XDEQxZaMiy8FxB0KB/+Z3M6mcDhtM3PtZ2Jbb1Po1xg0v5d9YoE99A0++/hVcuScCn9rmuoaFPIkqb/QfQubeJxMPpEbOf8DabnB03ovh5/6rGSaxMR2cLpyWj3jrNNdgBj3inx/hFfmKOhu7fRXrcNo7k2Uxm8hdGVUZgOvo3vz+IOpcfuM8I9EjNXsEH8wiT/A0HZUldbYMxzhql0JPizgInzqYxo+JHfmbMMaYms5v/5YQyU5T1OK+dceLrCqZsizZTx6GyRUhRlbZfa0O93fHzTKbTBC9GRY7OMsPKRljZ2EI7Zp6aWkWOzjLDykZY2dhCO2aemlpkbjII7/J+vTHjkE+VsZsiRY7OMsPKRljZ2EI7Zp6aW1FalgcGI6E1yaFhUpEHhAw==",
        "X-CSRFToken": "tlh4nNdukpMz84vk0wKyuzSAZgxzQd3m",
        })
    print(asu.text)
def nextto():
    asu = requests.get("http://localhost:8888/server.php?itemid=7925814033&shopid=173666539", headers={
        "Host":"shopee.co.id",
        "X-Shopee-Language": "id",
        "If-None-Match-": "8001",
        "accept": "application/json",
        "Sec-Ch-U":"\"; Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "X-API-SOURCE": "pc",
        "Accept": "application/json",
        "Origin": "https://shopee.co.id",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer":"https://shopee.co.id",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "af-ac-enc-dat": "null",
        "X-CSRFToken": "tlh4nNdukpMz84vk0wKyuzSAZgxzQd3m",
        "Cookie": cookie
        })
    print(asu.json())
main()
