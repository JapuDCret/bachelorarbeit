@Injectable({ providedIn: 'root' })
export class ShoppingCartDataSource extends DataSource<ShoppingCartItem> {
  constructor(
    private log: NGXLogger,
    private cartService: ShoppingCartService,
    private localizationService: LocalizationService,
    private tracer: Tracer
  ) {
    super();
  }

  getAndMapShoppingCart(shoppingCartId: string) {
    const span = this.tracer.startSpan( 'ShoppingCartDataSource.getAndMapShoppingCart', { /* Attribute */} );

    this.log.debug('getAndMapShoppingCart(): requesting translations');
    const translations$ = this.localizationService.getTranslations(span);
    
    this.log.debug('getAndMapShoppingCart(): requesting shoppingCart');
    const shoppingCart$ = this.cartService.getShoppingCart(shoppingCartId, span);

    return /* ... */;
  }
}
