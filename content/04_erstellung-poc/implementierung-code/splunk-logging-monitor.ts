@Injectable({ providedIn: 'root' })
export class SplunkLoggingMonitor extends NGXLoggerMonitor {
    constructor(
        private log: NGXLogger,
        private splunk: SplunkForwardingService
    ) {
        super();
    }

    onLog(logObject: NGXLogInterface): void {
        const params = this.makeParamsPrintable(logObject.additional);

        const logEvent = {
            sourcetype: 'log',
            event: {
                severity: logObject.level,
                message: logObject.message,
                ...params,
                fileName: logObject.fileName,
                lineNumber: logObject.lineNumber,
                timestamp: logObject.timestamp
            }
        };

        this.splunk.forwardEvent(logEvent);
    }
}
