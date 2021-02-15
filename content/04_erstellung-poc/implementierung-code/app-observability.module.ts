import { NGXLogger } from 'ngx-logger';

import { Tracer } from '@opentelemetry/tracing'
import { Meter } from '@opentelemetry/metrics';

import { AppConfig, APP_CONFIG } from 'src/app/app-config-module';
import { SplunkForwardingService } from 'src/app/shared/splunk-forwarding-svc/splunk-forwarding.service';

const tracerFactory = (log: NGXLogger, config: AppConfig): Tracer => {
  /* Logik zum Erstellen des Tracers */
  return tracer;
};

const meterFactory = (splunkFwdSvc: SplunkForwardingService): Meter => {
  /* Logik zum Erstellen des Meters */
  return meter;
};

const requestCountMetric = (meter: Meter): CounterMetric => {
  return meter.createCounter('requestCount') as CounterMetric;
};


@NgModule({
  providers: [
    {
      provide: Tracer,
      useFactory: tracerFactory,
      deps: [ NGXLogger, APP_CONFIG ]
    },
    {
      provide: Meter,
      useFactory: meterFactory,
      deps: [ SplunkForwardingService ]
    },
    {
      provide: CounterMetric,
      useFactory: requestCountMetric,
      deps: [ Meter ]
    },
  ]
})
export class AppObservabilityModule {
  constructor() {}
}
