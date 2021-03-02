export class RecordConsentDialogComponent {
  constructor(
    public dialogRef: MatDialogRef<RecordConsentDialogComponent>,
    @Inject(APP_CONFIG) private config: AppConfig
  ) { }

  closeDialog() {
    this.dialogRef.close(window.logrocketData.sessionURL);
  }

  activateLogRocket() {
    // initialize session recording
    LogRocket.init(this.config.logRocketAppId, {});

    // start a new session
    LogRocket.startNewSession();

    // pass unique "session"-id to LogRocket
    LogRocket.identify(window.customer.shoppingCartId);

    // make sessionURL accessable
    LogRocket.getSessionURL((sessionURL) => {
      window.logrocketData.sessionURL = sessionURL;

      this.dialogRef.close(sessionURL);
    });
  }
}
