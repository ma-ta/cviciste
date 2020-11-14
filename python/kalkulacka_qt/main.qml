import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.13

Window {
    title: qsTr("Kalkulačka")
    visible: true
    //flags: "Sheet"
    height: 712
    minimumHeight: 712
    maximumHeight: 712
    width: 430
    minimumWidth: 430
    maximumWidth: 430
    color: "#f3cccccc"

    MouseArea {
        id: mouseArea
        x: 0
        y: 0
        width: parent
        height: parent

        // Zachytávání stisknutých kláves
        Keys.onPressed: {

            // "Escape" = buttonC
            if (event.key === Qt.Key_Escape) {
                buttonC.clicked();
                event.accepted = true;
            }
            if (event.key === Qt.Key_Enter) {
                buttonVysledek.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_Plus) {
                buttonScitani.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_Minus) {
                buttonOdcitani.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_Asterisk) {
                buttonNasobeni.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_Slash) {
                buttonDeleni.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_M) {
                buttonMplus.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_Period || event.key === Qt.Key_Comma) {
                buttonFloat.clicked()
                event.accepted = true;
            }

            if (event.key === Qt.Key_0) {
                button0.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_1) {
                button1.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_2) {
                button2.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_3) {
                button3.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_4) {
                button4.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_5) {
                button5.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_6) {
                button6.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_7) {
                button7.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_8) {
                button8.clicked()
                event.accepted = true;
            }
            if (event.key === Qt.Key_9) {
                button9.clicked()
                event.accepted = true;
            }


        }



        MenuBar {
            width: parent.width
            height: 30
            antialiasing: true

        }

        RoundButton {
            id: roundButtonExit
            ToolTip.visible: hovered
            ToolTip.delay: 500
            ToolTip.text: qsTr("Zavřít")
            x: 7
            y: 7
            width: 16
            height: 16
            antialiasing: true
            font.weight: Font.Normal
            font.bold: false
            padding: 6
            rightPadding: 6
            leftPadding: 6
            bottomPadding: 6
            topPadding: 6
            font.pointSize: 5
            font.family: "Tahoma"
            highlighted: true

            onClicked: mainpy.zavrit_app(0)
        }

        Text {
            id: displej
            x: 6
            y: 36
            width: 418
            height: 140
            text: qsTr("0")
            antialiasing: true
            font.weight: Font.Normal
            bottomPadding: 0
            font.pixelSize: 70
            leftPadding: 20
            font.bold: false
            font.family: "Roboto Light"
            rightPadding: 20
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignRight
            focus: true

        }

        Button {
            id: button0
            x: 112
            y: 606
            width: 100
            height: 100
            text: qsTr("0")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("0")
        }

        Button {
            id: button1
            x: 6
            y: 500
            height: 100
            text: qsTr("1")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("1")
        }

        Button {
            id: button2
            x: 112
            y: 500
            height: 100
            text: qsTr("2")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("2")
        }

        Button {
            id: button3
            x: 218
            y: 500
            height: 100
            text: qsTr("3")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("3")
        }

        Button {
            id: button4
            x: 6
            y: 394
            height: 100
            text: qsTr("4")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("4")
        }

        Button {
            id: button5
            x: 112
            y: 394
            height: 100
            text: qsTr("5")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("5")
        }

        Button {
            id: button6
            x: 218
            y: 394
            height: 100
            text: qsTr("6")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("6")
        }

        Button {
            id: button7
            x: 6
            y: 288
            height: 100
            text: qsTr("7")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("7")
        }

        Button {
            id: button8
            x: 112
            y: 288
            height: 100
            text: qsTr("8")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("8")
        }

        Button {
            id: button9
            x: 218
            y: 288
            height: 100
            text: qsTr("9")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("9")
        }

        Button {
            id: buttonFloat
            x: 218
            y: 606
            height: 100
            text: qsTr(".")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto(".")
        }

        Button {
            id: buttonPlusMinus
            x: 6
            y: 606
            width: 100
            height: 100
            text: qsTr("+/-")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("buttonPlusMinus")
        }

        Button {
            id: buttonVysledek
            x: 324
            y: 606
            width: 100
            height: 100
            text: qsTr("=")
            antialiasing: true
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Bold
            font.bold: false
            flat: false
            highlighted: true
            display: AbstractButton.TextBesideIcon

            onClicked: mainpy.tlacitko_stisknuto("=")
        }

        Button {
            id: buttonScitani
            x: 324
            y: 500
            height: 100
            text: qsTr("+")
            font.strikeout: false
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            antialiasing: true
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("+")
        }

        Button {
            id: buttonOdcitani
            x: 324
            y: 394
            height: 100
            text: qsTr("-")
            font.strikeout: false
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            antialiasing: true
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("-")
        }

        Button {
            id: buttonNasobeni
            x: 324
            y: 288
            height: 100
            text: qsTr("*")
            font.strikeout: false
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            antialiasing: true
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("*")
        }

        Button {
            id: buttonDeleni
            x: 324
            y: 182
            height: 100
            text: qsTr("/")
            font.strikeout: false
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            antialiasing: true
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("/")
        }

        Button {
            id: buttonMminus
            x: 218
            y: 182
            height: 100
            text: qsTr("M-")
            font.strikeout: false
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            antialiasing: true
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("buttonMminus")
        }

        Button {
            id: buttonMplus
            x: 112
            y: 182
            height: 100
            text: qsTr("M+")
            font.strikeout: false
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Normal
            antialiasing: true
            font.bold: false
            flat: false

            onClicked: mainpy.tlacitko_stisknuto("buttonMplus")
        }


        Button {
            id: buttonC
            x: 6
            y: 182
            width: 100
            height: 100
            text: "C"
            antialiasing: true
            font.strikeout: false
            font.pointSize: 10
            font.family: "Roboto"
            font.weight: Font.Bold
            checkable: false
            autoRepeat: false
            checked: false
            highlighted: false
            font.bold: false
            flat: false
            spacing: 6

            onClicked: {
                mainpy.tlacitko_stisknuto("buttonC");
            }

        }
    }
}
