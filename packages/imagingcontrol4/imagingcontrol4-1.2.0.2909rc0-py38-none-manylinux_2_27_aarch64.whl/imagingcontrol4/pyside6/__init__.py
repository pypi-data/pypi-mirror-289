
try:
    from PySide6.QtWidgets import QApplication
    _HAS_PYSIDE6 = True
except ImportError:
    _HAS_PYSIDE6 = False

if _HAS_PYSIDE6:
    from .display import DisplayWidget, DisplayWindow

    # Keep the linter happy
    __all_pyside6 = [DisplayWidget, DisplayWindow]

    try:
        from imagingcontrol4pyside6 import DeviceSelectionDlg, PropertyDialog

        __all_pyside6.append(DeviceSelectionDlg)
        __all_pyside6.append(PropertyDialog)
    except ImportError:
        pass
