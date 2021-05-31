BLACK_STACKOVERFLOW = """
QCalendarWidget QToolButton {
    width: 150px;
}
#qt_calendar_navigationbar {
    max-height: 0px;
}
/* header row */
QCalendarWidget QWidget {
    background-color: rgb(0,0,0);
}
/* normal days */
QCalendarWidget QAbstractItemView:enabled {
    font-size:24px;
    color: rgb(180, 180, 180);
    background-color: white;
    /* */ selection-background-color: rgb(64, 64, 64);
    selection-background-color: rgb(197, 14, 78);
    selection-color: rgb(197, 14, 78);
    border-radius: 0 0 10px 10px;
}
QCalendarWidget QAbstractItemView:disabled {
    color: rgb(0, 64, 64);
    background-color: white;
}
}
"""
