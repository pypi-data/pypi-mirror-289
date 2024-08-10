from robot.api.deco import keyword
from AppiumLibrary import AppiumLibrary

class AppKeywords:

    def __init__(self):
        self.appium = AppiumLibrary()

    @keyword
    def fw_app_abrir_conexao_app(self, device_name, udid, platform_name):
        """Abre a conexão com o aplicativo móvel, configurando as capacidades do dispositivo com base no sistema operacional.

        Arguments:
        - device_name: Nome do dispositivo.
        - udid: Identificador único do dispositivo.
        - platform_name: Nome da plataforma (Android ou iOS).
        """
        if platform_name == 'Android':
            self.appium.open_application(
                '${APPIUM_URL}/wd/hub',
                platformName=platform_name,
                udid=udid,
                appPackage='${ANDROID_APP_PACKAGE}',
                appActivity='${ANDROID_APP_ACTIVITY}',
                dontStopAppOnReset=False,
                autoGrantPermissions=True
            )
        elif platform_name == 'iOS':
            self.appium.open_application(
                '${APPIUM_URL}/wd/hub',
                automationName='XCUI',
                platformName=platform_name,
                udid=udid,
                platformVersion='${IOS_PLATFORM_VERSION}',
                bundleId='${IOS_BUNDLE_ID}',
                noReset=True,
                autoGrantPermissions=True,
                autoAcceptAlerts=True,
                xcodeOrgId='${XCODE_ORG_ID}',
                xcodeSigningId='${XCODE_SIGNING_ID}'
            )

        self.fw_app_aguardar_splash_screen()

    @keyword
    def fw_app_fechar_conexao_app(self):
        """Fecha a conexão com o aplicativo móvel."""
        self.appium.close_application()

    def fw_app_aguardar_splash_screen(self):
        """Aguarda até que a splash screen seja exibida e esteja visível e habilitada."""
        # Implementar o método de espera da splash screen baseado na aplicação específica.
        pass
