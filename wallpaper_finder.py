import winreg
import subprocess

reg_handle = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
key_handle = winreg.OpenKey(reg_handle, r"Software\Microsoft\Internet Explorer\Desktop\General")
source = winreg.QueryValueEx(key_handle, 'WallpaperSource')[0]
subprocess.call(['explorer', '/select,{0}'.format(source)])
