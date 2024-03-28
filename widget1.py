from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import platform
from jnius import autoclass

if platform == 'android':
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    WifiManager = autoclass('android.net.wifi.WifiManager')
    activity = PythonActivity.mActivity
    wifi_manager = activity.getSystemService(PythonActivity.WIFI_SERVICE)


class WifiToggleWidget(App):
    def build(self):
        self.button = Button(text='Turn WiFi On' if self.is_wifi_enabled() else 'Turn WiFi Off')
        self.button.bind(on_press=self.toggle_wifi)
        return self.button

    def is_wifi_enabled(self):
        if platform == 'android':
            return wifi_manager.isWifiEnabled()

        return False

    def toggle_wifi(self, instance):
        if platform == 'android':
            wifi_manager.setWifiEnabled(not wifi_manager.isWifiEnabled())
            self.button.text = 'Turn WiFi On' if wifi_manager.isWifiEnabled() else 'Turn WiFi Off'


if __name__ == '__main__':
    WifiToggleWidget().run()
