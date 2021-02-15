@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css']
})
export class CheckoutComponent implements OnInit {
  /* andere Methoden */
    
  activateLogRocket() {
    // initialize session recording
    LogRocket.init('<app-id>', {});
    // start a new session
    LogRocket.startNewSession();
    // make sessionURL accessable
    LogRocket.getSessionURL((sessionURL) => {
      window.logrocketData.sessionURL = sessionURL;
    });
    // pass unique "session"-id to LogRocket
    LogRocket.identify(window.customer.shoppingCartId);
  }

  onShoppingCartSubmit(data: CheckoutShoppingCartInfo): void {
    // enrich LogRocket data with ShoppingCart data
    LogRocket.identify(window.customer.shoppingCartId, {
      itemCount: data.itemCount,
      totalSum: data.totalSum
    });
  }

  onBillingAddressSubmit(data: CheckoutBillingAddress): void {
    // enrich LogRocket data with BillingAddress data
    LogRocket.identify(window.customer.shoppingCartId, {
      name: data.firstName + ' ' + data.lastName,
      email: data.email
    });
  }
}
