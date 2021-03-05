@Injectable({ providedIn: 'root' })
export class LocalizationService {
  constructor(
    private log: NGXLogger,
    private http: HttpClient,
    private tracer: Tracer,
    private traceUtil: TraceUtilService,
    private requestCounter: CounterMetric
  ) {}

  public getTranslations(parentSpan?: api.Span) {
    this.log.info('getTranslations(): requesting translations');
    
    // Starte einen neuen Span mit Elternreferenz
    const span = this.traceUtil.startChildSpan(
        this.tracer, 'LocalizationService.getTranslations', parentSpan,
        { 'shoppingCartId': window.customer.shoppingCartId }
    );

    // Generiere aus OTel span einen Jaeger-kompatiblen HTTP-Header
    const jaegerTraceHeader = this.traceUtil.serializeSpanContextToJaegerHeader(span.context());

    // Erhöhe die "requestCounter"-Metric
    this.requestCounter.add(1, { 'component': 'LocalizationService' });

    return this.http.get<Localization>(
        this.localizationServiceUrl,
        { headers: { 'uber-trace-id': jaegerTraceHeader } }
      )
      .pipe(
        tap(
          (val) => {
            this.log.info('getTranslations(): returnVal = ', val);

            span.end();
          },
          (err) => {
            // Protokolliere Fehler
            span.recordException({ code: err.status, name: err.name, message: err.message });
            span.end();
          }
        ),
      );
  }
}
