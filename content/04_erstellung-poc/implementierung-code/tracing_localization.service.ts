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
    
    // start span with provided span as a parent
    const span = this.traceUtil.startChildSpan(
        this.tracer, 'LocalizationService.getTranslations', parentSpan,
        { 'shoppingCartId': window.customer.shoppingCartId }
    );

    // generate a jaeger-compatible trace header from OTel span
    const jaegerTraceHeader = this.traceUtil.serializeSpanContextToJaegerHeader(span.context());

    // increment the requestCounter metric
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
            // handle and record exception
            span.recordException({ code: err.status, name: err.name, message: err.message });
            span.end();
          }
        ),
      );
  }
}
