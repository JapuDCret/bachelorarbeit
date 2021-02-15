@Injectable({ providedIn: 'root' })
export class SplunkForwardingErrorHandler extends ErrorHandler {
    private splunkForwarding: SplunkForwardingService;

    constructor(injector: Injector) {
        super();

        this.splunkForwarding = injector.get(SplunkForwardingService);
    }

    handleError(error, optionalData?: any): void {
        LogRocket.captureException(error);

        const entry: SplunkEntry = {
            sourcetype: 'error',
            event: {
                ...optionalData,
                frontendModel: window.frontendModel,
                // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error
                name: error.name,
                message: error.message,
                stack: error.stack,
                fileName: error.fileName,// non-standard
                lineNumber: error.lineNumber,// non-standard
                columnNumber: error.columnNumber// non-standard
            }
        };

        this.splunkForwarding.forwardEvent(entry);
    }
}