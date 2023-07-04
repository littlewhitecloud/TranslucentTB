from ctypes import (
    POINTER,
    Structure,
    byref,
    c_int,
    c_size_t,
    c_uint,
    cast,
    pointer,
    sizeof,
    windll,
)
from ctypes.wintypes import BOOL, DWORD, HRGN, HWND


class ACCENTPOLICY(Structure):
    _fields_ = [
        ("AccentState", c_uint),
        ("AccentFlags", c_uint),
        ("GradientColor", c_uint),
        ("AnimationId", c_uint),
    ]


class WINDOWCOMPOSITIONATTRIBDATA(Structure):
    _fields_ = [
        ("Attribute", c_int),
        ("Data", POINTER(c_int)),
        ("SizeOfData", c_size_t),
    ]


class DWM_BLURBEHIND(Structure):
    _fields_ = [
        ("dwFlags", DWORD),
        ("fEnable", BOOL),
        ("hRgnBlur", HRGN),
        ("fTransitionOnMaximized", BOOL),
    ]


class MARGINS(Structure):
    _fields_ = [
        ("cxLeftWidth", c_int),
        ("cxRightWidth", c_int),
        ("cyTopHeight", c_int),
        ("cyBottomHeight", c_int),
    ]


SetWindowCompositionAttribute = windll.user32.SetWindowCompositionAttribute
SetWindowCompositionAttribute.argtypes = (HWND, WINDOWCOMPOSITIONATTRIBDATA)
SetWindowCompositionAttribute.restype = c_int


def HEXtoRGBAint(HEX: str):
    alpha = HEX[7:]
    blue = HEX[5:7]
    green = HEX[3:5]
    red = HEX[1:3]
    gradientColor = alpha + blue + green + red
    return int(gradientColor, base=16)


def blur(blurtype: str = "acrylic", hexColor: str = "", spechwnd: int = None):
    hwnd = spechwnd if spechwnd else windll.user32.FindWindowW("Shell_TrayWnd", None)

    accent = ACCENTPOLICY()
    accent.AccentState = 3
    gradientColor = 0
	
    if hexColor:
        accent.AccentFlags = 2
        gradientColor = (
            HEXtoRGBAint(hexColor)
        )

    if blurtype == "clear":
        accent.AccentState = 2
    elif blurtype == "noeffect":
        accent.AccentState = 1
    elif blurtype == "blur":
        DWM_BB_ENABLE = 0x01
        bb = DWM_BLURBEHIND()
        bb.dwFlags = DWM_BB_ENABLE
        bb.fEnable = 1
        bb.hRgnBlur = 1
        windll.dwmapi.DwmEnableBlurBehindWindow(hwnd, byref(bb))
    elif blurtype == "acrylic":
        accent.AccentState = 4
    accent.GradientColor = gradientColor

    data = WINDOWCOMPOSITIONATTRIBDATA()
    data.Attribute = 19
    data.SizeOfData = sizeof(accent)
    data.Data = cast(pointer(accent), POINTER(c_int))

    SetWindowCompositionAttribute(int(hwnd), data)
