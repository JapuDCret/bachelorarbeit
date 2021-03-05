export class RecordConsentDialogComponent {
  constructor(
    public dialogRef: MatDialogRef<RecordConsentDialogComponent>,
    @Inject(APP_CONFIG) private config: AppConfig
  ) { }

  closeDialog() {
    this.dialogRef.close(window.logrocketData.sessionURL);
  }

  activateLogRocket() {
    // Initialisiere die Aufnahme mit LogRocket
    LogRocket.init(this.config.logRocketAppId, {});

    // Starte eine neue Sitzung
    LogRocket.startNewSession();

    // Stelle die LogRocket sessionURL bereit
    LogRocket.getSessionURL((sessionURL) => {
      window.logrocketData.sessionURL = sessionURL;

      this.dialogRef.close(sessionURL);
    });
  }
}
