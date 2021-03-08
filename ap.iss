; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Adivinha a Palavra"
#define MyAppVersion "0.4.012021"
#define MyAppPublisher "ArtesGC Inc."
#define MyAppURL "http://artesgc.home.blog"
#define MyAppExeName "jogo_adivinha_palavra.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{F5586444-E486-40D1-8E21-72E54C4E5F71}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
VersionInfoCompany={#MyAppPublisher}
VersionInfoCopyright="Nurul GC"
VersionInfoDescription="Jogo com objectivo de Adivinhar a Palavra selecionada (letra por letra)"
VersionInfoOriginalFileName={#MyAppName}
VersionInfoProductName="Jogo {#MyAppName}"
VersionInfoProductTextVersion={#MyAppVersion}
VersionInfoProductVersion={#MyAppVersion}
VersionInfoTextVersion={#MyAppVersion}
VersionInfoVersion={#MyAppVersion}
DisableDirPage=yes
DisableProgramGroupPage=yes
; The [Icons] "quicklaunchicon" entry uses {userappdata} but its [Tasks] entry has a proper IsAdminInstallMode Check.
UsedUserAreasWarning=no
LicenseFile=D:\Projectos\GC-Jogos\Jogo_Adivinha_Palavra\pt\license_AFL(pt).txt
InfoAfterFile=D:\Projectos\GC-Jogos\Jogo_Adivinha_Palavra\LEIA.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=D:\Projectos\GC-Jogos\Jogo_Adivinha_Palavra\pt\dist
OutputBaseFilename=Adivinha a Palavra (JOGO)
SetupIconFile=D:\Projectos\GC-Jogos\Jogo_Adivinha_Palavra\pt\img\adivinhapalavra_gc.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "portuguese"; MessagesFile: "compiler:Languages\Portuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
Source: "D:\Projectos\GC-Jogos\Jogo_Adivinha_Palavra\pt\dist\jogo_adivinha_palavra.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projectos\GC-Jogos\Jogo_Adivinha_Palavra\pt\img\*"; DestDir: "{app}\img"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\Projectos\GC-Jogos\Jogo_Adivinha_Palavra\pt\license_AFL(pt).txt"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

