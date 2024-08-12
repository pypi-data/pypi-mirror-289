import os, time
import undetected_chromedriver as uc


class ChromeProxy:

    def __init__(self, host: str, port: int, username: str = "", password: str = ""):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def get_path(self) -> str:
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "proxy_extension"
        )

    def create_extension(self, name: str = "Chrome Proxy", version="1.0.0") -> str:
        proxy_folder = self.get_path()
        os.makedirs(proxy_folder, exist_ok=True)

        # generate manifest (establish extension name and version)
        manifest = ChromeProxy.manifest_json
        manifest = manifest.replace("<ext_name>", name)
        manifest = manifest.replace("<ext_ver>", version)

        # write manifest to extension directory
        with open(f"{proxy_folder}/manifest.json", "w") as f:
            f.write(manifest)

        # generate javascript code (replace some placeholders)
        js = ChromeProxy.background_js
        js = js.replace("<proxy_host>", self.host)
        js = js.replace("<proxy_port>", str(self.port))
        js = js.replace("<proxy_username>", self.username)
        js = js.replace("<proxy_password>", self.password)

        # write javascript code to extension directory
        with open(f"{proxy_folder}/background.js", "w") as f:
            f.write(js)

        return proxy_folder

    manifest_json = """
    {
        "version": "<ext_ver>",
        "manifest_version": 3,
        "name": "<ext_name>",
        "permissions": [
            "proxy",
            "tabs",
            "storage",
            "webRequest",
            "webRequestAuthProvider"
        ],
        "host_permissions": [
            "<all_urls>"
        ],
        "background": {
            "service_worker": "background.js"
        },
        "minimum_chrome_version": "22.0.0"
    }
    """

    background_js = """
    var config = {
        mode: "fixed_servers",
        rules: {
            singleProxy: {
                scheme: "http",
                host: "<proxy_host>",
                port: parseInt("<proxy_port>")
            },
            bypassList: ["localhost"]
        }
    };

    chrome.proxy.settings.set({
        value: config,
        scope: "regular"
    }, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "<proxy_username>",
                password: "<proxy_password>"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
        callbackFn, {
            urls: ["<all_urls>"]
        },
        ['blocking']
    );
    """


if __name__ == "__main__":
    proxy = ChromeProxy(host="localhost", port=3128, username="", password="")
    extension_path = proxy.create_extension()

    options = uc.ChromeOptions()
    options.add_argument(f"--load-extension={extension_path}")

    driver = uc.Chrome(options=options)
    driver.get("https://www.2ip.io/")
    time.sleep(10)
