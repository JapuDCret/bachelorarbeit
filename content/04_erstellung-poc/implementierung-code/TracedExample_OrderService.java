@ApplicationScoped
public class OrderService {

    @Inject
    private ValidationService validation;

    @Traced(operationName = "OrderService.placeOrder")
    public Receipt placeOrder(Order order, ShoppingCart shoppingCart) {
        validation.validateBillingAddress(order.getBillingAddress());

        validation.validateShippingData(order.getShippingData());

        /* Berechnung zur Bestellung */

        return new Receipt(/* Belegdaten */);
    }
}
