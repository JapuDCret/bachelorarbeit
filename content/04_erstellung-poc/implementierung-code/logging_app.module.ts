import { LoggerModule, NgxLoggerLevel } from 'ngx-logger';

@NgModule({
  declarations: [
    /* Komponenten */
  ],
  imports: [
    /* andere Module */
    LoggerModule.forRoot({
      level: NgxLoggerLevel.DEBUG,
    }),
  ],
})
export class AppModule { }
