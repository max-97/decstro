from decstro import Model, Attribute, Element


class Delta(Model):
    x: int = Attribute("x")
    y: int = Attribute("y")


class Window(Model):
    x: int = Attribute("x")
    y: int = Attribute("y")


class Screen(Model):
    x: int = Attribute("x")
    y: int = Attribute("y")


class Cursor(Model):
    delta: Delta = Element("Delta")
    window: Window = Element("Window")
    screen: Screen = Element("Screen")


class Buttons(Model):
    bitField: int = Attribute("bitField")


class Modifiers(Model):
    alt: bool = Element("Alt")
    ctrl: bool = Element("Ctrl")
    shift: bool = Element("Shift")
    meta: bool = Element("Meta")


class MouseEvent(Model):
    type: str = Element("Type")
    timestamp: float = Element("Timestamp")
    cursor: Cursor = Element("Cursor")
    buttons: Buttons = Element("Buttons")
    modifiers: Modifiers = Element("Modifiers")


def test_composed_xml():
    xml = """
        <MouseEvent>
            <Type>mousemove</Type>
            <Timestamp>52489.07000000145</Timestamp>
            <Cursor>
                <Delta x="-4" y="8"/>
                <Window x="171" y="480"/>
                <Screen x="586" y="690"/>
            </Cursor>
            <Buttons bitField="0"/>
            <Modifiers>
                <Alt>false</Alt>
                <Ctrl>true</Ctrl>
                <Shift>false</Shift>
                <Meta>false</Meta>
            </Modifiers>
        </MouseEvent>
    """
    mouse_event = MouseEvent(xml)
    assert mouse_event.type == "mousemove"
    assert mouse_event.timestamp == 52489.07000000145
    assert mouse_event.cursor.delta.x == -4
    assert mouse_event.cursor.delta.y == 8
    assert mouse_event.cursor.window.x == 171
    assert mouse_event.cursor.window.y == 480
    assert mouse_event.cursor.screen.x == 586
    assert mouse_event.cursor.screen.y == 690
    assert mouse_event.buttons.bitField == 0
    assert mouse_event.modifiers.alt is False
    assert mouse_event.modifiers.ctrl is True
    assert mouse_event.modifiers.shift is False
    assert mouse_event.modifiers.meta is False
