export class SplunkForwardingService {
  // ...
  
  private batchQueue: SplunkEntry[];
  
  constructor(private http: HttpClient) {
    // ...
	
    // Prüfe alle 5s ob Daten zum Weiterleiten existieren
    interval(5000)
      .subscribe(() => {
        const batch = this.batchQueue;

        this.batchQueue = [];

        this.sendBatch(batch)
          .pipe(
            // 5 Versuche mit einer Wartezeit von jew. 15s
            retryWhen(errors => errors.pipe(delay(15000), take(5)))
          )
          .subscribe();
      });
  }

  private sendBatch(batch: SplunkEntry[]): Observable<void> {
    // ...
    
    return this.http.post<void>(this.logBatchServiceUrl, batch);
  }
}
