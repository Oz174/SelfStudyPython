class Button:
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        return 'Render a windows button'


class MacButton(Button):
    def render(self):
        return 'Render a mac button'


class LinuxButton(Button):
    def render(self):
        return 'Render a linux button'


def get_button(os):
    if os == 'Windows':
        return WindowsButton()
    elif os == 'Mac':
        return MacButton()
    else:
        return LinuxButton()


if __name__ == "__main__":
    print("Welcome to Factory Pattern")
    print("This class aims to create an object of a class based on the input provided")
    print("Here, we are creating a button based on the OS provided")
    print("Creating a Windows Button")
    windows_button = get_button('Windows')
    print(windows_button.render())
    print("Creating a Mac Button")
    mac_button = get_button('Mac')
    print(mac_button.render())
    print("Creating a Linux Button")
    linux_button = get_button('Linux')
    print(linux_button.render())
    print("Factory Pattern implemented successfully")
