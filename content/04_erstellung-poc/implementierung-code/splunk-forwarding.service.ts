export class SplunkForwardingService {
  private batchQueue: SplunkEntry[] = [];
  
  constructor(private http: HttpClient) {
    // Prüfe alle 5s ob Daten zum Weiterleiten existieren
    interval(5000)
      .subscribe(() => {
        const batch = this.batchQueue;

        this.batchQueue = [];

        this.sendBatch(batch)
          .pipe(
            // 5 Versuche mit einer Wartezeit von jeweils 15s
            retryWhen(errors => errors.pipe(delay(15000), take(5)))
          )
          .subscribe();
      });
  }

  public forwardEvents(entries: SplunkEntry[]): void {
    for(const entry of entries) {
      // Füge Kontextinformationen hinzu
      entry.event.path = window.location.href;
      entry.event.shoppingCartId = window.customer.shoppingCartId;

      this.batchQueue.push(entry);
    }
  }

  private sendBatch(batch: SplunkEntry[]): Observable<void> {
    return this.http.post<void>(this.logBatchServiceUrl, batch);
  }
}
