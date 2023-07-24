from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)  # Wait time between requests

    # Headers
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9,vi;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Referer": "https://thanhmaihskonline.com.vn/ho-tro",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",
        "sec-ch-ua": '"Chromium";v="115", "Not/A)Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    # Cookies
    cookies = {
        "remember_member_59ba36addc2b2f9401580f014c7f58ea4e30989d": "eyJpdiI6IkhiaWpZKzN0WnZsY21pOG9CcW1mNFE9PSIsInZhbHVlIjoiNzlXSnNFNmQrcVNWckpob00wdWk0LzA3VFd0OTNEQ1ZxQUl0VGJtVmxSRmx2NjZvY3FOZWQ5dDFBM1dlei9rUVNHMWM2aXlEd3B5bkZ3OTJuaytUNUJMVGdDV3c2L0Y3Rjh6bEJwNmtVVmdiMUZmcXB2NEx6WEg5MXFTWW1iUkdqNXcxUXlYSU84ZDBjOVU3Nmx6NGd3anZmMkRHR08rR0lTcVpUUjhWUG5PTmxGeW9zUk91L0Evc0tUZCtPcHhPZExhOXhSWXovbTlMRVo1RFJlUnBySmM0aUM4TjJjT01iZzdBQkx2WnhNdz0iLCJtYWMiOiJkMDJkMjY2ZjU3OGQwYjgwMTg0MWU5YzM2MDg5YzAwMjY1NWZiY2M5MjVmZDI0YzhmMTgwM2Y5YzZkZWQ4YjU0IiwidGFnIjoiIn0%3D",
        "XSRF-TOKEN": "eyJpdiI6Ilh4V0NmWTdGd1FxTkhPOFVKMjRJeWc9PSIsInZhbHVlIjoiTlkxbTdLUHFDU0F4ZUNPRW1QSnJXTm03K21MYUpINDk0bkpIaVllNjVxaGNndjVGOUZQa212ZC93WUpoRVdBK1phK05qZDFUWk40Qk90Y2lvUVRNcXVrcUwyUCtCbi8xcXpmQTEwWEVMYzJWQWs1T29zSUlXVUpKb2FBVjFWNDYiLCJtYWMiOiI2ZGU5ZTU5YzRjNDc3MDI2NjVhMTI0NTUwMWFhNzcxODM5MTRiZTMwM2UyOWEwOWU5NzY4NjRhMDZlYzhjNDA1IiwidGFnIjoiIn0%3D",
        "hsk_session": "eyJpdiI6IkxxQ3dxUnRrUnkrbVpYcmw5OGtRNUE9PSIsInZhbHVlIjoibFZXdHlyZ1FsUlBVMERMVml2aEJxZjZ5dGtkb1hxOWJzOGZpSGxYZHVPbnJ1VHBlN29iV2E0NHc5Vm5xS044eWViMUJkTHJkaDZhbHZTMWJrQUFTTFdESkhTK0JDZGQ3bkdFR2g2RzBrZmNkQ3J2bmJ3UTcxWWtMUjhyRTkreXUiLCJtYWMiOiI5MmQxMGEwMGRmY2UzY2U1OGJlYmMxM2NkNmQ4ZDc2ZjM3MDRjMzgxYWEwZmQzMjdmMjIxOTg5OGEyNTYyNjJmIiwidGFnIjoiIn0%3D",
    }

    @task
    def load_main_page(self):
        self.client.get("/", headers=self.headers, cookies=self.cookies)

    @task
    def load_specific_page(self):
        self.client.get("/danh-sach-loai-luyen-tap?skill_id=2&category_id=5", headers=self.headers, cookies=self.cookies)