from ..errors.fatal_exception import FatalException
from ..log.language import translate


class CamError(RuntimeError):
    pass


class CamerasOffException(FatalException):
    def __init__(self) -> None:
        super().__init__(
            *translate(
                {
                    "ja": (
                        "カメラがオフの場合",
                        "問題が解決しない場合、絞り機でMindhiveのキャビネットをパワーサイクルしてください。",
                    ),
                    "es": (
                        "Las cámaras están apagadas",
                        "Si el problema persiste trate de reiniciar el gabinete de Mindhive localizado cerca del exprimidor.",
                    ),
                    "it": (
                        "Le telecamere sono spente.",
                        "Se il problema persiste, prova a riavviare l'alimentazione del cabinet Mindhive presso lo spremiagrumi.",
                    ),
                    "de": (
                        "Die Kameras sind ausgeschaltet",
                        "Falls das Problem weiterhin besteht, versuchen Sie, den Mindhive-Schrank am Wringer neu zu starten",
                    ),
                    "en": (
                        "Cameras are turned off",
                        "If the problem persists try power cycling the Mindhive cabinet at the wringer.",
                    ),
                }
            ),
        )


class CamerasMissingException(FatalException):
    def __init__(self, indexes: list[int]) -> None:
        super().__init__(
            *translate(
                {
                    "ja": (
                        f'カメラ{", ".join(str(i) for i in indexes)}がオフラインの場合',
                        [
                            "絞り機の裏を見た時に一番右にあるのがカメラ0です。",
                            "",
                            "問題が解決しない場合、絞り機でMindhiveのキャビネットをパワーサイクルしてください。",
                            "",
                            'カメラの"ステータス"のLEDがついているか確認してください。',
                        ],
                    ),
                    "es": (
                        f'Las cámaras {", ".join(str(i) for i in indexes)} están apagadas',
                        [
                            "Desde la perspectiva de la salida del exprimidor, mirando hacia el exprimidor, la cámara 0 está a su mano derecha.",
                            "",
                            "Verifique el estado (color)  encima de la misma cámara.",
                        ],
                    ),
                    "it": (
                        (
                            f"La camera {indexes[0]} è offline"
                            if len(indexes) == 1
                            else f'Le telecamere {" e ".join(str(i) for i in indexes)} sono offline'
                        ),
                        [
                            "Guardando nella parte posteriore dello spremiagrumi, la telecamera 0 è quella più a destra.",
                            "",
                            "Se il problema persiste, prova a riavviare l'alimentazione del cabinet Mindhive presso lo spremiagrumi.",
                            "",
                            "Controlla il LED di stato sulla parte superiore della telecamera stessa.",
                        ],
                    ),
                    "de": (
                        (
                            f"Kamera {indexes[0]} ist offline"
                            if len(indexes) == 1
                            else f"Kameras {", ".join(str(i) for i in indexes)} sind offline"
                        ),
                        [
                            "Wenn man auf die Rückseite des Wringers schaut, ist Kamera 0 die rechte Kamera",
                            "",
                            "Falls das Problem weiterhin besteht, versuchen Sie, den Mindhive-Schrank am Wringer neu zu starten.",
                            "",
                            "Überprüfen Sie die Status-LED oben an der Kamera selbst.",
                        ],
                    ),
                    "en": (
                        (
                            f"Camera {indexes[0]} is offline"
                            if len(indexes) == 1
                            else f'Cameras {", ".join(str(i) for i in indexes)} are offline'
                        ),
                        [
                            "When looking into the back of the wringer camera 0 is the right most camera.",
                            "",
                            "If the problem persists try power cycling the Mindhive cabinet at the wringer.",
                            "",
                            "Check the status LED on the top of camera itself.",
                        ],
                    ),
                }
            ),
        )
